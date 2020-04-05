import time
import unittest
from framework.browser_engine import BrowserEngine

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        browse=BrowserEngine(self)
        self.driver=browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.',format(e))

if __name__=='__main__':
    unittest.main()