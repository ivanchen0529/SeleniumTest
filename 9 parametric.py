'''
ddt Data-Driven Tests 数据驱动测试
@ddt 装饰测试类，继承自TestCase的类
@data() 装饰测试方法
    @data(a,b)
    @data([a,d],[c,d])
@unpack 解包

步骤:
1.导入ddt
2.引用ddt装饰类
3.加载测试数据
'''
from selenium import webdriver
import time
import unittest
import ddt  # 1

@ddt.ddt    # 2
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.2.117')

    def tearDown(self):
        self.browser.quit()

    # 登录
    def login(self, username, password):
        self.browser.find_element_by_link_text('登录').click()
        time.sleep(1)
        self.browser.find_element_by_id('user_name').send_keys(username)
        self.browser.find_element_by_id('user_password').send_keys(password)
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[4]/div/button[1]').click()

    # 退出
    def logout(self):
        self.browser.find_element_by_link_text('退出')

    # 加载测试数据
    @ddt.data(['ivan','123456'],['','123456'],['ivanchen',''],['lawliet','123456'])
    @ddt.unpack
    def test_login_success(self, username, password):
        # 异常处理
        try:
            self.login(username, password)
            time.sleep(1)
            self.assertTrue(self.browser.find_element_by_link_text('退出'))
            self.logout()
        except:
            if username == '':
                print("用户名不能为空")
            elif password == '':
                print("密码不能为空")

if __name__ == '__main__':
    unittest.main()











