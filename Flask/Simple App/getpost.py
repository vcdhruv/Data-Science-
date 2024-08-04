from flask import Flask,render_template,request

'''
It will create an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome To Flask.</h1>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

#entry point of any .py file
if __name__ == "__main__":
    app.run(debug=True)