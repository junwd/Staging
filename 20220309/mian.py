#练习1:
html="""
<div class="animal">
     <p class="name">
      <a title="Tiger"></a>
      </p>
      <p class="contents">
      Two tiger two tigers run fast
      </p>
</div>
<div class="animal">
     <p class="name">
      <a title="Rabbit"></a>
      </p>
      <p class="contents">
      small white rabbit white and white
      </p>
</div>"""

#匹配打印出来
# [("Tigers","Two tiger ..."),
#  ("Rabbit","small rabbit ...")]

#打印输出:
#动物名称:Tiger
#动物描述:Two tiger ...

import re
p= re.compile('<div class="animal">.*?<a title="(.*?)">.*?<p class="contents">\n      (.*?)\n      </p>',re.S)
r_list= p.findall(html)
for name in r_list:
    print("动物名称:",name[0])
    print("动物属性:", name[1])
