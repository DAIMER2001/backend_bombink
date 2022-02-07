
from django.test import TestCase
from products.models import HistorySearchProduct, Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name = "CAMISA Y JEAN",
            description = "MARCA",
            price = 200000,
            discount = 22,)

        self.history = HistorySearchProduct.objects.create(
            id_product_id= self.product.id,
            count_search = 1,
        )


    def test_products(self):
        camisa = Product.objects.get(name="CAMISA Y JEAN")
        self.assertEqual(camisa.name, "CAMISA Y JEAN")
        self.assertEqual(self.product.description, "MARCA")

    def test_history(self):
        self.assertEqual(self.history.count_search, 1)
