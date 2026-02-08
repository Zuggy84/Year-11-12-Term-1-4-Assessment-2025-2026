from flask import Flask, render_template
from sqlalchemy import create_engine, text
app=Flask(__name__)
engine=create_engine('sqlite:///Taste Tracker.db')
connection=engine.connect()
@app.route('/')
def home():
    return render_template('Taste Tracker Home Page.html')
@app.route('/reviews')
def reviews():
    query=text('SELECT * FROM reviews')
    result=connection.execute(query).fetchall()
    return render_template('Taste Tracker Reviews Page.html', reviews=result)
@app.route('/credits')
def credits():
    return render_template('Taste Tracker Credits Page.html')
app.run(debug=True, reloader_type='stat', port=5000)