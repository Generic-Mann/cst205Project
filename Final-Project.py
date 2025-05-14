from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_site='https://csumb.edu/'
site_html=urlopen(my_site)
soup = BeautifulSoup(site_html.read(), 'lxml')

app = Flask(__name__)
bootstrap = Bootstrap5(app)

raw_images = [img['src'] for img in soup.find_all('img') if img.get('src')]
images = [src if src.startswith('http') else my_site + src for src in raw_images]

for link in soup.find_all('img'):
    print(link.get('src'))

texts = [p.get_text(strip=True) for p in soup.find_all('p')]

@app.route('/', methods=('GET', 'POST'))
def index():

    return render_template('soup.html', images=images, texts=texts)