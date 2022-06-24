        url1 = response.xpath('//li/a').re('shtml.*>(.*?)<\/a>$')
        print(url1)
        # yield scrapy.Request(url1)
        # url1 = response.css('h1.')