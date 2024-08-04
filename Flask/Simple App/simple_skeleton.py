from flask import Flask

'''
It will create an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome To Flask. Hello World!"

@app.route("/index")
def index():
    return "Welcome to index page"

#entry point of any .py file
if __name__ == "__main__":
    app.run(debug=True)