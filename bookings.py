# build 1 19072018-1416
import os, json
from flask import Flask, make_response
from werkzeug.exceptions import NotFound

# addon
def root_dir():
    """ Returns root director for this project """
    #return os.path.dirname(os.path.realpath(__file__ + '/..'))
    return os.path.dirname(os.path.realpath(__file__ + '/'))

def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys = True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response
# end-addon

app = Flask(__name__)

with open("{}/bookings.json".format(root_dir()), "r") as f:
    bookings = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "bookings": "/bookings",
            "booking": "/bookings/<username>"
        }
    })


@app.route("/bookings", methods=['GET'])
def booking_list():
    return nice_json(bookings)


@app.route("/bookings/<username>", methods=['GET'])
def booking_record(username):
    if username not in bookings:
        raise NotFound

    return nice_json(bookings[username])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6003, use_reloader=True)

