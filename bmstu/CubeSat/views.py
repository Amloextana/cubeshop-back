from django.shortcuts import render, redirect
import psycopg2
from django.conf import settings
from django.http import HttpResponseNotFound

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
    conn.close()

    if result:
        product = {
            'title': result[0],
            'description': result[1],
            'price': result[2],
            'image_url': result[3].split('static/', 1)[-1],
            'id': id,
        }
        return render(request, 'detail.html', {'product': product})
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

    return render(request, 'details.html', {'products': local_products})

