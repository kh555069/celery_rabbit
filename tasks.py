from worker import app
import requests
from bs4 import BeautifulSoup

@app.task
def crawler():
    home_url = 'https://www.ptt.cc'
    url = 'https://www.ptt.cc/bbs/forsale/index.html'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    items=[]
    for ele in soup.select('.r-ent'):
        data={}
        data['title'] = ele.select('.title')[0].text
        data['url'] = home_url + ele.select('.title a')[0]['href']
        article.delay(data)

@app.task
def article(data):
    item_res = requests.get( data['url'] )
    item_soup = BeautifulSoup(item_res.text, 'lxml')
    data['content'] = item_soup.select('#main-content')[0].text.strip()
    print( data['title'] )
    print( data['url'] )
