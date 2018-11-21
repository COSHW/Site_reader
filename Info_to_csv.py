import pandas


def to_csv(all_info):
    df = pandas.DataFrame(all_info)
    df.to_csv("News.csv", index_label="Номер", encoding="utf-16")
