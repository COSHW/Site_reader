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
            d = list()
            d.append("ProKazan")
            for a in item.find_all('a', title=True):
                title = a['title']
            d.append(title)
            time = self.time[j].text.replace("\n", "")
            d.append(time)
            for a in self.info1[j].find_all('a', href=True):
                link50.append("http://prokazan.ru" + a['href'])
            d.append(link50[0]+"\n")
            self.all_info.append(d)
            j += 1

        print(self.all_info)


if __name__ == "__main__":
    start = Info()
