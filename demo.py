import requests
url="https://www.baidu.com/"
re = requests.get(url)
print re.headers["Content-Type"]
