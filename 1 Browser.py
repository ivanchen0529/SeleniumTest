from selenium import webdriver
import time

# 打开浏览器，最大化浏览器
browser = webdriver.Chrome()
browser.maximize_window()

# 1.访问百度首页
browser.get('http://baidu.com')
time.sleep(2)

# 2.定位搜索栏，输入Selenium
# browser.find_element_by_id('kw').send_keys('selenium')
# browser.find_element_by_class_name('s_ipt').send_keys('selenium')
# browser.find_element_by_name('wd').send_keys('selenium')

# 2.定位关键字，点击新闻
browser.find_element_by_link_text('新闻').click()
time.sleep(2)
# browser.find_element_by_partial_link_text('新').click()
# time.sleep(2)
# 3.清除输入内容
# browser.find_element_by_id('kw').clear()
# time.sleep(1)

# 切换页面
handles = browser.window_handles
browser.switch_to.window(handles[1])
# 屏幕快照
browser.save_screenshot('.//baidu.png')
time.sleep(1)
# browser.find_element_by_id('kw').send_keys('python')
# 4.点击百度一下
# browser.find_element_by_id('su').click()
# time.sleep(3)

browser.quit()