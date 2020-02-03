#Author:fanzzhenzhen
#-*-coding:utf-8-*-
import requests
from lxml import etree
import os

def main():
    if not os.path.exists("./pictures"):
        os.mkdir("./pictures")
    url = "http://pic.netbian.com/4kdongman/index_%d.html"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    for i in range(0,6):
        new_url = format(url%i)
        r = requests.get(url=new_url,headers=header)
        r.encoding = r.apparent_encoding
        page_text = r.text
        tree = etree.HTML(page_text)
        li_list = tree.xpath("//div[@class='slist']//li")
        for li in li_list:
            pic_src = "http://pic.netbian.com"+li.xpath("./a/img/@src")[0]
            img_name = li.xpath("./a/img/@alt")[0]+".jpg"
            img_data = requests.get(url=pic_src,headers= header).content
            img_path = "pictures/"+img_name
            with open(img_path, "wb") as fp :
                fp.write(img_data)
            print(img_name,"爬取成功")
    print("over!!!")
if __name__ == "__main__":
    main()