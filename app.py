from functools import wraps
from flask import Flask,request, Response,render_template
from Quickstart import *
from base_mongo import *



app = Flask(__name__)
def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    for user in USER:
        if user['user']== username and user['pass']==password:
            return True
    #return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/datos',)
@requires_auth
def secret_page():
    return render_template('Microdatos.csv' )

@app.after_request
def after_request(response):
    auth = request.authorization

    base_mongo(datetime.now(),response.status_code,response.status,response.content_length,response.content_type,auth.username)
    return response
    


app.run(port=6123)



