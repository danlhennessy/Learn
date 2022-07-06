from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'Username': 'Danec'}
    return '''
    <html>
        <head>
            <title>Home Page - Flasked</title>
        </head>
        <body>
            <h1>Hello, ''' + user['Username'] + '''!</h1>
        </body>
    </html>
    '''
