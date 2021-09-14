from flask import Flask, redirect, render_template, request,url_for, jsonify
import pymysql
import json
from compare import compare_info
com = compare_info()
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Kyotsuu5@18.222.210.94/Docomo_Hackathon?charset=utf8'
# db = SQLAlchemy(app)
# engine = create_engine('mysql+pymysql://root:Kyotsuu5@18.222.210.94/Docomo_Hackathon?charset=utf8')
def getConnection():
    connection = pymysql.connect(
    host="localhost",
    db="hackathon",
    user="root",
    password="Kyotsuu5",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
    return connection

# class DATABASENAME(db.Model):
#   __tablename__ = 'DATABASENAME'
@app.route('/<username>/logingin', methods = ['GET', 'POST'])
def login(username):
    connection = getConnection()
    myusername = request.form["username"]
    common, not_common = com.compare(myusername,username)
    # sql = "SELECT * FROM user where usename=%s"
    # cursor = connection.cursor()
    # cursor.execute(sql,(username))
    # user = cursor.fetchall()
    # name = cursor.fetchall()
    render_template('kojin.html', name = username, kyotsus=common, hikyoutsuus=not_common)

@app.route('/')
def redirect_share_login():
    return render_template('login.html')
@app.route('/<username>/login')
def redirect_login(username):
    return render_template('login.html')

@app.route('/login')
def return_login():
    return render_template('login.html')

@app.route('/logingin', methods = ['GET', 'POST'])
def index():
    print("connected")
    connection = getConnection()
    username=request.form["username"]
    password=request.form["password"]
    
    print(username)
    print(password)
    # sql = "SELECT password FROM user where usename=%s AND password = %s"
    # cursor = connection.cursor()
    # cursor.execute(sql,(username,password))
    # passw = cursor.fetchall()
    sql = "SELECT * FROM user where usename=%s AND password=%s"
    cursor = connection.cursor()
    print(sql)
    cursor.execute(sql,(username,password))
    user = cursor.fetchall()
    exist = len(cursor.fetchall())
    cursor.close()
    connection.close()
    # print(passw)
    print(user)
    user_info=user[0]
    print(user_info)
    user_info['share_url']="http://ec2-18-222-210-94.us-east-2.compute.amazonaws.com:5000/"  + user_info["usename"] + "/login"
    print((user))
    # del user['enter_date']
    if(len(user)!=0):
        return render_template('mypage.html', users = user_info)
    else:
        return render_template('login.html')

        # return redirect(url_for('return_login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.debug = True

