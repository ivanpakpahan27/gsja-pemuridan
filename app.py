from re import template
from flask import Flask, url_for, render_template, jsonify, request, Blueprint, redirect
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
import os

app = Flask(__name__)
########################################################################################
# Beranda
@app.route('/', methods=['GET', 'POST'])

def index():
    file_carousel = []
    directory = 'static/images/carousel/'
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            file_carousel.append(f)
            
    return render_template('beranda.html', carousel=file_carousel, title='beranda')
########################################################################################
# Pengakuan Iman
@app.route('/pengakuan_iman', methods=['GET', 'POST'])

def pengakuan_iman():        
    return render_template('pengakuan_iman.html', title='pengakuan_iman')
########################################################################################
# Struktur Organisasi
@app.route('/struktur_organisasi', methods=['GET', 'POST'])

def struktur_organisasi():        
    return render_template('struktur_organisasi.html', title='struktur_organisasi')
########################################################################################
# Sejarah Gereja
@app.route('/sejarah_gereja', methods=['GET', 'POST'])

def sejarah_gereja():        
    return render_template('sejarah_gereja.html', title='sejarah_gereja')
########################################################################################
# Blog
@app.route('/blog', methods=['GET', 'POST'])

def blog():        
    return render_template('blog.html', title='blog')
########################################################################################
# Kegiatan
@app.route('/kegiatan', methods=['GET', 'POST'])

def kegiatan():        
    return render_template('kegiatan.html', title='kegiatan')
########################################################################################
# Galeri
@app.route('/galeri', methods=['GET', 'POST'])

def galeri():        
    return render_template('galeri.html', title='galeri')
########################################################################################
# Download
@app.route('/download', methods=['GET', 'POST'])

def download():        
    return render_template('download.html', title='download')
########################################################################################
# Kontak
@app.route('/kontak', methods=['GET', 'POST'])

def kontak():        
    return render_template('kontak.html', title='kontak')
########################################################################################
########################################################################################
########################################################################################
if __name__ == '__main__':
    app.run(debug=True)