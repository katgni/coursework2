from flask import Flask, request, render_template, url_for, g, redirect, session, flash, request, jsonify, json
from functools import wraps
import sqlite3
import settings
import sqlite3 as sql


from main import Main
from login import Login
from data import Data

app = Flask(__name__)

app.secret_key = settings.secret_key


@app.route('/')
def root():
    connection = sqlite3.connect("mydatabase.db")
    connection.row_factory = sqlite3.Row

    rows = connection.cursor().execute("SELECT * FROM categories").fetchall()
    
    return render_template("index.html", rows=rows)

	
	#Templates for errors
	
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

	
@app.route('/treasures')
@app.route('/treasures/<name>')
def treasures(name):
	sql = ('SELECT * FROM treasures WHERE page_name = ?')
	connection = sqlite3.connect("mydatabase.db")
	connection.row_factory = sqlite3.Row     		
	treasures = connection.cursor().execute(sql,[name]).fetchall()
    
	sql2 = ('SELECT * FROM categories')
	connection = sqlite3.connect("mydatabase.db")
	connection.row_factory = sqlite3.Row     		
	all = connection.cursor().execute(sql2).fetchall()
    
	return render_template('treasures.html',  name=name, all=all, treasures=treasures)  
	connection.close()
    
@app.route('/category')
@app.route('/category/<name>')
def category(name):
	sql = ('SELECT * FROM categories WHERE page_name = ?')
	connection = sqlite3.connect("mydatabase.db")
	connection.row_factory = sqlite3.Row     		
	rows = connection.cursor().execute(sql,[name]).fetchall()
    
	sql2 = ('SELECT * FROM treasures WHERE category = ?')
	connection = sqlite3.connect("mydatabase.db")
	connection.row_factory = sqlite3.Row     		
	treasures = connection.cursor().execute(sql2,[name]).fetchall()
   	all = connection.cursor().execute("SELECT * FROM categories").fetchall()
    
	return render_template('category.html', rows = rows, name=name, all=all, treasures=treasures)  
    
	
	
@app.route('/form', methods=('GET', 'POST'))
def form():
    msg = None
    if request.method == 'POST':
      try:
        name = request.form['name']
        year = request.form['year']
        info = request.form['info']
        location = request.form['location']
        page_name = request.form['page_name']
        category = request.form['category']
        img = request.form['img']
        img2 = request.form['img2']

        if (name and year and info and location and page_name and category and img and img2):
           con = sqlite3.connect("mydatabase.db")
           cur = con.cursor()
           cur.execute("INSERT INTO treasures (name,year,info,location,page_name,category,img,img2) VALUES (?,?,?,?,?,?,?,?)",(name,year,info,location,page_name,category,img,img2) )

           con.commit()
           msg = "Record successfully added"

        else:
           msg = "Please enter details in each field"

      except:
           msg="Something went wrong. Try again."
           print msg


    return render_template('form.html', msg=msg)
  

@app.route('/list')
def list():
    con = sql.connect("mydatabase.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from treasures")
   
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)
	
	
@app.route('/delete')
def delete():
    con = sql.connect("mydatabase.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from treasures")
    rows = cur.fetchall();
	
    return render_template("delete.html",rows = rows)
	
	
# Routes for login
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])

app.add_url_rule('/data/',
                 view_func=Data.as_view('data'),
                  methods=["GET", "POST"])

@app.route('/contactme/')

def contactme():
    return render_template('form_submit.html')



@app.route('/thankyou/', methods=['POST'])
def thankyou():
    name=request.form['yourname']
    email=request.form['youremail']
    message=request.form['message']
    return render_template('form_action.html', name=name, email=email, message=message)


if __name__ == "__main__":
 app.run( host ='0.0.0.0', debug = True )
 


