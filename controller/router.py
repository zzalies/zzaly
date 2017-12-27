
from flask import render_template, request
import os
import redis
import json
from werkzeug.utils import secure_filename


class zzal:
    creator = "me"
    url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
    tag = "twice"


zzal_list = [zzal, zzal, zzal]
db = redis.Redis('localhost')  # connect to server

def index():
    return render_template("index.html", zzal_list = zzal_list)


def my_page():
    return render_template("mypage.html")


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def my_page_zzal_upload_post(upload_folder):
    f = request.files['file']

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


