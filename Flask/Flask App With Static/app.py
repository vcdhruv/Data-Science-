from flask import Flask,request ,render_template , jsonify , redirect , url_for

app = Flask(__name__)


# @app.route('/')
# def home_page():
#     return render_template('index.html')

@app.route("/welcome")
def welcome():
    return "<h1>Welcome To ABC Corporation</h1>"

data = {
        "Company Name" : "ABC Corporation",
        "Location" : "India",
        "Contact Detail" : "999-999-9999"
    }

@app.route('/')
def detail():
    return render_template('data.html',data=data)

@app.route("/redirect_to_welcome")
def redirect_go():
    return redirect(url_for('welcome'))

@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return render_template('results.html' , result = result)




@app.route('/postman_action',methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return jsonify(result)
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
