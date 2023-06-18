
# @app.route("/cricket",methods=["POST"])
# def selected_player_details():
#     player_details = {}
#     if request.method == "POST":
#         player_details["Player Name"] = request.form["player_name"]
#         player_details["Player Age"] = int(request.form["age"])
#         player_details["Player Role"] = request.form["role"]
#         cricket_collection.insert_one(player_details)
#         result = "{} of jersey no {} who is {} has been selected in an INDIAN TEAM".format(player_details["Player Name"],player_details["Player Age"],player_details["Player Role"])
#         return render_template('result.html',result=result)