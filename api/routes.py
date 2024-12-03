import flask
from flask import request, abort, make_response, jsonify
from json import JSONDecodeError, loads, dumps
from api import db
from flask_cors import cross_origin


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return "<h1>Hello Word</h1>"


@app.route('/api/v1/tweets/', methods=['POST'])
def import_tweets():
    db.init_db(app)
    query = 'insert into trails (name, updated_date, status) values(?, ?, ?)'
    if request.json is None:
        return abort(400, 'Not Json or no data recieved.')
    try:
        json_tweets = request.json
        res = db.insert_rows(query, json_tweets)
    except JSONDecodeError as e:
        return abort(400, 'Bad Json data')
    data = {'message': 'Created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)


@app.route('/api/v1/tweets/', methods=['GET'])
@cross_origin()
def get_tweets():
    trails = db.query_db('select name, updated_date, status from trails')
    return dumps(trails)


if __name__  == '__main__':
    with app.app_context():
        db.init_db(app)
    app.run()

