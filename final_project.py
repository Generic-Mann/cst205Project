from flask import Flask, render_template, flash, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from urllib.request import urlopen
from bs4 import BeautifulSoup

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from datetime import datetime
from color import use


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

Links = None

def webscrape(web):
#     Beautiful Soup
# web scraps a website given by the user and displays
# the images and text of the page.
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
@app.route('/',methods=('GET', 'POST'))
def index():
    images = []
    texts = []
    if request.method == 'POST':
        if request.form.get('user_link') is None:
            return redirect(url_for('/'))
        images, texts = webscrape(request.form.get('user_link'))

        return render_template('soup.html', images=images, texts=texts)
    return render_template('landing_page.html')


# @app.route('/colorblind_value_converter', methods=('GET', 'POST'))
# def cvc():
#     images = []
#     texts = []
#     if request.method == 'POST':
#         if request.form.get('user_link') is None:
#             return redirect(url_for('colorblind_value_converter'))
#         images, texts = webscrape(request.form.get('user_link'))

#         return render_template('soup.html', images=images, texts=texts)
#     return render_template('colorblind_value_converter.html')


# Beautiful Soup
# web scraps a website given by the user and displays
# the images and text of the page.
@app.route('/soup', methods=('GET', 'POST'))
def so():
    if request.method == 'POST':
        if request.form.get('user_link') is None:
            return redirect(url_for('soup'))
        use()
        
        

    return render_template('soup.html', images=images, texts=texts)


# Course: CST205 - Multimedia Design & Programming
# Roles:
# Michael Garcia: Beautiful Soup
# Christopher Morales: Colorblind Filter
# Valeria Arteaga-Higueros: design
# Oscar Aviles-Saldana: Landing Page & UI

