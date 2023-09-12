from django.test import TestCase
from main.models import Product

# Create your tests here.
class TestProduct(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_product_list(self):
        product = Product.objects.create(
            name='Test Product',
            amount=10,
            description='Test Description',
            price=100
        )
        product.save()
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, 'Test Product')
        self.assertEqual(Product.objects.first().amount, 10)
        self.assertEqual(Product.objects.first().description, 'Test Description')
        self.assertEqual(Product.objects.first().price, 100)

    def test_product_model(self):
        product = Product.objects.create(
            name='Test Product',
            amount=10,
            description='Test Description',
            price=100
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.price, 100)
        self.assertEqual(str(product), 'Test Product')

