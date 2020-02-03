#Author:fanzzhenzhen
#-*-coding:utf-8-*-
import requests
from lxml import etree
import os

def main():
    if not os.path.exists("./ppt_img"):
        os.mkdir("./ppt_img")
    new_url = "http://www.ypppt.com/moban/list-%d.html"
    url = "http://www.ypppt.com/moban"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    for i in range(2,11):
        if i == 1:
            url = url
        else:
            url = format(new_url%i)
        r = requests.get(url=url,headers=header,timeout=30)
        r.encoding = r.apparent_encoding
        page_text = r.text
        tree = etree.HTML(page_text)
        a_list = tree.xpath("//ul[@class='posts clear']/li")
        for li in a_list:
            ppt_img_src = "http://www.ypppt.com"+li.xpath("./a/img/@src")[0]
            ppt_img_name = li.xpath("./a[2]/text()")[0]+".jpg"
            ppt_data = requests.get(url=ppt_img_src,headers=header,timeout=30).content
            ppt_path = "ppt_img/"+ppt_img_name
            with open(ppt_path, "wb") as fp :
                fp.write(ppt_data)
            print(ppt_img_name,"爬取成功")
    print("over!!!")

if __name__ == "__main__":
    main()