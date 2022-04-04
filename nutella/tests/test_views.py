from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse
from nutella import views


class TestViews(TestCase):
    
    fixtures = ['fixture_category.json',
                'fixture_product.json',
                'fixture_user.json']
    
    def setUp(self):
        self.client = Client()
    
    def test_index_view_redirects_to_nutella(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/nutella/', status_code=301, target_status_code=200)

    def test_index_view_renders_proper_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'nutella/index.html')

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = views.index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Pur Beurre</title>', html)
        self.assertTrue(html.endswith('</html>'))
        
    def test_product_view_uses_proper_url(self):
        response = self.client.get(reverse('product', args=[1]))
        self.assertEqual(response.status_code,200)
        
    def test_product_view_renders_proper_template(self):
        response = self.client.get(reverse('product', args=[1]))
        self.assertTemplateUsed(response, 'nutella/product.html')
        
    def test_legal_notice_view_uses_proper_url(self):
        response = self.client.get(reverse('legal_notice'))
        self.assertEqual(response.status_code, 200)
        
    def test_legal_notice_view_renders_proper_template(self):
        response = self.client.get(reverse('legal_notice'))
        self.assertTemplateUsed(response, 'nutella/legal_notice.html')

    # def test_product_search_view_uses_proper_url(self):
    #     response = self.client.get(reverse('product_search'))
    #     self.assertEqual(response.status_code,200)
    