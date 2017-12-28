from flask import Flask
from controller import router


### page ##

app = Flask(__name__)

temp = "dddd"

@app.route('/')
def root():
    return router.index()


@app.route('/index')
def index():
    return router.index()


@app.route('/mypage')
def my_page():
    return router.my_page()


@app.route('/index/search/<user_name>')
def search(user_name):
    return router.index_search(user_name)


@app.route('/index/board', methods=['GET', 'POST'])
def board():
    if request.method == 'POST':
        return router.index_board()


@app.route('/mypage/zzal/upload')
def zzal_upload():
    return router.my_page_zzal_upload()



## functions

# @app.route('/mypage/zzal/upload')
# def

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


