import os
from dotenv import load_dotenv
import requests

# Загружаем переменные окружения из файла .env
load_dotenv()
login_username = os.getenv("LOGIN_USERNAME")
login_password = os.getenv("LOGIN_PASSWORD")
login = os.getenv("LOGIN")
https_proxy = os.getenv("HTTPS_PROXY")

session = requests.Session()
url = 'https://rutracker.org/forum/login.php'
data = {
	'login_username': login_username,
	'login_password': login_password,
	'login': login
}
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
proxies = {
	'https': https_proxy
}
r = session.post(url, data=data, headers=headers, proxies=proxies)

url = 'https://rutracker.org/forum/tracker.php?f=635'
r = session.get(url, proxies=proxies)#, data=data, headers=headers, proxies=proxies)
print(r.text)
# УСПЕХ!
