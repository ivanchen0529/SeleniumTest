from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.runoob.com/html/html-basic.html')
browser.find_element_by_xpath('//*[@id="content"]/div[3]/a').click()
# time.sleep(1)

'''
浏览器打开2个窗口，有2个控制句柄handles
handles的值是列表，handles[0]代表第1个窗口 handles[1]代表第2个窗口
'''
# 切换页面步骤
# 1.获取句柄
handles = browser.window_handles
# 2.选择网页
browser.switch_to.window(handles[1])
# time.sleep(1)

# 切换frame
browser.switch_to.frame('iframeResult')
browser.find_element_by_link_text('这是一个链接使用了 href 属性').click()
# time.sleep(1)

# 切换回父页面
browser.switch_to.default_content()

browser.quit()
