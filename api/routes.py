import flask
from flask import request, abort, make_response, jsonify
from json import JSONDecodeError, loads, dumps
from api import db


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
    data = {'message': 'Created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)


@app.route('/api/v1/tweets/', methods=['GET'])
def get_tweets():
    trails = db.query_db('select name, short_hand, status from trails')
    return dumps(trails)


if __name__  == '__main__':
    with app.app_context():
        db.init_db(app)
    app.run()

