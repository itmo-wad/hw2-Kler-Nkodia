from flask import Flask, send_from_directory
app = Flask(__name__)


@app.route('/<path:filename>')
def send_from_static(filename):
    return app.send_static_file(filename)


@app.route('/')
def index():
    return send_from_directory('', 'index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)