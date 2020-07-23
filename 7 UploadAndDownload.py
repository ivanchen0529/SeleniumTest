from selenium import webdriver
import time

# 文件上传
# browser = webdriver.Firefox()
# browser.maximize_window()
# browser.get('http://www.sahitest.com/demo/php/fileUpload.htm')
#
# upload = browser.find_element_by_id('file')
# upload.send_keys('C:\\Users\\a\\Pictures\\Saved Pictures\\2.ico')
# time.sleep(3)
# print(upload.get_attribute('value'))

# 文件下载
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # 1默认路径 2自定义
profile.set_preference('browser.download.dir', 'E:\\') # 指定文件下载目录
profile.set_preference('browser.download.manager.showWhenStarting', False) # 是否显示下载器
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip') # 无需弹窗提醒 文件格式为zip

browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://sahitest.com/demo/saveAs.htm')
browser.find_element_by_xpath('/html/body/a[1]').click()

browser.quit()