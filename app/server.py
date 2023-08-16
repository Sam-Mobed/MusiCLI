'''
small Flask server that will handle requests at the redirect URI;
Not necessary, but without it the user would have to copy and paste the redirect uri with the token on the terminal, which isn't ideal.
the callback uri:http://localhost:3000/callback
'''
from flask import Flask, render_template

def start_server()->None:
    app = Flask(__name__)

    @app.route('/callback')
    def callback()->str:
        #handle the URL, which contains the accesss token
        return render_template("index.html")
    
    app.run(host='localhost', port=3000)