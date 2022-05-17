from selenium import webdriver
import time
import csv

driver = webdriver.PhantomJS()
driver.get("http://www.jd.com")
# product = input("请你输入要搜索的内容:")
id = driver.find_element_by_id("key")
id.send_keys("电脑")
submit = driver.find_element_by_class_name("button")
submit.click()
time.sleep(3)
# driver.save_screenshot("京东.png")
js = "window.scrollTo(0,document.body.scrollHeight)"  # 脚本
driver.execute_script(js)
time.sleep(2)

r_list = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li//i')[1]
# r_list1 = driver.find_elements_by_xpath('//div[@class="p-name"]/em')
# r_list2 = driver.find_elements_by_xpath('//div[@class="p-commit"]/strong')
# r_list3 = driver.find_elements_by_xpath('//div[@class="p-shop"]/span/a')


for r in r_list:
    m = r.text
    print(m)
# with open("ass.csv", 'a', newline="", encoding="utf_8") as f:
#     writer = csv.writer(f)
#     writer.writerow(r_list)
