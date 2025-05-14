from flask import Flask, render_template, flash, redirect, request
from flask_bootstrap import Bootstrap5
from urllib.request import urlopen
from bs4 import BeautifulSoup



my_site='https://csumb.edu/'
site_html=urlopen(my_site)
soup = BeautifulSoup(site_html.read(), 'lxml')

app = Flask(__name__)
bootstrap = Bootstrap5(app)
# web scraping
raw_images = [img['src'] for img in soup.find_all('img') if img.get('src')]
images = [src if src.startswith('http') else my_site + src for src in raw_images]

for link in soup.find_all('img'):
    print(link.get('src'))

texts = [p.get_text(strip=True) for p in soup.find_all('p')]
print(texts)
# routes 
@app.route('/')
def index():

    return render_template('landing_page.html')

@app.route('/text_to_speech.html', methods=['GET', 'POST'])
def tts():
    my_site = request.form.get('user_input')
    return render_template('text_to_speech.html', user_input=my_site)


@app.route('/colorblind_value_converter.html')
def cvc():

    return render_template('Colorblind_value_converter.html')

@app.route('/soup', methods=('GET', 'POST'))
def so():

    return render_template('soup.html', images=images, texts=texts)
