from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_site='https://csumb.edu/'
site_html=urlopen(my_site)
soup = BeautifulSoup(site_html.read(), 'lxml')

app = Flask(__name__)
bootstrap = Bootstrap5(app)

images = soup.findAll('img')
paragraphs = soup.findAll('p')
texts = ' '.join(p.get_text() for p in paragraphs)


@app.route('/', methods=('GET', 'POST'))
def index():

    return render_template('soup.html', images=images, texts=texts)

    