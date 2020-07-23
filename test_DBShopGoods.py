from selenium import webdriver
import unittest
import time
import ddt

@ddt.ddt
class TestGoods(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.2.117')

    def tearDown(self):
        self.browser.quit()

    def login(self):
        self.browser.find_element_by_link_text('登录').click()
        self.browser.find_element_by_id('user_name').send_keys('ivan')
        self.browser.find_element_by_id('user_password').send_keys('123456')
        self.browser.find_element_by_xpath('//*[@id="login_form"]/div[4]/div/button[1]').click()
        time.sleep(1)

    def search(self, name):
        self.browser.find_element_by_xpath('//*[@id="shop_top_search"]/form/div/input').send_keys(name)
        self.browser.find_element_by_xpath('//*[@id="shop_top_search"]/form/div/button').click()
        time.sleep(1)
        self.browser.find_element_by_class_name('thumbnail').click()
        time.sleep(1)

    def change(self, num):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[num])
        self.browser.find_element_by_id('add_cart_submit').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="message_url"]/a[2]').click()
        time.sleep(1)

    def goods(self, name1, name2):
        self.login()
        self.search(name1)
        self.change(1)
        self.search(name2)
        self.change(2)
        self.browser.find_element_by_xpath('//*[@id="goods_cart"]/div/table/tbody/tr[4]/td/span/input[2]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="cart_step"]/form/div/div[3]/div/input[2]').click()
        self.browser.find_element_by_xpath('//*[@id="cart_step"]/form/div/div[14]/div/input[2]').click()

    @ddt.data(['40','上衣'],['40','null'])
    @ddt.unpack
    def test_goods_success(self, name1, name2):
        try:
            self.goods(name1, name2)
            time.sleep(2)
            self.assertTrue(self.browser.find_element_by_xpath('//*[@id="dbshop-body"]/div[5]/div/div/input[2]'))
        except Exception as err:
            print(err)

if __name__ == '__main__':
    unittest.main()


