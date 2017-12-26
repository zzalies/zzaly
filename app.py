from flask import Flask
from controller import router


app = Flask(__name__)


@app.route('/')
def index():
    return router.index()


@app.route('/mypage')
def my_page():
    return router.my_page()


@app.route('/index/search')
def search():
    return router.index_search()


@app.route('/mypage/zzal/upload')
def zzal_upload():
    return router.my_page_zzal_upload()


if __name__ == '__main__':
    app.run()


