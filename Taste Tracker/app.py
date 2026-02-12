from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from werkzeug.security import generate_password_hash, check_password_hash
app=Flask(__name__)
engine=create_engine('sqlite:///Taste Tracker.db')
connection=engine.connect()
user_logged_in=False
@app.route('/')
def home():
    if user_logged_in==True:
        return render_template('Taste Tracker Home Page.html', user_logged_in=user_logged_in)
    else:
        return render_template('Taste Tracker Home Page.html')
@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method=='POST':
        restaurant_name=request.form['restaurant_name']
        cuisine_type=request.form['cuisine_type']
        restaurant_rating=request.form['restaurant_rating']
        restaurant_review_text=request.form['restaurant_review_text']
        query=text('INSERT INTO reviews (restaurant_name, cuisine_type, restaurant_rating, restaurant_review_text) VALUES (:restaurant_name, :cuisine_type, :restaurant_rating, :restaurant_review_text);')
        connection.execute(query, {'restaurant_name': restaurant_name, 'cuisine_type': cuisine_type, 'restaurant_rating': restaurant_rating, 'restaurant_review_text': restaurant_review_text})
        connection.commit()
        query=text('SELECT * FROM reviews;')
        result=connection.execute(query).fetchall()
        user_logged_in=True
        return render_template('Taste Tracker Reviews Page.html', reviews=result, user_logged_in=user_logged_in)
    else:
        query=text('SELECT * FROM reviews;')
        result=connection.execute(query).fetchall()
        return render_template('Taste Tracker Reviews Page.html', reviews=result)
@app.route('/credits')
def credits():
    if user_logged_in==True:
        return render_template('Taste Tracker Credits Page.html', user_logged_in=user_logged_in)
    else:
        return render_template('Taste Tracker Credits Page.html')
@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method=='POST':
        user_name=request.form['user_name']
        user_email=request.form['user_email']
        user_password=request.form['user_password']
        user_password_hash=generate_password_hash(user_password)
        query=text('INSERT INTO users (user_name, user_email, user_password, user_password_hash) VALUES (:user_name, :user_email, :user_password, :user_password_hash);')
        connection.execute(query, {'user_name': user_name, 'user_email': user_email, 'user_password': user_password, 'user_password_hash': user_password_hash})
        connection.commit()
        user_logged_in=True
        return render_template('Taste Tracker Reviews Page.html', user_logged_in=user_logged_in)
    else:
        return render_template('Taste Tracker Sign Up Page.html')
@app.route('/logIn', methods=['GET', 'POST'])
def logIn():
    if request.method=='POST':
        user_email=request.form['user_email']
        user_password=request.form['user_password']
        query=text('SELECT user_password FROM users WHERE user_email = :user_email;')
        result=connection.execute(query, {'user_email': user_email}).fetchone()
        if result:
            fetched_password=result[0]
            if fetched_password==user_password:
                user_logged_in=True
                return render_template('Taste Tracker Reviews Page.html', user_logged_in=user_logged_in)
            else:
                user_not_logged_in=True
                return render_template('Taste Tracker Log In Page.html', user_not_logged_in=user_not_logged_in)  
    else:
        return render_template('Taste Tracker Log In Page.html')
if __name__=='__main__':
    app.run(debug=True, reloader_type='stat', port=5000)