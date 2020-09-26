from flask import Flask, render_template, request
from handlers.pulls import get_pulls
from handlers.pulls import get_request


app = Flask(__name__)
params = {'per_page': 100, 'state': 'all'}


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/pulls')
def pulls():
    state = request.args.get("state")
    return render_template("pulls.j2", pulls=get_pulls(state, get_request(params)))


app.run(debug=True)
