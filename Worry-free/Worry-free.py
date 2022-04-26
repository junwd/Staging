from selenium import webdriver
import time
import csv

Search = input("请你输入要搜索的：")
Begin = webdriver.Chrome()
Begin.get("https://www.51job.com")

text = Begin.find_element_by_id("kwdselectid")
text.send_keys(Search)
i = 1
button = Begin.find_element_by_xpath('//div[@class="ush top_wrap"]/button')
button.click()
time.sleep(3)
while True:
    js1 = 'window.scrollTo(0,document.body.scrollHeight)'
    Begin.execute_script(js1)
    time.sleep(3)
    content = Begin.find_elements_by_xpath('//div[@class="j_joblist"]/div')
    # content = Begin.find_elements_by_xpath('//div[@class="j_joblist"]//span | //div[@class="er"]/a')
    # //div[@class="j_joblist"]/div

    for con in content:
        need = con.text.split('\n')
        # print(need)
        name = need[0]
        conni = need[2]
        mit = need[3]
        dein = need[-3]
        L = [name, conni, mit[16:], dein]
        print(L)
        with open("job.csv", 'a', newline="", encoding="utf_8") as f:
            writer = csv.writer(f)
            L = [name, conni, mit[16:], dein]
            writer.writerow(L)
    print("第%d页成功" % i)
    i += 1
    js = 'window.scrollTo(0,document.body.scrollTop=0)'
    Begin.execute_script(js)
    if Begin.page_source.find("e_icons") != -1:
        a = Begin.find_element_by_class_name("next")

        a.click()
        time.sleep(3)
    else:
        print("结束")
        break
