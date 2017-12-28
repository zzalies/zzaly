from werkzeug.utils import secure_filename
from flask import render_template, request
from models import db
import os
import sys



#
# class Zzal:
#     '''
#     creator = "me"
#     url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
#     tag = "twice"
#     '''
#
#     def set(self, creator, url, tag, ref_count, desc):
#         self.creator = creator
#         self.url = url
#         self.tag = tag
#         self.desc = desc
#         self.ref_count = ref_count
#
#     def __init__(self):
#         pass
#
#     def __init__(self, creator, url, tag, ref_count, desc):
#         self.set(creator, url, tag, ref_count, desc)
#
#
# class Statistics:
#     def set(self, total_ref_count):
#         self.total_ref_count = total_ref_count
#
#     def __init__(self):
#         pass
#
#     def __init__(self, total_ref_count):
#         self.set(total_ref_count)
#
# def get_zzal_list():
#     return [Zzal("me", "http://localhost:8080/static/upload_image/sana.gif", "twice", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
#             Zzal("me", "http://localhost:8080/static/upload_image/twice.gif", "twice", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."),
#             Zzal("me", "http://localhost:8080/static/upload_image/irene.gif", "red velvet", 3, "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.")]
# =======



SERVER_HOST = 'http://10.100.103.165:8080'
UPLOAD_FOLDER = 'static/upload_image'
USER_ID = "lovely_zzaly"

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
def get_post_list():
    return db.get_post()


def index():
    return render_template("index.html", zzal_list=get_post_list())


def my_page():
    total_count = 0
    # statistics = Statistics(total_count)

    zzal_list = db.get_post_by_user(USER_ID)
    temp = ""
    for zzal in zzal_list:
        ref_count_byte  = "ref_count"

        print(zzal.encode('utf-8'))
        total_count += int(zzal[ref_count_byte.encode('utf-8')].decode('utf-8'))
        temp=zzal["url".encode('utf-8')].decode('utf-8')

    return render_template("mypage.html", zzal_list=zzal_list, total_count=total_count, temp=temp)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def root_path():
    fn = getattr(sys.modules['__main__'], '__file__')
    root_path = os.path.abspath(os.path.dirname(fn))
    return root_path

def my_page_zzal_upload_post():
    print('1')
    print(request.values.values())
    title = request.form['title']
    tag = request.form['tag']
    desc = request.form['desc']
    print('2')

    f = request.files['upload_file']
    user_id = USER_ID
    print(title, tag, desc)

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
    key = request.args.get('tag')
    return db.get_post_by_tag(key)


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



def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result
