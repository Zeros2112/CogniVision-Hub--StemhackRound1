import os
from flask import Flask, request, render_template
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# Định dạng cho phép
ALLOWED_EXTENSIONS = set(['mp4']) 

app = Flask(__name__)
# Khóa bí mật
app.secret_key = "bimatl@mnha"

# Nơi lưu file tải lên
app.config['UPLOAD_FOLDER'] = 'static/uploads/' 

# Dung lượng (ví dụ 16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form3.html')
    else:
        question = request.form['question']

        # Nếu trường thông tin gửi lên không có trường thông tin nào có tên là file
        if 'file' not in request.files:
            flash('none of the files are entered')
            return redirect(request.url)
        file = request.files['file']
        # Nếu không có file nào được chọn
        if file.filename == '':
            flash('none of the files are entered')
            return redirect(request.url)
        # Nếu file tải lên là file có định dạng được cho phép
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Xử lý phân tích hình ảnh tại đây và cho kết quả
            result = "Đây là con mèo"

            return render_template('results3.html', question=question, filename=filename, result=result)
        # Nếu không phải là file có định dạng cho phép
        else:
            flash('Định dạng cho phép là: mp4')
            return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__ == '__main__':
    app.run()