#!/usr/bin/python3
""" list of states """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    states = sorted(storage.all('State').values(), key=lambda s: s.name)
    return render_template('states.html', states=states)


@app.route('/states/<id>')
def state_id(id):
    state = storage.all('State')
    key = "State.{}".format(id)
    try:
        state = all_states[key]
        return render_template('9-states.html', state=state,
                               condition="state_id")
    except IndexError:
        return render_template('9-states.html', condition='not_found')


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ just some quick teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
