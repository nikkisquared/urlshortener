from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():

    print "my method: ", request.method
    print request.data
    
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return "YOU GOT HERE FROM POST!"

if __name__ == '__main__':
    app.run(debug=True)