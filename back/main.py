from flask import Flask, redirect, render_template, request,url_for
import pymysql

app = Flask(__name__)
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
@app.route('/<username>', methods = ['GET', 'POST'])
def login(username):
    connection = getConnection()
    sql = "SELECT name FROM user WHERE usename ={}".format(username)
    cursor = connection.cursor()
    cursor.execute(sql)
    user = cursor.fetchall()
    name = cursor.fetchall()
    common = {
        'koumokumei':koumokumei,
        'setsumei':setumeibun
    }
    uncommon = {
        'koumokumei':koumokumei,
        'setsumei':setumeibun
    }
    render_template('kojin.html', name=name, kyotsus=common, hikyoutsuus=uncommon)

@app.route('/')
def redirect_login():
    return render_template('login.html')

@app.route('/login')
def return_login():
    return redirect(url_for('return_login'))

@app.route('/logingin', methods = ['GET', 'POST'])
def index():
    print("connected")
    connection = getConnection()
    username=request.form["username"]
    password=request.form["password"]
    print(username)
    # sql = "SELECT password FROM user where usename=%s AND password = %s"
    # cursor = connection.cursor()
    # cursor.execute(sql,(username,password))
    # passw = cursor.fetchall()
    sql = "SELECT * FROM user where usename=%s AND password = %s"
    cursor = connection.cursor()
    cursor.execute(sql,(username,password))
    user = cursor.fetchall()
    exist = len(cursor.fetchall())
    cursor.close()
    connection.close()
    # print(passw)
    print(user)
    print(exist)
    if(exist!=0):
        return render_template('mypage.html', users = user)
    else:
        return redirect(url_for('return_login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
