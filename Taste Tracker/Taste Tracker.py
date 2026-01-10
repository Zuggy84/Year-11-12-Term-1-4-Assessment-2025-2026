from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    Taste_Tracker_Home_Page='''
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/css/Taste Tracker Home Page.css">
            <title>Taste Tracker Home Page</title>
        </head>
        <body>
            <hr>
            <div style="margin: 20px; border: 2px solid grey; padding: 2px">
                <div style="border: 2px solid grey; padding: 10px">
                    <h1>Welcome To Taste Tracker!</h1>
                    <h2>View And Share Reviews About Restaurants <span style="color: red">A<span style="color: orange">L<span style="color: yellow">L <span style="color: green">A<span style="color: blue">C<span style="color: purple">R<span style="color: red">O<span style="color: orange">S<span style="color: yellow">S <span style="color: green">T<span style="color: blue">O<span style="color: purple">W<span style="color: red">N<span style="color: orange">!</h2>
                </div>
            </div>
            <hr>
            <div style="margin: 20px; border: 2px solid grey; padding: 2px">
                <div style="border:2px solid grey; padding: 10px">
                    <h2>Navigate Taste Tracker:</h2>
                    <br>
                    <div class="container">
                        <a href="/reviews">Reviews Page</a>
                    </div>
                    <div class="container">
                        <a href="/credits">Credits Page</a>
                    </div>
                    <hr>
                    <h1>OR</h1>
                    <hr>
                </div>
            </div>
            <hr>
        </body>
    </html>
    '''
    return Taste_Tracker_Home_Page
@app.route('/reviews')
def reviews():
    Taste_Tracker_Reviews_Page='''
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/css/Taste Tracker Reviews Page.css">
            <title>Taste Tracker Reviews Page</title>
        </head>
        <body>
            <hr>
            <div style="margin: 20px; border: 2px solid grey; padding: 2px">
                <div style="border: 2px solid grey; padding: 10px">
                    <h1>Taste Tracker Reviews Page</h1>
                </div>
            </div>
            <hr>
        </body>
    </html>
    '''
    return Taste_Tracker_Reviews_Page
@app.route('/credits')
def credits():
    Taste_Tracker_Credits_Page='''
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="/static/css/Taste Tracker Credits Page.css">
            <title>Taste Tracker Credits Page</title>
        </head>
        <body>
            <hr>
            <div style="margin: 20px; border: 2px solid grey; padding: 2px">
                <div style="border: 2px solid grey; padding: 10px">
                    <h1>Taste Tracker Credits Page</h1>
                </div>
            </div>
            <hr>
        </body>
    </html>'''
app.run(debug=True, reloader_type='stat', port=5000)