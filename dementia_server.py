from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    return "dementia server"


@app.route('/address',methods=['GET','POST'])
def address_request():
    return render_template("daum.html")
app.run(host="0.0.0.0", port=5000, debug=True)
