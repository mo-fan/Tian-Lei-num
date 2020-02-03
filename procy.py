#Author:fanzzhenzhen
import requests
from lxml import etree

def main():
    all_ids_list = []
    url = "http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=2&time=1&pro=%E5%AE%81%E5%A4%8F%E5%9B%9E%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA&city=&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=15"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    page_text = r.text
    tree = etree.HTML(page_text)
    body_list = tree.xpath("//body//text()")
    for id in body_list:
        dic = {"https":id}
        all_ids_list.append(dic)
    print(all_ids_list)
    #






if __name__ == "__main__":
    main()