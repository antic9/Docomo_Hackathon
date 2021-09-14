from flask import Flask, redirect, render_template, request
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

@app.route('/', methods = ['GET', 'POST'])
def index():
    print("connected")
    connection = getConnection()
    message = "Successfully Connected to SQL"

    sql = "SELECT * FROM user"
    cursor = connection.cursor()
    cursor.execute(sql)
    user = cursor.fetchall()

    cursor.close()
    connection.close()
    return render_template('index_test_flask_base.html', message = message, users = user)