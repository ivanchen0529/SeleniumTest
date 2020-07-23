from selenium import webdriver
import unittest
import time
import ddt

@ddt.ddt
class TestPay(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.2.117')

    def tearDown(self):
        self.browser.quit()

    def pay(self, method):
        self.browser.find_element_by_link_text('登录').click()
        self.browser.find_element_by_id('user_name').send_keys('ivan')
        self.browser.find_element_by_id('user_password').send_keys('123456')
        self.browser.find_element_by_xpath('//*[@id="login_form"]/div[4]/div/button[1]').click()
        self.browser.find_element_by_xpath('//*[@id="shop_top_search"]/form/div/input').send_keys('40')
        self.browser.find_element_by_xpath('//*[@id="shop_top_search"]/form/div/button').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="right_goods_list"]/ul/li/p[1]/a').click()
        time.sleep(2)
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[1])
        self.browser.find_element_by_id('add_cart_submit').click()
        time.sleep((1))
        self.browser.find_element_by_xpath('//*[@id="message_url"]/a[2]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="goods_cart"]/div/table/tbody/tr[3]/td/span/input[2]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="cart_step"]/form/div/div[3]/div/input[2]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="cart_step"]/form/div/div[11]/label['+method+']/input').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="cart_step"]/form/div/div[14]/div/input[2]').click()

    def logout(self):
        self.browser.find_element_by_link_text('退出').click()

    @ddt.data('1','2','3')
    def test_pay_success(self, method):
        try:
            self.pay(method)
            time.sleep(2)
            self.assertTrue(self.browser.find_element_by_xpath('//*[@id="dbshop-body"]/div[5]/div/div/input[2]'))
            self.logout()
        except Exception as err:
            print(err)

if __name__ == '__main__':
    unittest.main()
