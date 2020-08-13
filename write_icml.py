import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm
from googletrans import Translator
translator = Translator()


def main():
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }
    paper_all_list = []
    for i in tqdm(range(5000, 10000)):
        url_name = "https://icml.cc/virtual/2020/poster/{}".format(i)
        url = requests.get(url_name, headers)
        soup = BeautifulSoup(url.content, "html.parser")
        title = soup.find("h2", class_="card-title").get_text()
        if len(title) == 1:
            continue
        else:
            title = title.strip()
            pdf_link = soup.find_all("a", class_="card-link")
            pdf_link = pdf_link[1].attrs['href']
            driver = webdriver.Chrome('/home/hiroaki-k4/Downloads/chromedriver_linux64/chromedriver')
            driver.get(url_name)
            driver.find_element_by_class_name('card-link').click()
            abstract = driver.find_element_by_id('abstractExample').get_attribute("textContent")
            abstract = abstract.replace('\n' , '')
            abstract = abstract.strip()
            abstract_ja = translator.translate(abstract, src='en', dest='ja')
            abstract_ja = str(abstract_ja.text)
            abstract_ja = abstract_ja.strip()
            paper_list = [title, pdf_link, abstract, abstract_ja]
            paper_all_list.append(paper_list)
            driver.quit()

    with open('/home/hiroaki-k4/icml.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(paper_all_list)


if __name__ == '__main__':
    main()
