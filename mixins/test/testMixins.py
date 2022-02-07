from django.test import TestCase
from mixins.models import ListType, ListItem

class ListTypeTestCase(TestCase):
    def setUp(self):
        self.ListType = ListType.objects.create(
            code = 1,
            name = "PAIS",
            description = "PAISES ADMITIDOS",)
        self.ListItem = ListItem.objects.create(
            list_type_id = self.ListType.id,
            code = 1,
            name = "COLOMBIA",
            description = "PAIS CON MUCHOS PAISAJES",)
    def test_create_list_type(self):
        self.assertEqual(self.ListType.name, "PAIS")
        self.assertEqual(self.ListType.description, "PAISES ADMITIDOS")
        self.assertEqual(self.ListType.code, 1)
    def test_create_list_item(self):
        self.assertEqual(self.ListItem.name, "COLOMBIA")
        self.assertEqual(self.ListItem.description, "PAIS CON MUCHOS PAISAJES")
        self.assertEqual(self.ListItem.code, 1)
