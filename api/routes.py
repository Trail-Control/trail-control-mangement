import flask
from flask import request, abort
from json import JSONDecodeError, loads


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return "<h1>Hello Word</h1>"


@app.route('/api/v1/tweets/', methods=['POST'])
def import_tweets():
    if request.json is None:
        return abort(400, 'Not Json or no data recieved.')
    try:
        loads(request.json)
    except JSONDecodeError as e:
        return abort(400, 'Bad Json data')
    return "<p>{}</p>".format(request.json)


@app.route('/api/v1/tweets/', methods=['GET'])
def get_tweets():
    return "twittles"


if __name__  == '__main__':
    app.run()