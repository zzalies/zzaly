from werkzeug.utils import secure_filename
from flask import render_template, request, json
from models import db
import os
import sys
from util import convert_gif, get_root_path
from flask import render_template, json, request, redirect

import datetime

SERVER_HOST = 'http://10.100.103.165:8080'
UPLOAD_FOLDER = 'static/upload_image'
USER_ID = "lovely_zzaly"



db.init()


def get_post_list():
    return db.get_post()




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
    print(os.pardir)

    try:
        if f and allowed_file(f.filename):
            f.save(os.path.join(get_root_path.get_root_path()+"/static/upload_image/", f.filename))
            print("성공")
            url = "./static/upload_image/" + f.filename
            db.reg_image(user_id, tag, url, title, desc, 0, 0)
            return 'ok'
    except Exception as e:
        print(str(e))
        return 'fail'


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
    gif_title = request.form.get('gif_title')
    gif_tag = request.form.get('gif_tag')
    duration = float(request.form.get('duration')) #float 형변환
    url_list = json.JSONDecoder().decode(request.form.get('url_list'))
    file_list = request.files.getlist("upload_image")
    seq_list = json.JSONDecoder().decode(request.form.get('seq_list'))
    
    if gif_title == None and gif_tag == None and duration == None and seq_list == None :
        return 'parm error' 

    if len(seq_list) != len(url_list) + len(file_list) :
        print(seq_list)
        print(url_list)
        print(file_list)
        return 'file, url error'
    
    print(gif_title,gif_tag,duration,url_list,file_list,seq_list)
    url_idx = 0
    file_idx = 0
    gif = convert_gif.ConvGIF()
    for seq in seq_list:
        if seq == 'file':
            gif.SetFile(file_list[file_idx].stream.read())
            file_idx += 1
        elif seq == 'url':
            gif.SetURL(url_list[url_idx])
            url_idx += 1
    path = gif.Convert(gif_title,duration)
    if path == None :
        return 'error'
    # gif_tag 레디스 등록
    db.reg_image(USER_ID, gif_tag, path, gif_title, 'user make', 0 ,0 )
    return path


def zzal_make_video_post():
    gif_title = request.form.get('gif_title')
    gif_tag = request.form.get('gif_tag')
    path = request.form.get('video_path')
    start_min = requset.form.get('start_min')
    start_sec = request.fomr.get('start_sec')
    end_min = request.form.get('end_min')
    end_sec = request.form.get('end_sec')

    return 'ok'

def zzal_make_video_reg():
    yurl = request.form.get('youtube')
    reponse = {length:'4.20'}
    return response
    
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
    print(os.path.abspath((os.pardir)))