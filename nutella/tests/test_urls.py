from django.test import Client, SimpleTestCase
from django.urls import resolve, reverse
from nutella import views


class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_legal_notice_url_is_resolved(self):
        url = reverse('legal_notice')
        self.assertEqual(resolve(url).func, views.legal_notice)
