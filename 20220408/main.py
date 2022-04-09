from selenium import webdriver
bdriver=webdriver.Chrome()
# bdriver.grt("https://baidu.com/")
bdriver.get("http://baidu.com/")
# bdriver.save_screenshot("ss.jpg")


# from selenium import webdriver
# import time
# bdriver=webdriver.Chrome()
# bdriver.get("https://baidu.com/")
# kw=bdriver.find_element_by_id("kw")
# kw.send_keys("mein")
# su=bdriver.find_element_by_id("su")
# su.click()
# time.sleep(6)
# bdriver.save_screenshot("ssa.jpg")

# from selenium import webdriver
# import time
#
# bdriver = webdriver.Chrome()
# bdriver.get("https://www.jd.com/")
# kw = bdriver.find_element_by_class_name("text")
# name=input("请输入要搜索的：")
#
# kw.send_keys(name)
# su = bdriver.find_element_by_class_name("iconfont")
# su.click()
# time.sleep(6)
# bdriver.save_screenshot("ssa.jpg")
