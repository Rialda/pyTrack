from flask import Flask, render_template

app = Flask(__name__)


# @ signifies a decorator - for wrapping function and modifying it's behavior
# @ map a url to a return value
@app.route('/')
@app.route('/<data_source>')
def index(data_source=None):
    return render_template("data.html", data_source=data_source)


@app.route('/test')
def test():
    test_list = ["Item1", "Item2", "Item3"]
    return render_template("test.html", test_list=test_list)


# make sure to start the web server whenever this file is called directly
if __name__ == "__main__":
    app.run(debug=True)
