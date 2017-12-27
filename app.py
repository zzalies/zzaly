from flask import Flask, render_template, request, redirect, url_for
from controller import router


### page ##

app = Flask(__name__)
UPLOAD_FOLDER = './static/upload_image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

temp = "dddd"

@app.route('/')
def root():
    return router.index()


@app.route('/index')
def index():
    return router.index()


@app.route('/index/search')
def search():
    return router.index_search()


@app.route('/mypage')
def my_page():
    return router.my_page()


@app.route('/mypage/zzal/upload',  methods=['GET', 'POST'])
def zzal_upload():
    if request.method == 'POST':
        return router.my_page_zzal_upload_post(UPLOAD_FOLDER)

    return router.my_page_zzal_upload_get()



@app.route('/mypage/zzal/make', methods=['GET', 'POST'])
def zzal_make():
    if request.method == 'GET':
        return router.zzal_make_get()

    elif request.method == 'POST':
        return router.zzal_make_post()



@app.errorhandler(404)
def page_not_found(e):
    return router.page_not_found()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


