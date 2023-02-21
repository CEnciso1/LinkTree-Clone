from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder="templates")
app.config.from_pyfile('config.py')

mysql = MySQL(app)



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     #Creating a connection cursor
#     cursor = mysql.connection.cursor()

#     #Executing SQL Statements
#     cursor.execute('CREATE TABLE haha (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);')
 
#     #Saving the Actions performed on the DB
#     mysql.connection.commit()
 
#     #Closing the cursor
#     cursor.close()

#     return 'Success'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signUp():
    return render_template('signup.html')

if __name__ == '__main__': # With this can create app file instead of python -m flask run
       app.run()
