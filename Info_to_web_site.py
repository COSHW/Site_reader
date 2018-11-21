from flask import Flask, render_template
import pandas
import psycopg2
from Info_v3 import Info
import json


class Site (Info):
    def __init__(self):
        self.columns = ["Источник", "Заголовок", "Время", "Ссылка"]
        # Информация из датабазы

        self.conn = psycopg2.connect("dbname='site_info' user='postgres' password='Lovunod2302' host='localhost' port='5432'")
        self.cur = self.conn.cursor()
        self.cur.execute("select * from news")
        self.all_info = self.cur.fetchall()


         #Информация сразу с сайта
        
        super(Site, self).__init__(self.all_info)


        self.from_json = json.load(open("News.json"))
        print(self.from_json)
        self.df = pandas.DataFrame(self.all_info)
        self.df.columns = self.columns
        self.app = Flask(__name__)

        @self.app.route("/")
        def index():
            return render_template("index.html")

        @self.app.route('/success', methods=['POST'])
        def success():
            return render_template("index2.html", text=self.df.to_html(index=False))

        self.app.run()


site_start = Site()


























