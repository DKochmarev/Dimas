import sqlite3
import requests
from bs4 import BeautifulSoup
from time import sleep
import os

def create_database():
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS games 
                 (name TEXT, views INTEGER, likes INTEGER, size TEXT, repack_or_activation TEXT)''')
    conn.commit()
    conn.close()

def connect_to_database():
    if os.path.exists('games.db'):
        os.remove('games.db')
    create_database()
    conn = sqlite3.connect('games.db')
    c = conn.cursor()
    return conn, c


def get_urls(page):
    url = f"https://itorrents-igruha.org/newgames/page/{page}/"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    container = soup.select_one("div.articles")
    products = container.find_all("div", class_="article-film")

    urls = [product.select_one("div a")["href"] for product in products if product.select_one("div a")["href"] != "https://itorrents-igruha.org/8456-vazhnaya-informaciya.html"]
    return urls

def get_game_info(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")

    name = soup.select_one("h1").text

    size = soup.find("div", style="padding-left: 215px;").text
    size_2 = size.split()
    size_3 = size_2[size_2.index('диске:') + 1] + size_2[size_2.index('диске:') + 2] if 'диске:' in size_2 else 0

    repack_or_activation = 'Активация' if 'активация,' in size_2 else 'Репак'

    views = int(soup.find("div", id="article-film-full-info").select("span")[-1].text)
    likes = int(soup.select_one("a.orating_res").text[1:]) if '+' in soup.select_one("a.orating_res").text else int(soup.select_one("a.orating_res").text)

    return (name, views, likes, size_3, repack_or_activation)

def insert_data(conn, c, data):
    c.executemany('INSERT INTO games VALUES (?,?,?,?,?)', data)
    conn.commit()

def main():
    conn, c = connect_to_database()

    for count in range(1, 3):
        sleep(3)
        urls = get_urls(count)
        args = [get_game_info(url) for url in urls]
        insert_data(conn, c, args)

    conn.close()

if __name__ == "__main__":
    main()