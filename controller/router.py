
from flask import render_template, request
import os, sys
from werkzeug.utils import secure_filename
from models import db


SERVER_HOST = 'http://10.100.103.165:8080'
UPLOAD_FOLDER = 'static/upload_image'

db.init()

# class zzal:
#     '''
#     creator = "me"
#     url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
#     tag = "twice"
#     '''
#     def __init__(self, user_id, tag, url, title, descript, ref_count=0, like=0):
#         self.user_id = user_id
#         self.tag = tag
#         self.url = url
#         self.title= title
#         self.descript = descript
#         self.ref_count = ref_count
#         self.like = like
#
#     def like_up(self):
#         db.like_up(self.title)
#
#     def count_up(self):
#         db.count_up(self.title)
#
#
def get_zzal_list():
    return #zzal list


def index():
    return render_template("index.html", zzal_list = get_zzal_list())


def my_page():
    return render_template("mypage.html")


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def root_path():
    fn = getattr(sys.modules['__main__'], '__file__')
    root_path = os.path.abspath(os.path.dirname(fn))
    return root_path

def my_page_zzal_upload_post():
    f = request.files['upload_file']
    title = request.form['title']
    tag = request.form['tag']
    desc = request.form['desc']
    user_id = "lovely_zzaly"

    if f and allowed_file(f.filename):
        file_name = secure_filename(f.filename)
        file_path = os.path.join(root_path(), UPLOAD_FOLDER)

        f.save(os.path.join(file_path, file_name))
    else:
        return 'fail'


    url = file_path+"/"+file_name
    db.reg_image(user_id, tag, url, title, desc, 0 ,0 )
    return 'ok'



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


