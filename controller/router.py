from werkzeug.utils import secure_filename
from flask import render_template, request, json
from models import db
import os
import sys
from util import convert_gif
import datetime

SERVER_HOST = 'http://10.100.103.165:8080'
UPLOAD_FOLDER = 'static/upload_image'
USER_ID = "lovely_zzaly"

db.init()


def get_post_list():
    return db.get_post()


from flask import render_template, json, request, redirect


class zzal:
    creator = "me"
    url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
    tag = "twice"


zzal_list = [zzal, zzal, zzal]


def index():
    return render_template("index.html", article_list=get_article())


def bytemap_to_stringmap(bytemap):
    stringmap={}
    for k in bytemap.keys():
        v=bytemap[k]
        stringmap[k.decode('utf-8')]=v.decode('utf-8')

    return stringmap


def my_page():
    total_count = 0
    # statistics = Statistics(total_count)

    zzal_list_byte = db.get_post_by_user(USER_ID)
    temp = ""
    zzal_list = list()
    for zzal_byte in zzal_list_byte:
        zzal = bytemap_to_stringmap(zzal_byte)
        total_count += int(zzal["ref_count"])
        zzal_list.append(zzal)

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

    try:
        if f and allowed_file(f.filename):
            file_name = secure_filename(f.filename)
            file_path = os.path.join(root_path(), UPLOAD_FOLDER)

            f.save(os.path.join(file_path, file_name))
    except :
        return 'fail'


    url = "./static/upload_image/"+file_name
    db.reg_image(user_id, tag, url, title, desc, 0 ,0 )
    return 'ok'


def my_page_zzal_upload_get():
    return render_template("upload.html")


def index_search(user_name):
    image = db.get_post_by_tag(user_name)
    image_list=bytemap_to_stringmap(image)
    str_list=list()
    for item in image_list.values():
        str_list.append(item)
    json_data = { "list": str_list }
    return json.dumps(json_data)


def zzal_make_get():
    return render_template("create.html")


def zzal_make_post():
    title = request.form.get('gif_title')
    print(title)
    url_list = request.form.get('url_list')
    dec = json.JSONDecoder()
    ll = dec.decode(url_list)
    if ll != None :
        gif = convert_gif.ConvGIF()
        for url in ll:
            gif.SetURL(url)
        return gif.Convert(title,0.1)
    
    return 'ok'    
'''
    for i in range(file_cnt):
        file_name = 'sys_' + str(i)
        f = request.files[file_name]
 '''       
    


def page_not_found():
    return render_template('404.html'), 404


def create_article():
    num = 1
    key_title = request.form.get("index_title")
    title = key_title
    key_title = "image/"+key_title
    content = request.form.get("index_text")
    # while(1) :
    #     if db.keycheck(key_title) == 0 :
    #         key_title = key_title+"_ayoungcustom"+str(num)
    #         print(key_title,num)
    #         break
    #     num+=1
    #
    # if len(request.form.get("gif_selected")) == 0:
    #     image = "none"
    # else:
    image = request.form.get("gif_selected")

    db.reg_post(title,content, image)

    return "ok"


def get_article():
    post_list = db.get_post()
    result = list()
    for item in post_list:
        result.append(bytemap_to_stringmap(item))
    print(result)
    return result


'''
def index_search(user_name):
    json_data = { 'list': ['static/upload_image/jeny.gif', 'static/upload_image/jisoo.gif', 'static/upload_image/sana.gif']}
    return json.dumps(json_data)
'''

def index_board():
    title = request.form.get("index_title")
    content = request.form.get("index_text")

    image = "none"
    if len(request.form.get("gif_selected")) == 0:
        db.reg_post(title, content, "none")
    else:
        image = request.form.get("gif_selected")
        db.reg_post(title, content, image)


    return "ok"


if __name__ == '__main__':
    get_article()
    print(datetime.datetime.now().isoformat())