from flask import Flask, redirect, render_template, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
	mysql = connectToMySQL('friendsdb')
	my_friends = mysql.query_db("SELECT * FROM friends")
	lngthOfFriends = len(my_friends)
	print(my_friends)
	return render_template("index.html", friends = my_friends, lngth= lngthOfFriends)

@app.route('/add', methods = ['POST'])
def addFriends():
	mysql = connectToMySQL('friendsdb')
	
	
	
	query = "INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
	
	data = { 
	"first_name": request.form["first_name"], 
	"last_name": request.form["last_name"],
	"occupation": request.form["occupation"]
	}
	
	mysql.query_db(query, data)
	
	return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)