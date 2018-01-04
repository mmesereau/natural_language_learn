import urllib3
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer

def getAllDoxyDonkeyPosts(url, links):
    http = urllib3.PoolManager()
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'html5lib')
    for a in soup.findAll('a'):
        try:
            url = a['href']
            title = a['title']
            if title == "Older Posts":
                links.append(url)
                getAllDoxyDonkeyPosts(url, links)
        except:
            title = ""
    return

def getDoxyDonkeyText(testUrl):
    http = urllib3.PoolManager()
    page = http.request('GET', testUrl)
    soup = BeautifulSoup(page.data, 'html5lib')
    mydivs = soup.findAll("div", {"class": 'post-body'})

    posts = []
    for div in mydivs:
        post = ' '.join(map(lambda p: p.text.encode('ascii', errors='replace').replace(b"?", b" ").decode('utf-8'), div.findAll("li")))
        posts.append(post)
    return posts


blogUrl = "http://doxydonkey.blogspot.in"
links = []
posts = []

getAllDoxyDonkeyPosts(blogUrl, links)
for i in links:
    posts.append(getDoxyDonkeyText(i))
vectorizer = TfidfVectorizer(max_df = 0.5, min_df = 2, stop_words = 'english')

X = vectorizer.fit_transform(posts)
print(X)
