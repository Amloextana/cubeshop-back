from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetOrders(request):
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'orders': [
            {'title': 'Книга с картинками', 'id': 1},
            {'title': 'Бутылка с водой', 'id': 2},
            {'title': 'Коврик для мышки', 'id': 3},
        ]
    }})


def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})



def product_list(request):
    # Ваши товары с ценами
    products = [
        {'title': 'Книга с картинками', 'price': 6500, 'image_url': 'images/CUBE1.jpg', 'id': 1},
        {'title': 'Бутылка с водой', 'price': 5200, 'image_url': 'images/CS2.jpg', 'id': 2},
        {'title': 'Коврик для мышки', 'price': 8400, 'image_url': 'images/CS3.jpg', 'id': 3},
    ]

    # Проверяем, был ли отправлен POST-запрос
    if request.method == 'POST':
        # Получаем значение цены из POST-запроса
        max_price = request.POST.get('max_price', None)
        # Фильтруем товары по цене, если указана минимальная цена
        if max_price is not None:
            try:
                max_price = int(max_price)  # Преобразуем значение в число
                products = [product for product in products if product['price'] <= max_price]
            except ValueError:
                pass  # Обработка ошибки, если введено некорректное значение

    return render(request, 'product_list.html', {'products': products})


def sendText(request):
    input_text = request.POST['text']