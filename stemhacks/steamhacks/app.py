import os
from flask import Flask, request, render_template
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from texttrans import * 



app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        question = request.form['question']
        result = enter(question)
        return render_template('results.html', question=question, result=result)
    

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__ == '__main__':
    app.run()