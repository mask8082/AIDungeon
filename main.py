from flask import g
from flask import session
import os
from story.utils import *
import json
from flask import Flask, render_template, request, abort
from story.story_manager import *
from generator.web.web_generator import *
from other.cacher import *

app = Flask(__name__)
app.secret_key = '#d\xe0\xd1\xfb\xee\xa4\xbb\xd0\xf0/e)\xb5g\xdd<`\xc7\xa5\xb0-\xb8d0S'
GOOGLE_CRED_LOCATION = "./AI-Adventure-2bb65e3a4e2f.json"

@app.route('/')
def root():
    seed = -1
    data = {'seed': seed}
    return render_template('index.html', data=data)


@app.route('/<seed>')
def rootseed(seed):
    if seed == "":
        seed = -1
    else:
        seed = int(seed)
    data = {'seed': seed}
    session["seed"] = seed
    return render_template('index.html', data=data)


@app.route('/index.html')
def index():
    data = {'seed': -1}

    return render_template('index.html', data=data)


@app.route('/about.html')
def about():
    return render_template('about.html')


def story_init(session, seed):
    pass

@app.route('/generate', methods=['POST'])
def story_request():
    pass
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)