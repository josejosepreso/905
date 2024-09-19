from flask import Flask

# 
from routes.public import public
from routes.user import user

app = Flask(__name__)

#
app.register_blueprint(public)
app.register_blueprint(user)
