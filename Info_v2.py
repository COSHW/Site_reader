import requests
from bs4 import BeautifulSoup


class Info(object):
    def __init__(self, all_info=1):
        self.all_info = all_info
        self.all_info = []

        self.req = requests.get("http://prokazan.ru/news/")
        self.cont = self.req.content
        self.soup = BeautifulSoup(self.cont, "html.parser")
        self.news = self.soup.find_all("div", {"id": "RedColumn"})
        self.info1 = self.news[0].find_all("div", {"class": "news-mid__content"})

        self.time = self.news[0].find_all("div", {"class": "news-mid__date"})
        j = 0
        for item in self.info1:
            link50 = []
            title = []
            d = dict()
            d["Источник"] = "ProKazan"
            for a in item.find_all('a', title=True):
                title = a['title']
            d["Заголовок"] = title
            time = self.time[j].text.replace("\n", "")
            d["Время"] = time
            for a in self.info1[j].find_all('a', href=True):
                link50.append("http://prokazan.ru" + a['href'])
            d["Ссылка"] = link50[0]
            self.all_info.append(d)
            j += 1

        #print(self.all_info)


if __name__ == "__main__":
    start = Info()
