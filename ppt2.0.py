#Author:fanzzhenzhen
#-*-coding:utf-8-*-
# 爬取ppt文件的模板并保存到txt文件当中
import requests
from lxml import etree
import os

header = {"Connection":"close","User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}

def get_html(url):

    r = requests.get(url=url, headers=header, timeout=30)
    r.encoding = r.apparent_encoding
    page_text = r.text
    return page_text


def parse_html(page_text,name_list,href_list):
    tree = etree.HTML(page_text)
    a_list = tree.xpath("//ul[@class='posts clear']/li")
    for li in a_list:
        ppt_href = "http://www.ypppt.com" + li.xpath("./a[2]/@href")[0]
        ppt_name = li.xpath("./a[2]/text()")[0] + ".rar"
        name_list.append(ppt_name)
        href_list.append(ppt_href)
    print(name_list)
    print(href_list)

def parse_download(href_list,download_url_list):
    for i in href_list:
        ppt_text = requests.get(url=i, headers=header, timeout=30).text
        tree = etree.HTML(ppt_text)
        download_url = "http://www.ypppt.com" + tree.xpath("//div[@class = 'infos']/div/div[2]/a/@href")[0]
        download_url_list.append(download_url)
    print(download_url_list)

def parse_download_data(download_url_list,down_url_list):
    for d in download_url_list:
        download_text = requests.get(url=d, headers=header, timeout=30).text
        tree = etree.HTML(download_text)
        download = "http://www.ypppt.com" + tree.xpath("//div[@class='wrapper']/div/ul/li/a/@href")[0]
        down_url_list.append(download)
    print(down_url_list)
        # return download
        #down_url_list.append(download)
    #print(down_url_list)
def ppt_down(down_url_list):
    for ppt in down_url_list:
        ppt_data = requests.get(url=ppt, headers=header).content
        # ppt_data_list.append(ppt_data)
        #ppt_data_list.append(ppt_data)
        # print(ppt_data_list)
        # for i in name_list:
        ppt_path = "ppt_muban/" + "name"
        #     # for a in ppt_data_list:
        #     #     ppt = a.text
        with open(ppt_path, "wb") as fp:
            fp.write(ppt_data)
            print( "爬取成功")

def main():
    name_list = []
    href_list = []
    #ppt_data_list= []
    download_url_list = []
    down_url_list = []
    if not os.path.exists("./ppt_muban"):
        os.mkdir("./ppt_muban")
    #url = "http://www.ypppt.com/moban/list-%d.html"
    url = "http://www.ypppt.com/moban"
    # for i in range(2,4):
    #     new_url = format(url%i)
    page_text = get_html(url)
    parse_html(page_text,name_list,href_list)
    parse_download(href_list,download_url_list)
    parse_download_data(download_url_list,down_url_list)
    ppt_down(down_url_list)
    #ppt_down(down_url_list,ppt_data_list)
    #save_ppt(name_list,ppt_data)
    # print(download)

    print("over!!!")

if __name__ == "__main__":
    main()