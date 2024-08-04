### Jinja 2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions,for loop
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for

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

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

#Variable rule
@app.route('/success/<int:score>')
def success(score):
    return render_template('result.html',results=score)

@app.route("/successloop/<int:score>")
def successloop(score):
    res = ""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    exp = {"result" : res , "score" : score}
    return render_template("resultloop.html",results=exp)

@app.route("/marks_form",methods=['GET','POST'])
def student_form():
    total_score = 0
    if request.method == 'POST':
        c = float(request.form['c'])
        java = float(request.form['java'])
        python = float(request.form['python'])
        total_score = (c + java + python)/3
        return redirect(url_for('success',score=total_score))
    return render_template('student_form.html')

#entry point of any .py file
if __name__ == "__main__":
    app.run(debug=True)