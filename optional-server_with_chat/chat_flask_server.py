from flask import Flask, render_template, request
app = Flask(__name__)

messages = []

@app.route('/', methods=["GET", "POST"])
def index():
    global messages
    if request.method == "GET":
        return render_template("chat.html", "")
    else:
        message = request.form["message"]
        messages.append("From user: "+ message)
        return render_template("chat.html", history=messages, new=message)
        #return render_template("test-chat.html", new_message=message)
        #return message


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)