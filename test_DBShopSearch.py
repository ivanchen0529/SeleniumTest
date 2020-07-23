from selenium import webdriver
import unittest
import time
import ddt

@ddt.ddt
class TestSearch(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.2.117')

    def tearDown(self):
        self.browser.quit()

    def search(self, goods):
        self.browser.find_element_by_xpath('//*[@id="shop_top_search"]/form/div/input').send_keys(goods)
        self.browser.find_element_by_xpath('//*[@id="shop_top_search"]/form/div/button').click()
        time.sleep(1)

    def clear(self):
        self.browser.find_element_by_xpath('//*[@id="shop_top_search"]/form/div/input').clear()

    @ddt.data('HUAWEI P40', '变形剑刚')
    def test_search_success(self, goods):
        try:
            self.search(goods)
            time.sleep(2)
            self.assertTrue(self.browser.find_element_by_class_name('goods_price'))
            self.clear()
            time.sleep(2)
        except Exception as err:
            print(err)

if __name__ == '__main__':
    unittest.main()
