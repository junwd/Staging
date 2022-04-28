from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()
driver.get("https://www.huya.com/l")
# submit = driver.find_element_by_class_name("tag-layer--zQ1ICWrOJt1ycRxlLT9oM")
# submit.click()
i = 1
while True:
    element = driver.find_element_by_xpath('//div[@class="laypage_main laypageskin_default"]/a')
    driver.execute_script("arguments[0].scrollIntoView(false);", element)
    list = driver.find_elements_by_xpath('//div[@class="box-bd"]/ul/li')
    for r in list:
        m = r.text.split('\n')
        # print(m)
        name = m[-3:]
        commit = m[-1]
        L = [name[0], commit]
        print(L)
        with open("huya.csv", 'a', newline="", encoding="utf_8") as f:
            writer = csv.writer(f)
            L = [name[0], commit]
            writer.writerow(L)
    print("第%d页成功" % i)
    i += 1
    time.sleep(2)
    element = driver.find_element_by_xpath('//div[@class="laypage_main laypageskin_default"]/a')
    driver.execute_script("arguments[0].scrollIntoView(false);", element)
    time.sleep(3)
    if driver.page_source.find("laypage_next") != -1:
        a = driver.find_element_by_class_name("laypage_next")
        time.sleep(1)
        a.click()
        time.sleep(3)
    else:
        print("结束")
        break
