from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from off.models import Favorite


class TestNutellaStandardViews(TestCase):
    
    fixtures = [
        'fixture_category.json',
        'fixture_product.json',
        'fixture_favorite.json',
        'fixture_user.json'
    ]
    
    def setUp(self):
        self.client = Client()
    
    def test_index_view_redirects_to_nutella(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/nutella/', status_code=301, target_status_code=200)

    def test_index_view_renders_proper_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'nutella/index.html')

    def test_product_view_response(self):
        response = self.client.get(reverse('product', args=[1]))
        self.assertEqual(response.status_code,200)
        
    def test_product_view_renders_proper_template(self):
        response = self.client.get(reverse('product', args=[1]))
        self.assertTemplateUsed(response, 'nutella/product.html')

    def test_product_search_response(self):
        response = self.client.get(reverse('product_search'), {
            "home_search": "pizza"})
        self.assertEqual(response.status_code, 200)

    def test_product_search_renders_proper_template(self):
        response = self.client.get(reverse('product_search'), {
            "home_search": "pizza"})
        self.assertTemplateUsed(response, 'nutella/product_search.html')

    def test_search_replacement_view_response(self):
        response = self.client.get(reverse('product_replacement', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_search_replacement_view_renders_proper_template(self):
        response = self.client.get(reverse('product_replacement', args=[1]))
        self.assertTemplateUsed(response, 'nutella/product_replacement.html')

    def test_legal_notice_view_response(self):
        response = self.client.get(reverse('legal_notice'))
        self.assertEqual(response.status_code,200)
        
    def test_legal_notice_view_renders_proper_template(self):
        response = self.client.get(reverse('legal_notice'))
        self.assertTemplateUsed(response, 'nutella/legal_notice.html')
        
class TestSaveFavoriteView(TestCase):

    fixtures = [
        'fixture_category.json',
        'fixture_product.json'
    ]
    
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='john', password='lennon')
        cls.kwargs = {'pk_replaced':1, 'pk_replacing':2}
        cls.url = 'save_favorite'
    
    def setUp(self):
        self.client.login(username = 'john', password='lennon')
    
    def test_response_with_no_user_logged(self):
        self.client.logout()
        response = self.client.get(reverse(self.url, kwargs=self.kwargs))
        self.assertTrue(response.status_code, 200)
    
    def test_redirects_properly_with_no_user_logged(self):
        self.client.logout()
        response = self.client.post(reverse(self.url, kwargs=self.kwargs))
        expected = "/accounts/login/?next=/nutella/save_favorite/1/2/"
        self.assertRedirects(response, expected, status_code=302, target_status_code=200)

    def test_response_with_user_logged(self):
        url = reverse(self.url, kwargs=self.kwargs)
        response = self.client.get(url, HTTP_REFERER = 'index')
        expected ="/nutella/"
        self.assertRedirects(response, expected, status_code=302, target_status_code=200)
        
    def test_add_favorite_with_user_logged(self):
        url = reverse(self.url, kwargs=self.kwargs)
        self.client.get(url, HTTP_REFERER = 'index')
        self.assertEqual(Favorite.objects.count(),1)

class TestDeleteFavoriteView(TestCase):
    
    fixtures = [
        'fixture_category.json',
        'fixture_product.json',
        'fixture_favorite.json',
        'fixture_user.json'
    ]
    
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='john', password='lennon')
        cls.url = 'delete_favorite'
    
    def setUp(self):
        self.client.login(username = 'john', password='lennon')
        
    def test_response_with_no_user_logged(self):
        self.client.logout()
        response = self.client.post(reverse(self.url, args=[1]))
        self.assertTrue(response.status_code, 200)
                   
    def test_redirects_properly_with_no_user_logged(self):
        self.client.logout()
        response = self.client.post(reverse(self.url, args=[1]))
        expected = "/accounts/login/?next=/nutella/delete_favorite/1/"
        self.assertRedirects(response, expected, status_code=302, target_status_code=200)
    
    def test_response_with_user_logged(self):
        url = reverse(self.url, args=[1])
        response = self.client.get(url, HTTP_REFERER = 'index')
        expected ="/nutella/"
        self.assertRedirects(response, expected, status_code=302, target_status_code=200)
    
    def test_delete_favorite_with_user_logged(self):
        url = reverse(self.url, args=[1])
        self.client.get(url, HTTP_REFERER='index')
        self.assertEqual(Favorite.objects.count(), 0)

class TestProductUserView(TestCase):
    
    fixtures = [
    'fixture_category.json',
    'fixture_product.json',
    ]
    
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(username='john', password='lennon')
        cls.url = 'product_user'
    
    def setUp(self):
        self.client.login(username = 'john', password='lennon')

    def test_response_with_no_user_logged(self):
        self.client.logout()
        response = self.client.post(reverse(self.url, args=[1]))
        self.assertTrue(response.status_code, 200)
                   
    def test_redirects_properly_with_no_user_logged(self):
        self.client.logout()
        response = self.client.post(reverse(self.url, args=[1]))
        expected = "/accounts/login/?next=/nutella/product_user/1/"
        self.assertRedirects(response, expected, status_code=302, target_status_code=200)
    
    def test_response_with_user_logged(self):
        url = reverse(self.url, args=[1])
        response = self.client.get(url)
        self.assertTrue(response.status_code, 200)
    
    def test_view_renders_proper_template(self):
        url = reverse(self.url, args=[1])
        response=self.client.get(url)
        self.assertTemplateUsed(response, 'nutella/product_user.html')
        