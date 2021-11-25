from flask import Flask, render_template, url_for, request, redirect
from core import app

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return redirect('/')
    else:
        # return render_template('index.html', tasks=tasks)
        return 'Hello world'