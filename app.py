from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        contents = file.read()
        return render_template('result.html', contents=contents.decode())
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
