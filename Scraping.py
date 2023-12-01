import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

for count in range(1, 5):

    sleep(3)
    url = f"https://itorrents-igruha.org/newgames/page/{count}/"

    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, "lxml")

    container = soup.select_one("div.articles")

    products = container.find_all("div", class_="article-film")

    urls = []
    for product in products:
        url1 = product.select_one("div a")["href"]
        if url1 != "https://itorrents-igruha.org/8456-vazhnaya-informaciya.html":
            urls.append(url1)

    args = []
    for url2 in urls:
        response = requests.get(url2)
        html = response.text
        soup = BeautifulSoup(html, "lxml")

        name = soup.select_one("h1").text

        size = soup.find("div", style="padding-left: 215px;").text
        size_2 = size.split()
        size_3 = 0
        if 'диске:' in size_2:
            size_3 = size_2[size_2.index('диске:') + 1] + size_2[size_2.index('диске:') + 2]

        if 'активация,' in size_2:
            repack_or_activation = 'Активация'
        else:
            repack_or_activation = 'Репак'

        views = int(soup.find("div", id="article-film-full-info").select("span")[-1].text)

        likes = soup.select_one("a.orating_res").text
        likes_2 = int(likes[1:]) if '+' in likes else int(likes)

        # args.append((name, views, likes_2, size_3, repack_or_activation))
        args.append((name, views, likes_2, size_3, repack_or_activation))

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO games VALUES(?,?,?,?,?)", args)
    conn.commit()
    conn.close()
