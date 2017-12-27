
from flask import render_template, request
import os
from werkzeug.utils import secure_filename

server_host = 'http://10.100.103.165:8080'

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
    return [zzal("me", server_host + "/static/upload_image/sana.gif", "twice"),
            zzal("me", server_host + "/static/upload_image/twice.gif", "twice"),
            zzal("me", server_host + "/static/upload_image/irene.gif", "red velvet")]


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

    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(upload_folder, filename))
        return 'success'
    else:
        return 'fail'


def my_page_zzal_upload_get():
    return render_template("upload.html")


def index_search():
    key = request.args.get('key')
    return key


def zzal_make_get():
    return render_template("make.html")


def zzal_make_post():
    file_cnt = request.form.get('file_cnt')

    for i in range(file_cnt):
        file_name = 'sys_' + str(i)
        f = request.files[file_name]
        is_file = request.form.get('is_file')

        return 'success'
    else:
        return 'fail'


def page_not_found():
    return render_template('404.html'), 404


