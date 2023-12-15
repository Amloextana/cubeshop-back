from django.shortcuts import render, redirect, get_object_or_404
import psycopg2
from django.conf import settings
from django.http import HttpResponseNotFound
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductsSerializer, OrderSerializer, OrdersToProductsSerializer, OrderWithProductsSerializer
from .models import Products, Orders, OrdersToProducts


def create_connect():
    db_settings = settings.DATABASES['default']
    conn = psycopg2.connect(
        dbname=db_settings['NAME'],
        user=db_settings['USER'],
        password=db_settings['PASSWORD'],
        host=db_settings['HOST'],
        port=db_settings['PORT'],
    )
    return conn


def deactivate_product(request, product_id):
    conn = create_connect()
    cur = conn.cursor()
    cur.execute('UPDATE "CubeSat_products" SET is_active = False WHERE id = %s', (product_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('product_list')


def GetProductDetail(request, id):
    conn = create_connect()
    cur = conn.cursor()
    cur.execute('SELECT name, description, price, image FROM "CubeSat_products" WHERE id = %s ', (id,))
    result = cur.fetchone()
    cur.close()

    def get_cube_sat_attributes(product_id):
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT a.attribute_name, v.attribute_value
                FROM "CubeSat_attributesvalues" v
                INNER JOIN "CubeSat_attributes" a ON v.attribute_ref_id = a.id
                WHERE v.product_ref_id = %s;
            """, [product_id])
            rows = cursor.fetchall()
        attributes_dict = {}
        for row in rows:
            attributes_dict[row[0]] = row[1]
        return attributes_dict

    if result:
        attrib_dict = get_cube_sat_attributes(id)
        product = {
            'title': result[0],
            'description': result[1],
            'price': result[2],
            'image_url': result[3].split('static/', 1)[-1],
            'id': id,
            'details': attrib_dict
        }
        return render(request, 'CubeSat/detail.html', {'product': product})
    else:
        return HttpResponseNotFound("Продукт не найден")


def ProductList(request):
    conn = create_connect()
    cur = conn.cursor()
    cur.execute('SELECT id, name, description, price, image FROM "CubeSat_products" WHERE is_active = True')
    results = cur.fetchall()
    cur.close()
    conn.close()

    local_products = []
    for result in results:
        local_products.append({
            'id': result[0],
            'title': result[1],
            'description': result[2],
            'price': result[3],
            'image_url': result[4].split('static/', 1)[-1],
        })

    if request.method == 'GET':
        max_price = request.GET.get('max_price', None)
        if max_price is not None:
            try:
                max_price = int(max_price)
                local_products = [product for product in local_products if product['price'] <= max_price]
            except ValueError:
                pass

    return render(request, 'CubeSat/details.html', {'products': local_products})


@api_view(['Get'])
def get_list_of_products(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['Get'])
def get_product(request, id):
    product = Products.objects.filter(pk=id).last()
    if not product:
        return Response("Выбран несуществующий продукт")

    serializer = ProductsSerializer(product)
    return Response(serializer.data)


@api_view(['Get'])
def get_list_of_orders(request):
    orders = Orders.objects.all()
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_order(request, id):
    orders = Orders.objects.filter(pk=id).last()
    if not orders:
        return Response("Выбран несуществующий заказ")
    serializer = OrderWithProductsSerializer(orders)
    return Response(serializer.data)




@api_view(['Put'])
def update_price(request, id):
    product = Products.objects.filter(pk=id).last()
    if not product:
        return Response("Выбран несуществующий продукт")
    serializer = ProductsSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def update_order_status(request, id):

    order = Orders.objects.filter(pk=id).last()
    if not order:
        return Response("Выбран несуществующий заказ")

    new_status = request.data.get('status')

    if new_status in ['In Progress', 'Completed', 'Cancelled']:
        order.status = new_status
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    else:
        return Response({'error': 'Invalid status'}, status=400)


# Добавление продукта к открытому заказу (если открытого заказа у пользователя нет, то создаем заказ)
@api_view(["POST"])
def add_product_to_order(request):
    customer_id = 2
    moderator_id = 1

    product = Products.objects.get(pk=request.data.get("product_ref"))
    if not product:
        return Response("Выбран несуществующий продукт")

    order = Orders.objects.get(status="Pending", customer=customer_id)
    if not order:
        order = Orders.objects.create(status="Pending", customer_id=customer_id,
                                      moderator_id=moderator_id)

    serializer = OrdersToProductsSerializer(data={"order_ref": order.pk, "product_ref": product.pk, "amount": request.data["amount"]})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Post'])
def add_product(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Delete'])
def delete_product(request, id):
    product = Products.objects.filter(pk=id).last()
    if not product:
        return Response("Выбран несуществующий продукт")
    product_in_orders = OrdersToProducts.objects.filter(product_ref=id)
    product_in_orders.delete()
    product.is_active = False
    product.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

