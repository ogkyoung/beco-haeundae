import urllib.request
import re

try:
    req = urllib.request.Request("https://www.beco.or.kr/kor/CMS/Main/Main.do", headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"][^>]*alt=[\'"][^\'"]*로고[^\'"]*[\'"]', html)
    if matches:
        print("FOUND:", matches[0])
    else:
        imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+logo[^\'"]+)[\'"]', html, re.IGNORECASE)
        print("LOGOS:", imgs)
except Exception as e:
    print("Error:", e)
