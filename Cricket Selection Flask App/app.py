import pymongo
from pymongo.mongo_client import MongoClient
from flask import Flask , render_template , request , jsonify


uri = "mongodb+srv://vcdhruv777:vcd7777777@cluster0.fsbb6ej.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client.test
print(db)


app = Flask(__name__)

db = client["Cricket_Selection"]

cricket_collection = db["player_details"]

@app.route("/",methods=["GET","POST"])
def home_page():
    return render_template('index.html')

@app.route("/cricket",methods=["POST"])
def selected_player_details():
    pd = {}
    if request.method == "POST":
        pd["Player Name"] = request.form["player_name"]
        pd["Player Age"] = int(request.form["age"])
        pd["Player Role"] = request.form["role"]
        cricket_collection.insert_one(pd)
        result = "{} of jersey no {} who is {} has been selected in an INDIAN TEAM".format(pd["Player Name"],pd["Player Age"],pd["Player Role"])
        return render_template('result.html',result=result)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)