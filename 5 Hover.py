from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://baidu.com')

# 定位到悬浮框
mouse_over = browser.find_element_by_name('tj_briicon')
# 将鼠标移动到悬浮框更多
ActionChains(browser).move_to_element(mouse_over).perform()
browser.find_element_by_xpath('//*[@id="s-top-more"]/div[2]/a[4]/div').click()
time.sleep(2)

browser.quit()



