from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


products = [
        {'title': 'Корпус CubeSat 1U', 'price': 6500, 'image_url': 'images/CS1.jpg', 'id': 1},
        {'title': 'Система энергопитания', 'price': 5200, 'image_url': 'images/CS2.jpg', 'id': 2},
        {'title': 'Солнечная панель с GaAs', 'price': 8400, 'image_url': 'images/CS3.jpg', 'id': 3},
    ]


def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetOrders(request):
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'orders': products
    }})


def GetOrder(request, id):

    # проходим по списку словарей
    for my_dict in products:
        # проверяем, есть ли нужный id в текущем словаре
        if my_dict['id'] == id:
            # если да, выводим соответствующий текст
            print(my_dict['title'])
            return render(request, 'order.html', {'my_dict': my_dict})


def product_list(request):
    return render(request, 'product_list.html', {'products': products})


def sendText(request):
    input_text = request.POST['text']