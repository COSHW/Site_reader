import pandas


def to_json(all_info):
    print(all_info)
    df = pandas.DataFrame(all_info)
    df.to_json("News.json")#, force_ascii=False)
