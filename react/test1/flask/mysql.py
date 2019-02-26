from flask import Flask, jsonify, request, jsonify,render_template 
from flask_table import Table,Col,LinkCol
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

#from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test1'
#app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

class student(db.Model):
	ID = db.Column(db.String(100), primary_key = True)
	Name = db.Column(db.String(100))

	def __init__(self, ID, Name):
		self.ID = ID
		self.Name = Name
'''app.config['MySQL_USER'] = 'root1'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
#mysql.init_app(app)
#CORS(app) '''

class StudTable(Table):
	ID = Col('ID')
	Name = Col('Name')
	#update = LinkCol('Update','upd',url_kwargs=dict(id='ID'))
	delete = LinkCol('Delete','dele',url_kwargs=dict(id='ID'))

@app.route('/users/ins', methods=['POST'])
def ins():
	#cur = mysql.connection.cursor()
	#ID = request.get_json()['ID']
	#Name = request.get_json()['Name']
	#ID = request.form.get('ID')
	#Name = request.form.get('Name')
	
	#cur.execute("INSERT INTO student (ID,Name) VALUES ('" + str(ID) + "', '" + str(Name) + "')")

	#mysql.connection.commit()
	stud = student(ID=request.form['ID'], Name=request.form['Name'])
	db.session.add(stud)
	db.session.commit()
	#flash('Record was successfully added')
    #return redirect(url_for('show_all'))
	'''result = {
		"ID" : ID,
		"Name" : Name
	}'''
	#printf("Student Added")
	return "Student Added"
	#return jsonify({"result" : result})


@app.route('/users/view', methods=['GET'])
def view():
	#cur = mysql.connection.cursor()
	#ID = request.get_json()['ID']
	#Name = request.get_json()['Name']
	#result = ""

	#cur.execute("SELECT * FROM student")
	#rv = cur.fetchall()
	rv = student.query.all()
	table = StudTable(rv)

	#print(table.__html__())

	return table.__html__()
	
@app.route('/users/dele/<int:id>', methods=['GET','POST'])
def dele(id):
	#cur = mysql.connection.cursor()
	#ID = request.get_json()['ID']
	#Name = request.get_json()['Name']
	#ID = request.form.get('del_ID')
	#query = "Delete from student WHERE ID = " + ID
	#cur.execute(query)

	#mysql.connection.commit()
	
	student.query.filter_by(ID=id).delete()
	#st = student.query.filter_by(ID=id)
	#db.session.delete(st)
	db.session.commit()
	return "Student Deleted"
 

@app.route('/users/upd', methods=['GET','POST'])
def upd():
	#cur = mysql.connection.cursor()
	#up_ID = request.get_json()['up_ID']
	#new_Name = request.get_json()['new_Name']
	up_ID = request.form['up_ID']
	new_Name = request.form['new_Name']
	#query = "Update student SET Name = " + "'" + str(new_Name) + "'" + " WHERE ID = " + str(up_ID)
	#cur.execute(query)
	#mysql.connection.commit()
	qry = student.query.filter_by(ID=up_ID).update(dict(Name=new_Name))
	db.session.commit()
	#st = qry.first()
	return "Student Updated"


if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)