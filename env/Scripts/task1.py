from flask import Flask,render_template, redirect, url_for, request
#creates an app
app=Flask(__name__,template_folder='template')
@ app.route("/", methods=["POST", "GET"])
def home():
	if(request.method=="POST"):
		name=request.form["clubName"]
		desc=request.form["clubdesc"]
		cat=request.form["category"]
		return render_template("home.html",clubName=name,clubdesc=desc,category=cat)
	else:
		return render_template("index.html",club="Lion's Club",description="This is a Social Impact Club",categoryName="Social Impact")

if(__name__=="__main__"):
	app.run(debug=True)

