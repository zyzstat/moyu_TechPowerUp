import urllib.request
from bs4 import BeautifulSoup
import sys


def handle_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_text(href):
    request = handle_request(href)
    content = urllib.request.urlopen(request).read().decode("utf8")
    soup = BeautifulSoup(content, "lxml")
    titlediv = soup.find_all("a", class_="newslink")
    contdiv = soup.find_all("div", class_="text p")
    with open("./tpu_txt.txt", "w") as writer:
        writer.write("------------------TechPowerUp!!!-----------------\n\n\n\n\n\n\n\n")
        for cont, cont_01 in zip(titlediv, contdiv):
            title = cont.text
            content = cont_01.text
            content = content.replace("Read Review", "")
            content = content.replace("Read full story", "")
            writer.write("------------------Title-----------------\n")
            writer.write(title.strip("\n").strip())
            writer.write("\n----------------------------------------\n")
            writer.write("\n")
            writer.write("-----------------Content----------------\n")
            writer.write(content.strip("\n").strip())
            writer.write("\n----------------------------------------\n")
            writer.write("\n\n\n")


get_text("http://techpowerup.com")
fufu = """
^ↀᴥↀ^
"""
print("All recent techpowerup data get, Miao~\n{}".format(fufu))

