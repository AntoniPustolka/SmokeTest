import unittest
from selenium import webdriver

class MojPrzypadekTestow(unittest.TestCase):

    def setUp(self):
        print("przygotowanie do testu")
        self.driver=webdriver.Firefox()

    def testSelenium(self):
        print('Test')

    def tearDown(self):
        print('Sprzatanie po tescie!')

if __name__ == '__main__':
    unittest.main(verbosity=2)



