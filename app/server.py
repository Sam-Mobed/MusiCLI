'''
small Flask server that will handle requests at the redirect URI;
Not necessary, but without it the user would have to copy and paste the redirect uri with the token on the terminal, which isn't ideal.
the callback uri:http://localhost:3000/callback
'''
from flask import Flask, request, render_template
from spotify import get_authorization_token
from waitress import serve
from messages import authorizationSuccessful

def start_server()->None:
    app = Flask(__name__)

    @app.route('/callback')
    def callback()->str:
        authorization_code = request.args.get('code')
        if authorization_code:
            get_authorization_token(authorization_code)
            authorizationSuccessful()
            return render_template("index.html")
        else:
            return 'Authorization failed. Please close this window and try again.'
    
    #we use waitress, a production WSGI server. because if we do app.run, it will display a warining that I can't mute, ruining the CLI.
    serve(app, host='localhost',port=3000)