from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Products

class ProductAPITestCase(TestCase):
    """
    Test module for Products API.
    """
    def setUp(self):
        self.client = APIClient()
        self.product_data = {"name": "Test Product", "description": "Test Description", "price": 10.00, "stock": 100}
        self.product = Products.objects.create(**self.product_data)

    def test_update_product(self):
        """
        Ensure we can update an existing product object.
        """
        updated_data = {"name": "Updated Product", "description": "Updated Description", "price": 30.00, "stock": 150}
        response = self.client.put(f'/api/products/{self.product.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Products.objects.count(), 1)
        self.assertEqual(Products.objects.get().name, updated_data['name'])

    def test_delete_product(self):
        """
        Ensure we can delete an existing product object.
        """
        response = self.client.post('/api/products/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Products.objects.count(), 2)
        
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Products.objects.count(), 1)
        
        