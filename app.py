import os, datetime
import re
from flask import Flask, request, render_template, redirect, abort, flash, json

from unidecode import unidecode

from os import listdir
from os.path import isfile, join



# mongoengine database module
#from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)   # create our flask app
#app.config['CSRF_ENABLED'] = True
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG'] = True


# import data models
#import models

#from models import Vote


# --------- Routes ----------
# this is our main page
@app.route("/", methods=['GET'])
def index():
		


	return render_template("index.html")

@app.route("/gallery", methods=['GET'])
def gallery():
	#onlyfiles = [ f for f in listdir("/Users/markbreneman/Desktop/ArtStartPlusSmart/static/img/ASK") if isfile(join("/Users/markbreneman/Desktop/ArtStartPlusSmart/static/img/ASK",f)) ]
	#app.logger.debug(onlyfiles)
	return render_template("gallery.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404





# --------- Server On ----------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)
	# app.run(host='127.0.0.1', port=port)



	