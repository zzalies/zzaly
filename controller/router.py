
from flask import render_template


class zzal:
    creator = "me"
    url = "https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif"
    tag = "twice"


zzal_list = [zzal, zzal, zzal]


def index():
    return render_template("index.html", zzal_list = zzal_list)


def my_page():
    return render_template("mypage.html")


def my_page_zzal_upload():
    return "Zzal upload"


def index_search():
    return "Zzal upload"
