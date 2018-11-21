import psycopg2


def psql_record(all_info):
    conn = psycopg2.connect("dbname='site_info' user='postgres' password='Lovunod2302' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS news")
    cur.execute("CREATE TABLE IF NOT EXISTS news (Номер SERIAL PRIMARY KEY, Источник text, Заголовок text, Время text, Ссылка text)")
    conn.commit()
    for item in all_info:
        cur.execute("INSERT INTO news (Источник, Заголовок, Время, Ссылка) VALUES (%s, %s, %s, %s)", (item['Источник'], item['Заголовок'], item['Время'], item['Ссылка']))
        conn.commit()
