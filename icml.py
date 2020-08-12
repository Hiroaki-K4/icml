import requests
from bs4 import BeautifulSoup
from selenium import webdriver



def main(first):
    if first == True:
        headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        for i in range(5000, 10000):
            url_name = "https://icml.cc/virtual/2020/poster/6695".format(i)
            url = requests.get(url_name, headers)
            soup = BeautifulSoup(url.content, "html.parser")
            title = soup.find("h2", class_="card-title").get_text()
            if len(title) == 1:
                continue
            else:
                title = title.strip()
                driver = webdriver.Chrome('/home/hiroaki-k4/Downloads/chromedriver_linux64/chromedriver')
                driver.get(url_name)
                driver.find_element_by_class_name('card-link').click()
        
    else:
        print('no')






if __name__ == '__main__':
    first = True
    main(first)
