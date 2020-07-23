from selenium import webdriver
import unittest
import time
import ddt

@ddt.ddt
class TestRegister(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.2.117')

    def tearDown(self):
        self.browser.quit()

    def register(self, username, password, password2, email):
        self.browser.find_element_by_link_text('注册').click()
        self.browser.find_element_by_id('user_name').send_keys(username)
        self.browser.find_element_by_id('user_password').send_keys(password)
        self.browser.find_element_by_id('user_com_passwd').send_keys(password2)
        self.browser.find_element_by_id('user_email').send_keys(email)
        self.browser.find_element_by_id('agreement').click()
        self.browser.find_element_by_xpath('//*[@id="user_register_form"]/div[6]/div/button').click()

    def logout(self):
        self.browser.find_element_by_link_text('退出').click()

    @ddt.data(['','123456','123456','321456@qq.com'],
              ['1111111111111111111111111111111111111111111111111111111','123456','123456','312456@qq.com'],
              ['law','1','123456','123456','032497@qq.com'],
              ['laylie','123456','654321','223456@qq.com'],
              ['laey','123456','123456','123456@qq.com'],
              ['ivan','123456','123456','43924@qq.com'])
    @ddt.unpack
    def test_register_success(self, username, password, password2, email):
        try:
            self.register(username,password,password2,email)
            time.sleep(2)
            self.assertTrue(self.browser.find_element_by_link_text('退出'))
            self.logout()
        except Exception as err:
            print(err)

if __name__ == '__main__':
    unittest.main()
