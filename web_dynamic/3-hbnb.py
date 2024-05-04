#!/usr/bin/python3
"""hbnb"""
from models import storage
from flask import Flask, render_template, url_for
import uuid


# flask
app = Flask(__name__)
app.url_map.strict_slashes = False
h = '0.0.0.0'
p = 5000


# begin
@app.teardown_appcontext
def teardown_db(exception):
    """close"""
    storage.close()


@app.route('/3-hbnb/')
def hbnb_filters(the_id=None):
    """hbnb_filters"""
    stateObjs = storage.all('State').values()
    states = dict([state.name, state] for state in stateObjs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = uuid.uuid4()
    return render_template('3-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)

if __name__ == "__main__":
    """main"""
    app.run(host=h, port=p)
