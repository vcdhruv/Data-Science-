from flask import Flask , jsonify , request

app = Flask(__name__)

items = [
    {"id":1,"name":"Item 1","description" : "This is item 1"},
    {"id":2,"name":"Item 2","description" : "This is item 2"}
]

@app.route("/",methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/<int:item_id>',methods=['GET'])
def get_item_by_id(item_id):
    item = [item for item in items if item["id"] == item_id]
    if len(item) == 0:
        return jsonify({"error" : "There is no such item."})
    else:
        return jsonify(item[0])
    
    
@app.route('/post_item',methods=['POST'])
def create_item():
    if request.method == 'POST':
        new_item = {
            "id" : items[-1]["id"] + 1,
            "name" : request.json["name"],
            "description" : request.json["description"]
        }
        items.append(new_item)
        return jsonify(new_item)
    
@app.route('/update_item/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = [item for item in items if item["id"] == item_id]
    if len(item) == 0:
        return jsonify({"error" : "item does not found."})
    else:
        update_item = {
            "id" : item[0]["id"],
            "name" : request.json["name"],
            "description" : request.json["description"]
        }
        item[0]["name"] = update_item["name"]
        item[0]["description"] = update_item["description"]

        return jsonify(update_item)

@app.route('/delete_item/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    item = [item for item in items if item["id"] == item_id]
    if len(item) == 0:
        return jsonify({"error" : "item does not found."})
    else:
        items = [item for item in items if item["id"] != item_id]
        return jsonify({"success":"Record deleted successfully."})

if __name__ == "__main__":
    app.run(debug=True)