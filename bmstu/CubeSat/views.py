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
    products = [
        {'title': 'Книга с картинками', 'description': 'Описание книги с картинками', 'image_url': 'images/CUBE1.jpg', 'id': 1},
        {'title': 'Бутылка с водой', 'description': 'Описание бутылки с водой', 'image_url': 'images/CS2.jpg', 'id': 2},
        {'title': 'Коврик для мышки', 'description': 'Описание коврика для мышки', 'image_url': 'images/CS3.jpg', 'id': 3},
    ]
    return render(request, 'product_list.html', {'products': products})
