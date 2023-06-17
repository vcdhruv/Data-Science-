from flask import Flask , render_template , request , jsonify
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vcd7777777"
)
mycursor = mydb.cursor()


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home_page():
    return render_template('index.html')

@app.route("/details",methods=["POST"])
def studentDetails():
    if request.method == "POST":
        student_name = request.form["student_name"]
        roll_no = request.form["roll_no"]
        spi = request.form["spi"]
        semester = request.form["semester"]
        # mycursor.execute("insert into College_Students.test_table values({},{},{},{})".format(str(student_name),int(roll_no),float(spi),int(semester)))
        query = "INSERT INTO College_Students.student_details (student_name, roll_no, spi, semester) VALUES (%s, %s, %s, %s)"
        values = (student_name, roll_no, spi, semester)
        
        mycursor.execute(query, values)
        mydb.commit()
        mydb.close()
        result = "student: "+str(student_name)+" roll no.: "+str(roll_no)+" spi: "+str(spi)+" semester: "+str(semester)+" has been succesfully entered."
        return render_template('result.html',result=result)

if __name__ == "__main__":
    app.run("0.0.0.0")