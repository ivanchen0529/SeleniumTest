from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import unittest

class TestShopping(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.2.117')

    def tearDown(self):
        self.browser.quit()

    def login(self, username, password):
        self.browser.find_element_by_link_text('登录').click()
        self.browser.find_element_by_id('user_name').send_keys(username)
        self.browser.find_element_by_id('user_password').send_keys(password)
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[4]/div/button[1]').click()

    def logout(self):
        self.browser.find_element_by_link_text('退出').click()

    def test_shopping_success(self):
        self.login('ivan', '123456')
        time.sleep(1)
        self.assertIn('DBShop电子商务系统', self.browser.title)
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/div/ul/li[2]/h5/a').click()
        self.browser.find_element_by_css_selector('a[title="苹果"]').click()
        self.browser.find_element_by_id('add_cart_submit').click()
        time.sleep(2)
        self.browser.find_element_by_link_text('去购物车结算').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr[3]/td/span/input[2]').click()
        time.sleep(2)
        # 点击下一步进入结算页面
        self.browser.find_element_by_xpath('/html/body/div[5]/form/div/div[3]/div/input[2]').click()
        # 获取商品清单的商品货号
        table = self.browser.find_element_by_xpath('/html/body/div[5]/form/div/div[8]/table')
        table_rows = table.find_elements_by_tag_name('tr')
        row2_Col2 = table_rows[1].find_elements_by_tag_name('td')[1].text
        print('第二行第二列文本内容:'+row2_Col2)
        self.assertEqual('DBS000025', row2_Col2)
        time.sleep(5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
