'''
python3提供unittest测试框架

步骤：
1.导入模块unittest;
2.创建一个测试类，继承TestCase;
3.定义setUp和tearDown方法
setUp是测试前的初始化工作；
tearDown是测试后的清除工作。
4.创建测试用例，测试用例需要以test开头；
每个测试用例的目的和内容都要非常明确。
5.调用unittest.main()方法，启动脚本。

断言
assertTrue(x，[msg])： 断言x是否True，是True则测试用例通过。bool(x)
assertFalse(x，[msg])： 断言x是否False，是False则测试用例通过。
assertIn(a,b，[msg])： 断言a是否在b中，在b中则测试用例通过。
assertNotIn(a,b，[msg])： 断言a是否在b中，不在b中则测试用例通过。
assertEqual(a,b，[msg])： 断言a和b是否相等，相等则测试用例通过。
assertNotEqual(a,b，[msg])： 断言a和b是否相等，不相等则测试用例通过。
msg='测试失败时打印的信息',默认为none.

'''

from selenium import webdriver
import time
import unittest  # 1

class Login(unittest.TestCase):  # 2
    def setUp(self):             # 3
        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.2.117')

    def tearDown(self):          # 3
        self.browser.quit()

    def test_login(self):        # 4
        self.browser.find_element_by_link_text('登录').click()
        time.sleep(2)
        self.browser.find_element_by_id('user_name').send_keys('ivan')
        self.browser.find_element_by_id('user_password').send_keys('123456')
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/div[4]/div/button[1]').click()
        time.sleep(2)
        # 断言
        self.assertTrue(self.browser.find_element_by_link_text('退出'))
        welcome = self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[7]')
        self.assertIn('欢迎您',welcome.text)
        self.assertEqual('欢迎您ivan退出', welcome.text)

if __name__ == '__main__':       # 5
    unittest.main()
