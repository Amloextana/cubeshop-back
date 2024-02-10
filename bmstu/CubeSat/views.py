from django.shortcuts import render

products = [
        {
            'id': 1, 
            'title': 'Корпус CubeSat 1U',
            'price': 6500,
            'image_url': 'images/CS1.jpg', 
            'description': "Солнечная панель Sputnix Orbicraft-Pro SXC-SGS-03 использует GaAs (арсенид галлия) фотоэлектрические преобразователи и встроенные электромагнитные катушки.\nПанель предназначена для установки на боковую кромку корпуса формата 1U CubeSat. Несколько панелей могут быть объединены для установки на боковые кромки корпуса формата 3U. Панель имеет встроенную электромагнитную катушку, которая может быть задействована в системе ориентации и стабилизации аппарата."
        },
        {
            'id': 2, 
            'title': 'Система энергопитания', 
            'price': 5200, 
            'image_url': 'images/CS2.jpg', 
            'description': "Система энергопитания SXC-PSU-03 управляет энергопитанием спутника от аккумуляторного блока SXC-BAT-03 и панелей солнечных батарей (обычно SXC-SSS-03, SXC-SSE-03, SXC-SGS-03 или SXC-SGE-03), которые могут подключаться в количестве до 14 штук. Контакт для зарядки внешних аккумуляторов находится на разъеме PC104 и, как правило, соединяется с разъемом USB сервисной панели SXC-SP-03. Для обмена данных с аккумуляторным блоком используется специальный интерфейс.\nСистема энергопитания позволяет использовать солнечные панели со встроенными электромагнитными катушками. На плате системы энергопитания находятся три входных разъема для солнечных панелей, по одному разъему на ось спутника. Солнечные панели каждой оси соединены между собой кабельной системой и подключаются к отдельному разъему. Это позволяет наращивать катушки, встроенные в каждую солнечную панель, для суммирования их магнитных полей. Подключение катушек к драйверам производится через разъем PC104. Зарядные устройства использую алгоритм отслеживания точки максимальной мощности (MPPT, окончания зарядки) и поддерживают два типа фотоэлементов: GaAs и Si при условии правильного уровня напряжения."
        },
        {   
            'id': 3, 
            'title': 'Солнечная панель с GaAs', 
            'price': 8400, 
            'image_url': 'images/CS3.jpg', 
            'description': "Солнечная панель Sputnix Orbicraft-Pro SXC-SGS-03 использует GaAs (арсенид галлия) фотоэлектрические преобразователи и встроенные электромагнитные катушки.\nПанель предназначена для установки на боковую кромку корпуса формата 1U CubeSat. Несколько панелей могут быть объединены для установки на боковые кромки корпуса формата 3U. Панель имеет встроенную электромагнитную катушку, которая может быть задействована в системе ориентации и стабилизации аппарата."
        },
    ]



draft_application = {
    'customer_email': "cust@mail.ru",

    'cart_data': [
            {
            'id': 1, 
            'title': 'Корпус CubeSat 1U',
            'price': 6500,
            'image_url': 'images/CS1.jpg', 
            'amount': 3
            },
            {
            'id': 2, 
            'title': 'Система энергопитания', 
            'price': 5200, 
            'image_url': 'images/CS2.jpg', 
            'amount': 2
            }
    ]
}


def show_cart(request):
    return render(request, 'draft_application.html', {'draft_application': draft_application})


def GetDetail(request, id):
    for my_dict in products:
        if my_dict['id'] == id:
            print(my_dict['title'])
            return render(request, 'detail.html', {'product': my_dict})


def GetDetails(request):
    local_products = products[:]
    if request.method == 'GET':
        max_price = request.GET.get('max_price', None)
        if max_price is not None:
            try:
                max_price = int(max_price)
                local_products = [product for product in local_products if product['price'] <= max_price]
            except ValueError:
                pass
    return render(request, 'details.html', {'products': local_products})
