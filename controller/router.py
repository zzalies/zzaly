
from flask import render_template, request
import os
import redis
import json
from werkzeug.utils import secure_filename

db = redis.Redis('localhost')  # connect to server

class Zzal:
    '''
    creator = "me"
    url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
    tag = "twice"
    '''

    def set(self, creator, url, tag, ref_count, desc):
        self.creator = creator
        self.url = url
        self.tag = tag
        self.desc = desc
        self.ref_count = ref_count

    def __init__(self):
        pass

    def __init__(self, creator, url, tag, ref_count, desc):
        self.set(creator, url, tag, ref_count, desc)


class Statistics:
    def set(self, total_ref_count):
        self.total_ref_count = total_ref_count

    def __init__(self):
        pass

    def __init__(self, total_ref_count):
        self.set(total_ref_count)

def get_zzal_list():
    return [Zzal("me", "http://localhost:8080/static/upload_image/sana.gif", "twice", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
            Zzal("me", "http://localhost:8080/static/upload_image/twice.gif", "twice", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
            Zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.")]


def index():
    return render_template("index.html", zzal_list = get_zzal_list())


def my_page():

    zzal_list = [Zzal("me", "http://localhost:8080/static/upload_image/sana.gif", "twice", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
                 Zzal("me", "http://localhost:8080/static/upload_image/twice.gif", "twice", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
                 Zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
                 Zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
                 Zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
                 Zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
                 Zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.")]

    total_count = 0
    for z in zzal_list:
        total_count += z.ref_count

    statistics = Statistics(total_count)

    return render_template("mypage.html", zzal_list=zzal_list, statistics=statistics)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def my_page_zzal_upload_post(upload_folder):

    f = request.files['file']
    title = request.form['title']
    tag = request.form['tag']
    desc = request.form['description']
    Zzal(title, tag, desc)

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


