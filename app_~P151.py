from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = b'randam string...'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
                           title='Index', \
                           message='Hello! This is Bootstrap sample.', )

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost')