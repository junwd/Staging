from selenium import webdriver
import time
import csv

product = input("请你输入要搜索的：")
driver = webdriver.PhantomJS()
driver.get("https://www.jd.com/")

text = driver.find_element_by_class_name("text")
text.send_keys(product)
i = 1

button = driver.find_element_by_class_name("button")
button.click()

while True:
    js1 = 'window.scrollTo(0,document.body.scrollHeight)'
    driver.execute_script(js1)
    time.sleep(2)
    r_list = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
    for r in r_list:
        r1 = r.text.split('\n')
        # print(r1)
        if r1[1] == "京品电脑":
            price = r1[0]
            names = r1[2]
            commit = r1[3]
            market = r1[4]
        elif "￥" in r1[1]:
            pass
        else:
            price = r1[0]
            names = r1[1]
            commit = r1[2]
            market = r1[3]
        with open("jd.csv", 'a', newline="", encoding="utf_8") as f:
            writer = csv.writer(f)
            L = [names.strip(), price.strip(), commit.strip(), market.strip()]
            writer.writerow(L)
    print("第%d页成功" % i)
    i += 1
    js = 'window.scrollTo(0,document.body.scrollTop=0)'
    driver.execute_script(js)
    if driver.page_source.find("pn-next disabled") == -1:
        a = driver.find_element_by_class_name("pn-next")
        a.click()
    else:
        print("结束")
        break
    # with open("ass.csv", 'a', newline="", encoding="utf_8") as f:
    #     writer = csv.writer(f)
    #     L=[price,names,market]
    #     writer.writerow(L)