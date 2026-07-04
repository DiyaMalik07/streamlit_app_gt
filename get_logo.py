import urllib.request
import re

try:
    req = urllib.request.Request("https://en.wikipedia.org/wiki/Goa_Engineering_College", headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode("utf-8")
    matches = re.findall(r'<img[^>]+src="([^"]+)"', html)
    for m in matches:
        if "logo" in m.lower() or "goa_engineering_college" in m.lower():
            if m.startswith("//"):
                m = "https:" + m
            print(m)
            break
except Exception as e:
    print(e)
