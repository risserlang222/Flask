from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = b'randam string...'

member_data = {'a':'a'}
message_data = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
                           title='Index', \
                           message='※Vue.js')

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost')