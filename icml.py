import requests
from bs4 import BeautifulSoup








def main(first):
    if first == True:
        for i in range(5000, 7000):
            url_name = "https://icml.cc/Conferences/2020/Schedule?showEvent={}".format(i)
            print(url_name)
            input()
        url_name = 'https://icml.cc/Conferences/2020/Schedule?type=Poster'
        headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        url = requests.get(url_name, headers)
        soup = BeautifulSoup(url.content, "html.parser")
        elems = soup.find_all("div", class_="maincardBody")
        print(elems)
        input()
    else:
        print('no')






if __name__ == '__main__':
    first = True
    main(first)
