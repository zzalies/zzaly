
from flask import render_template, json


class zzal:
    creator = "me"
    url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
    tag = "twice"


zzal_list = [zzal, zzal, zzal]


def index():
    return render_template("index/index.html", zzal_list = zzal_list)


def my_page():
    return render_template("mypage.html")


def my_page_zzal_upload():
    return "Zzal upload"


def index_search(user_name):
    json_data = { 'list': ['static/upload_image/jeny.gif', 'static/upload_image/jisoo.gif', 'static/upload_image/sana.gif']}
    return json.dumps(json_data)


def index_board():
    f = request.files['upload_file']
    f.save(os.path.join(file_path, file_name))
    return render_template("")