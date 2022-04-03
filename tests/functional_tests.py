import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_title_should_be_pur_beurre(self):
        self.browser.get('http://localhost:8000/nutella/')
        self.assertEqual(self.browser.title, "Pur Beurre")
        
if __name__ == '__main__':
    unittest.main()

