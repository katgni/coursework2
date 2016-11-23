from flask import Flask, request, render_template, url_for,g, redirect, session, flash
from functools import wraps

import sqlite3

app = Flask(__name__)

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


    return render_template('form.html', msg=msg)

if __name__ == "__main__":
 app.run( host ='0.0.0.0', debug = True)

