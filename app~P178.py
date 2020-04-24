from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = b'randam string...'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
                           title='Index', \
                           message='※UI関係について', \
                           flg=None, \
                           alert='※フォームを送信してください。')

@app.route('/', methods=['POST'])
def form():
    pf = request.form.get('platform')
    if pf in ['Windows', 'macOS']:
        flg = True
        alert = 'OK!問題ありません。'
    else:
        flg = False
        alert = 'すみません。%sは対応していません。。。' % pf
    return render_template('index.html', \
                           title='Index', \
                           message='※UI関係について', \
                           flg = flg,
                           alert=alert)

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost')