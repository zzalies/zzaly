from flask import Flask, render_template, request, redirect, url_for
from controller import router

### page ##

app = Flask(__name__)

@app.route('/')
def root():
    return router.index()

@app.route('/index')
def index():
    return router.index()


@app.route('/index/search/<user_name>')
def search(user_name):
    return router.index_search(user_name)


@app.route('/index/board', methods=['GET', 'POST'])
def board():
    if request.method == 'POST':
        return router.create_article()


@app.route('/mypage')
def my_page():
    return router.my_page()


@app.route('/mypage/zzal/upload',  methods=['GET', 'POST'])
def zzal_upload():
    if request.method == 'POST':
        if router.my_page_zzal_upload_post()=='ok':
            return redirect('/mypage')
        else :
            return redirect('/mypage/zzal/upload')
    elif request.method == 'GET':
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



## functions

# @app.route('/mypage/zzal/upload')
# def

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


