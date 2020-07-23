'''
强制等待 sleep(等待时间s)
显式等待 直到元素出现才开始操作，如果等待超时，则抛出异常。
         需要导入WebDriverWait类
         WebDriverWait(浏览器驱动，最大等待时间，监测时间间隔)
         一般与until  until_not 结合使用
隐式等待 implicitly_wait(最大等待时间s)

异常 NoSuchElementException 没有此元素
     TimeoutException 超时异常
'''

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 隐式等待
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.implicitly_wait(5)
# browser.get('http://baidu.com')
# browser.find_element_by_id('kw').send_keys('selenium')
# browser.quit()

# 显示等待
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://baidu.com')
WebDriverWait(browser, 5, 1).until(EC.presence_of_element_located((By.ID, 'kw')))
browser.quit()

