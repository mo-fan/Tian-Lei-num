#Author:fanzzhenzhen
import requests
from lxml import etree
# from bs4 import BeautifulSoup
import random
def main():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

    all_ids_list = []
    url = "http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=10&time=1&pro=&city=&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=15"
    r = requests.get(url=url, headers=header)
    r.encoding = r.apparent_encoding
    page_text = r.text
    tree = etree.HTML(page_text)
    body_list = tree.xpath("//body//text()")
    for id in body_list:
        dic = {"https": id}
        all_ids_list.append(dic)

    url = "https://www.63xs.com/book/161/161082/"
    page_text = requests.get(url = url,headers = header,timeout = 30).text
    tree = etree.HTML(page_text)
    dd_list = tree.xpath("//*[@id='list']/dl")
    with open("sanshengqing.txt", "w", encoding="utf-8")as fp:
        for dd in dd_list[1:]:
            title = dd.xpath("./a/text()")[0]
            detail_url ="https://www.63xs.com"+ dd.xpath("./a/@href")[0]
            detail__text = requests.get(detail_url,headers = header,proxies=random.choice(all_ids_list),timeout = 30).text
            tree = etree.HTML(detail__text)
            detail = tree.xpath("//*[@id='wrapper']/div[5]/div/div[3]/text()")

            fp.write(title+":"+detail+"\n")
            print(dd,"爬取成功")
    print(dd_list)
if __name__ == "__main__":
    main()