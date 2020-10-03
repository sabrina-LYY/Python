import os

from selenium import webdriver
import time
driver = webdriver.Chrome()
#file_path = 'file:///'+os.path.abspath("G:/qqfile/selenium2html/checkbox.html")
#driver.get(file_path)
#driver.maximize_window()
#inputs = driver.find_elements_by_tag_name("input")
#time.sleep(3)
#for input in inputs:
#    if input.get_attribute('type') == "checkbox":
#        input.click()

#多层框架，先找f1页面再到f2
file_path = 'file:///'+os.path.abspath("G:/qqfile/selenium2html/frame.html")
driver.get(file_path)
driver.maximize_window()
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("汪苏泷")
driver.find_element_by_id("su").click()

#点击f1页面的click要先跳转到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()


#层级定位，让java展示框高亮

time.sleep(3)
driver.quit()