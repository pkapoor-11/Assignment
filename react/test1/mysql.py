from flask import Flask, jsonify, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MySQL_USER'] = 'root1'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

@app.route('/users/ins', methods=['POST'])
def ins():
	cur = mysql.connection.cursor()
	ID = request.get_json()['ID']
	Name = request.get_json()['Name']
	cur.execute("INSERT INTO student (ID,Name) VALUES ('" + str(ID) + "', '" + str(Name) + "')")

	mysql.connection.commit()

	result = {
		"ID" : ID,
		"Name" : Name
	}

	return jsonify({"result" : result})


@app.route('/users/view', methods=['POST'])
def view():
	cur = mysql.connection.cursor()
	ID = request.get_json()['ID']
	Name = request.get_json()['Name']
	result = ""

	cur.execute("SELECT * FROM student")
	rv = cur.fetchone()
	result = {
		"ID" : rv['ID'],
		"Name" : rv['Name']
	}

	return jsonify({"result" : result})


if __name__ == '__main__':
	app.run(debug=True)