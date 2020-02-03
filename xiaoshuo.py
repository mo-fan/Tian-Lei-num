#Author:fanzzhenzhen
import requests
from bs4 import BeautifulSoup
global false, null, true
false = null = true = ''
def main():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    url = "https://book.qidian.com/ajax/book/category?_csrfToken=LTIaCE8SlTguV1OKyaJciio1fMVCdGkYGtlY93A9&bookId=1010191960"
    page_text = requests.get(url = url,headers = header,timeout = 30)
    page_text.encoding = page_text.apparent_encoding
    page_dic_text = eval(page_text.text)
    dic = page_dic_text["data"]["vs"]
    fp = open("dawang.txt","w",encoding="utf-8")
    for i in range(200,210):
        title = dic[1]["cs"][i]["cN"]#1为收费内容，
        new_url = "https://read.qidian.com/chapter/"+dic[1]["cs"][i]["cU"]
        content = requests.get(new_url,headers = header,timeout=30).text
        detail_soup = BeautifulSoup(content, "lxml")
        detail_list = detail_soup.find("div", class_="read-content j_readContent")
        content = detail_list.text
        fp.write(title + ":" + content + "\n")
        print(title, "爬取成功")



    #mu_list = page_dic_text["date"]

    # soup = BeautifulSoup(page_text,"lxml")
    # soup_list= soup.select(".book-mulu > ul > li")
    # fp = open("xiyouji.txt", "w", encoding="utf-8")
    # for li in soup_list:
    #     title = li.a.string
    #     detail_url ="http://www.shicimingju.com"+ li.a["href"]
    #     detail_name_text = requests.get(detail_url,headers = header,timeout = 30).text
    #     detail_soup = BeautifulSoup(detail_name_text,"lxml")
    #     detail_list = detail_soup.find("div",class_ = "chapter_content" )
    #     content = detail_list.text
    #     fp.write(title+":"+content+"\n")
    #     print(title,"爬取成功")


if __name__ == "__main__":
    main()