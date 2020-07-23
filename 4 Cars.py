from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.runoob.com/try/try.php?filename=tryhtml_select2')

browser.switch_to.frame('iframeResult')
select_element = browser.find_element_by_name('cars')
Select(select_element).select_by_index(3)

Select(select_element).select_by_value('saab')

Select(select_element).select_by_visible_text('Fiat')


is_selected = select_element.is_selected()
if is_selected == False:
    select_element.click()

browser.switch_to.default_content()

browser.quit()