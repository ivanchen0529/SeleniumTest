from selenium import webdriver
import time
import unittest
import ddt

@ddt.ddt
class TestLogin(unittest.TestCase):
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
        self.browser.find_element_by_link_text('退出')

    @ddt.data(['ivan','123456'],['ivan1234','123456'],['ivan','987654'],['ivan',''],['','123456'])
    @ddt.unpack
    def test_login_success(self, username, password):
        try:
            self.login(username, password)
            time.sleep(2)
            self.assertTrue(self.browser.find_element_by_link_text('退出'))
            self.logout()
        except Exception as err:
            print(err)

if __name__ == '__main__':
    unittest.main()












