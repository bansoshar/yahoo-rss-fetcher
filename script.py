from requests_html import HTMLSession
import datetime

session = HTMLSession()
url = "https://search.yahoo.co.jp/realtime/search?p=中央線"
r = session.get(url)
r.html.render(timeout=30)

posts = r.html.find(".sw-Card__title")
print(f"=== {datetime.datetime.now()} の検索結果 ===")
for p in posts[:5]:
    print("-", p.text)
