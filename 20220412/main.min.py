# 实例1获取HTML
# from selenium import webdriver
# import time
# bdriver = webdriver.Chrome()
# bdriver.get("https://www.baidu.com/")
# print(bdriver.page_source)

# 实例2，打印查找文字
# from selenium import webdriver
# import time
# bdriver = webdriver.PhantomJS()
# bdriver.get("https://www.baidu.com/")
# kw = bdriver.find_element_by_id("s-top-left")
# print(kw.text)

# 实例登录
# from selenium import webdriver
# import time
#
# bdriver = webdriver.Chrome()
# bdriver.get("https://cas.qnzy.net/lyuapServer/login")
# bdriver.save_screenshot("yzm.png")
# yzm2 = input("yzm:")
# name = bdriver.find_element_by_id("username")
# name.send_keys("202003170536")
# password = bdriver.find_element_by_id("password")
# password.send_keys("qwe2561216155")
# yzm = bdriver.find_element_by_id("captcha")
# yzm.send_keys(yzm2)
# submit = bdriver.find_element_by_class_name("btn-submit")
# submit.click()
