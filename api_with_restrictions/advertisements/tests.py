from unittest import TestCase
from rest_framework.test import APIClient
# from advertisements.views import AdvertisementViewSet


class TestView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def _require_login(self):
        self.client.login(username='testuser', password='1')

    def test_view_401(self):
        url = 'http://194.58.97.187/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_view_200(self):
        # self.client._require_login()
        client = APIClient()
        request = self.client.get('http://194.58.97.187/api/')
        view = views.AdvertisementViewSet.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
