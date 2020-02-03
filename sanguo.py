#Author:fanzzhenzhen
import requests
from bs4 import BeautifulSoup

def main():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    url = "http://www.shicimingju.com/book/xiyouji.html"
    page_text = requests.get(url = url,headers = header,timeout = 30).text
    soup = BeautifulSoup(page_text,"lxml")
    soup_list= soup.select(".book-mulu > ul > li")
    with open("xiyouji.txt", "w", encoding="utf-8")as fp:
        for li in soup_list:
            title = li.a.string
            detail_url ="http://www.shicimingju.com"+ li.a["href"]
            detail_name_text = requests.get(detail_url,headers = header,timeout = 30).text
            detail_soup = BeautifulSoup(detail_name_text,"lxml")
            detail_list = detail_soup.find("div",class_ = "chapter_content" )
            content = detail_list.text
            fp.write(title+":"+content+"\n")
            print(title,"爬取成功")

if __name__ == "__main__":
    main()