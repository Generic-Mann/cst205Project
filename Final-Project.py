from flask import Flask, render_template, flash, redirect, request
from flask_bootstrap import Bootstrap5
from urllib.request import urlopen
from bs4 import BeautifulSoup

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

Links = None
images = None
texts = None

def webscrape(web):
    my_site=str(web)
    site_html=urlopen(my_site)
    soup = BeautifulSoup(site_html.read(), 'lxml')
    # web scraping
    raw_images = [img['src'] for img in soup.find_all('img') if img.get('src')]
    images = [src if src.startswith('http') else my_site + src for src in raw_images]

    for link in soup.find_all('img'):
        print(link.get('src'))

    texts = [p.get_text(strip=True) for p in soup.find_all('p')]
    print(texts)

    return images, texts






# routes 
@app.route('/')
def index():

    return render_template('landing_page.html')

@app.route('/text_to_speech.html', methods=('GET', 'POST'))
def tts():
    return render_template('text_to_speech.html', )


@app.route('/colorblind_value_converter.html')
def cvc():

    return render_template('Colorblind_value_converter.html')

@app.route('/soup', methods=('GET', 'POST'))
def so():

    return render_template('soup.html', images=images, texts=texts)

