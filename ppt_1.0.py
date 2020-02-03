#Author:fanzzhenzhen
#-*-coding:utf-8-*-
import requests
from lxml import etree
import os
import random


def main():
    #创建文件夹
    if not os.path.exists("./ppt_muban"):
        os.mkdir("./ppt_muban")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}    #代理池
    all_ids_list = []
    url = "http://ip.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=10&time=1&pro=%E5%86%85%E8%92%99%E5%8F%A4%E8%87%AA%E6%B2%BB%E5%8C%BA&city=&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=15"
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    page_text = r.text
    tree = etree.HTML(page_text)
    body_list = tree.xpath("//body//text()")
    for id in body_list:
        dic = {"http": id}
        all_ids_list.append(dic)

    new_url = "http://www.ypppt.com/moban/list-%d.html"
    url = "http://www.ypppt.com/moban"
    for i in range(2, 51):
        if i == 1:
            url = url
        else:
            url = format(new_url % i)
        r = requests.get(url=url,headers=headers,proxies=random.choice(all_ids_list),timeout=30)
        r.encoding = r.apparent_encoding
        page_text = r.text
        tree = etree.HTML(page_text)
        a_list = tree.xpath("//ul[@class='posts clear']/li")
        for li in a_list:
            ppt_href = "http://www.ypppt.com"+li.xpath("./a[2]/@href")[0]
            ppt_name = li.xpath("./a[2]/text()")[0]+".rar"
            ppt_text = requests.get(url=ppt_href,headers= headers,timeout=30).text
            tree = etree.HTML(ppt_text)
            download_url= "http://www.ypppt.com"+tree.xpath("//div[@class = 'infos']/div/div[2]/a/@href")[0]

            download_text = requests.get(url = download_url,headers=headers,timeout=30).text
            tree = etree.HTML(download_text)
            download = tree.xpath("//div[@class='wrapper']/div/ul/li/a/@href")[0]
            if len(download) <40:#判断网址长度是否大于40
                new_download = "http://www.ypppt.com"+tree.xpath("//div[@class='wrapper']/div/ul/li/a/@href")[0]
            else:
                new_download = tree.xpath("//div[@class='wrapper']/div/ul/li/a/@href")[0]

            ppt_data = requests.get(url=new_download,headers=headers).content
            ppt_path = "ppt_muban/"+ppt_name
            with open(ppt_path, "wb") as fp :
                fp.write(ppt_data)
            print(ppt_name,"爬取成功")
            # print(new_download)
    print("over!!!")

if __name__ == "__main__":
    main()

