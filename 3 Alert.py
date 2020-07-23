from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.runoob.com/try/try.php?filename=tryjs_alert')

browser.switch_to.frame('iframeResult')
browser.find_element_by_xpath('/html/body/input').click()

info = browser.switch_to.alert.text
print(info)

browser.switch_to.alert.accept()
# browser.switch_to.alert.dismiss()
browser.switch_to.default_content()

browser.quit()


