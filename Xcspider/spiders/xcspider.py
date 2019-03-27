# -*- coding: utf-8 -*-
import scrapy
from Xcspider.items import xiciItem

class XcspiderSpider(scrapy.Spider):
    name = 'xcspider'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        item_1 = response.xpath("//tr[@class='odd']")
        item_2 = response.xpath("//tr[@class='']")
        items = item_1+item_2


        for item in items:
            # print(item)
            #获取国家图片链接
            countries = item.xpath("./td[@class='country']/img/@src").extract()
            # print(countries)
            if countries != []:
                country = countries[0]
            else:
                country = '未知'
            #获取ipaddress

            ipaddress = item.xpath("./td[2]/text()").extract()
            try:
                ipaddress = ipaddress[0]
            except:
                ipaddress = '未知'
            # print(ipaddress)
            port = item.xpath("./td[3]/text()").extract()
            try:
                port = port[0]
            except:
                port = '未知'
            serveraddr = item.xpath("./td[4]/text()").extract()
            try:
                serveraddr = serveraddr[0]
            except:
                serveraddr = '未知'
            isanonymous = item.xpath("./td[5]/text()").extract()
            try:
                isanonymous = isanonymous[0]
            except:
                isanonymous = '未知'
            type = item.xpath("./td[6]/text()").extract()
            try:
                type = type[0]
            except:
                type = '未知'
            alivetime = item.xpath("./td[7]/text()").extract()
            try:
                alivetime = alivetime[0]
            except:
                alivetime = '未知'
            verifictiontime = item.xpath("./td[8]/text()").extract()
            try:
                verifictiontime = verifictiontime[0]
            except:
                verifictiontime = '未知'
            # print(port,serveraddr,isanonymous,type,alivetime,verifictiontime)

            infos = xiciItem()

            infos["country"] = country
            infos["ipaddress"] = ipaddress
            infos["port"] = port
            infos["serveraddr"] = serveraddr
            infos["isanonymous"] = isanonymous
            infos["type"] = type
            infos["alivetime"] = alivetime
            infos["verifictiontime"] = verifictiontime

            print(infos)
            yield infos
