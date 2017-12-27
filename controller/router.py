
from flask import render_template, request
import os

import json
from werkzeug.utils import secure_filename

db = redis.Redis('localhost') #connect to server

class zzal:
    '''
    creator = "me"
    url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
    tag = "twice"
    '''
    def set(self, creator, url, tag):
        self.creator = creator
        self.url = url
        self.tag = tag

    def __init__(self):
        pass

    def __init__(self, creator, url, tag):
        self.set(creator, url, tag)

def get_zzal_list():
    return [zzal("me", "http://localhost:8080/static/upload_image/sana.gif", "twice"),
            zzal("me", "http://localhost:8080/static/upload_image/twice.gif", "twice"),
            zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet")]


def index():
    return render_template("index.html", zzal_list = get_zzal_list())


def my_page():
    return render_template("mypage.html")


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def my_page_zzal_upload_post(upload_folder):

    f = request.files['file']
    title = request.form['title']
    tag = request.form['tag']
    desc = request.form['description']
    zzal(title, tag, desc)

    json.dumps()


    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(upload_folder, filename))

        return 'success'
    else:
        return 'fail'


def my_page_zzal_upload_get():
    return render_template("upload.html")


def index_search():
    return "search"


def zzal_make():
    return render_template("make.html")


def page_not_found():
    return render_template('404.html'), 404


