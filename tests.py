import unittest
from links import *

class linkTests(unittest.TestCase):
    def test_resolve_http_redirect(self):
        resolvedLink = resolve_http_redirect('https://www.google.com/url?q=https://dannyrosen.net/&sa=D&source=hangouts&ust=1540391076667000&usg=AFQjCNGeaYYefTHzvwHHV2C0Vtzw0U-NaQ')
        self.assertEqual(resolvedLink, 'https://dannyrosen.net/')

if __name__ == '__main__':
    unittest.main()
