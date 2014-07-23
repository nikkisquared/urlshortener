from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():

    print "my method: ", request.method
    print request.form.get("originalURL")
    
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":

        originalURL = request.form.get("originalURL")
        originalURL = str(originalURL)
        return u"YOUR URL: " + originalURL


if __name__ == '__main__':
    app.run(debug=True)