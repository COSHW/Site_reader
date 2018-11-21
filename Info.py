import requests
from bs4 import BeautifulSoup
import re


class Info(object):
    def __init__(self, all_info):
        self.all_info = all_info
        self.all_info = []
        self.d_new = {}

        # Сбор информации с сайта

        self.req = requests.get("http://prokazan.ru/")
        self.cont = self.req.content
        self.soup = BeautifulSoup(self.cont, "html.parser")

        self.new = self.soup.find_all("div", {"class": "news-big"})
        self.new_title = self.new[0].find("a", {"class": "TvLink"}).text.replace("\n", "")
        try:
            self.new_time = self.new[0].find("b").text
        except Exception:
            self.new_time = "Время не указано"

        self.new_link = []
        self.same = "Заголовок"
        for link in self.new[0].find_all('a', attrs={'href': re.compile("^/news/")}):
            self.new_link.append(link.get('href'))
        self.new_link = "http://prokazan.ru" + self.new_link[0]
        self.d_new["Источник"] = "ProKazan"
        self.d_new[self.same] = self.new_title
        self.d_new["Время"] = self.new_time
        self.d_new["Ссылка"] = self.new_link

        self.req = requests.get("http://prokazan.ru/")
        self.cont = self.req.content
        self.soup = BeautifulSoup(self.cont, "html.parser")
        self.news = self.soup.find_all("div", {"class": "column-mid"})
        for item in self.news:

            link45 = []
            d = {}
            d["Источник"] = "ProKazan"
            d[self.same] = item.find_all("a", {"class": "caption"})[0].text.replace("\n", "")
            try:
                d["Время"] = item.find_all("b")[0].text
            except Exception:
                d["Время"] = "Время не указано"

            for link in item.find_all('a', attrs={'href': re.compile("^/news/")}):
                link1 = link.get('href')
                link45.append("http://prokazan.ru" + link1)
            if link45 == []:
                for link123 in item.find_all('a', attrs={'href': re.compile("^/auto/")}):
                    link1 = link123.get('href')
                    link45.append("http://prokazan.ru" + link1)
            if link45 == []:
                for link123 in item.find_all('a', attrs={'href': re.compile("^/adverting/")}):
                    link1 = link123.get('href')
                    link45.append("http://prokazan.ru" + link1)
            if link45 == []:
                for link123 in item.find_all('a', attrs={'href': re.compile("^http:/")}):
                    link1 = link123.get('href')
                    link45.append(link1)
            d["Ссылка"] = link45[0]

            self.all_info.append(d)
        self.all_info.insert(0, self.d_new)
        print(self.all_info)


if __name__ == "__main__":
    start = Info(1)
