from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from .models import Components, Users, Applications, Applicationscomponents
from .serializers import ComponentSerializer


class ComponentsModelTest(TestCase):
    """
        Создаем компонент и проверяем что он возвращается корректно при вызове 
        /component/, /components/{id}/
    """
    def setUp(self):
        self.component = Components.objects.create(
            id=1,
            title="Component 1",
            category="Category 1",
            description="Description of component 1",
            features="Feature 1, Feature 2",
            available=True,
            image="path/to/image.jpg",
            price=Decimal('99.99')
        )

    def test_get_components(self):
        
        response = self.client.get('/components/')

        components = Components.objects.filter(available=True)
        serializer = ComponentSerializer(components, many=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'components': serializer.data})

    def test_get_component(self):
        
        response = self.client.get('/components/1/')

        component = Components.objects.get(pk=1)
        serializer = ComponentSerializer(component)
        

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)



class UsersModelTest(TestCase):
    """
        Проверяем создание обычного пользователя и модератора
    """
    def test_create_moderator(self):
        data = {
            'email': 'admin@example.com',
            'password': 'adminpassword',
            'is_moderator': True  
        }

        response = self.client.post('/create/', data, format='json')
        created_user = Users.objects.get(email='admin@example.com')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(created_user.is_moderator)
    
    def test_create_customer(self):
        data = {
            'email': 'customer@example.com',
            'password': 'customerpassword',
            'is_moderator': False 
        }

        response = self.client.post('/create/', data, format='json')
        created_user = Users.objects.get(email='customer@example.com')

        self.assertEqual(response.status_code, 200)
        self.assertFalse(created_user.is_moderator)


class ApplicationsModelTest(TestCase):
    def test_create_application(self):
        customer = Users.objects.create_user(
            email="customer@example.com",
            password="password123"
        )
        application = Applications.objects.create(
            status=1,
            created_at=timezone.now(),
            customer=customer
        )
        self.assertEqual(application.status, 1 )
        self.assertEqual(application.customer.email, "customer@example.com")

