from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from KPI.models import KPI

class KPIModelTest(TestCase):
    def setUp(self):
        self.kpi = KPI.objects.create(name="Test KPI", expression="ATTR+10")

    def test_kpi_creation(self):
        self.assertEqual(self.kpi.name, "Test KPI")
        self.assertEqual(self.kpi.expression, "ATTR+10")

class KPIViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.kpi = KPI.objects.create(name="Test KPI", expression="ATTR+10")

    def test_create_kpi(self):
        response = self.client.post('/api/kpi/', {'name': 'New KPI', 'expression': 'ATTR*5'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_kpis(self):
        response = self.client.get('/api/kpi/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_link_asset_to_kpi(self):
        response = self.client.post(f'/api/kpi/{self.kpi.id}/link_asset/', {'asset_id': '123', 'value': '25'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['asset_id'], '123')
        self.assertEqual(response.data['kpi'], self.kpi.id)


class KPIAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.kpi_data = {"name": "Test KPI", "expression": "ATTR + 10"}
        self.kpi = KPI.objects.create(**self.kpi_data)

    def test_create_kpi(self):
        response = self.client.post('/api/kpi/', self.kpi_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.kpi_data['name'])

    def test_list_kpis(self):
        response = self.client.get('/api/kpi/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_link_asset_to_kpi(self):
        response = self.client.post(f'/api/kpi/{self.kpi.id}/link_asset/', {"asset_id": "123", "value": "15"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['asset_id'], "123")
        self.assertEqual(response.data['kpi'], self.kpi.id)
