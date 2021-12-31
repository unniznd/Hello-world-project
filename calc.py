
# Importing useful things from library
from flask import Flask, render_template

# "Flask" is a python class to make flask app
# "render_template" is a method to show html web page from "templates folder" using flask
# Refer about jinja engine to get more details on rendering templates

app = Flask(__name__)

# Making a object of class Flask by passing required parameters

@app.route("/",methods =['GET', 'POST'])

# Setting routes of app
# Example for route is, "https://www.abc.com/home" '/home' is route name 
# "https://www.abc.come/login" /login is route name
# No route name is denoted by "/"
# We can any number of routes, but routes must be unique
# methods above are "http methods" leave it like that (refer for more details)


def home():
    return render_template('home.html')

# home is function for the route defined above
# It return the rendering the template from the "templates/home.html"
# Make sure name of folder containing home.html is templates
# Please go through the html code too


@app.route("/name",methods =['GET', 'POST'])

def name():
    return render_template('name.html',name="Arjun")


if __name__=='__main__':
    app.run(debug=True)

# __name__ is special method in python 
# Make sure to add all routes before running
# app.run runs the app
# debug = True allows to get about errors

# run the file
# the output will be similar to as follows

#  Serving Flask app 'calc' (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 674-073-617


# Open the link showen in the line "Running on http://127.0.0.1:5000/""

# To go to other routes use the route name, "http://127.0.0.1:5000/(add route name here)"
# For example "http://127.0.0.1:5000/login"

