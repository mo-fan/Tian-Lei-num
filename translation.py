#Author:fanzzhenzhen
import requests
import json
def main():
    post_url = "https://fanyi.baidu.com/sug"
    word = input("enter a word:")
    data = {"kw":word}
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    r = requests.post(url=post_url,data= data,headers=header)
    r.encoding = r.apparent_encoding
    dic_obj = r.json()
    print(r.status_code)
    print(dic_obj)
    file_name = word + ".json"
    fp= open(file_name,"w",encoding="utf-8")
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print("已翻译")


if __name__ == "__main__":
    main()