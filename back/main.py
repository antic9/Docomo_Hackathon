from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

dns = {
    'user': 'root',
    'host': '18.222.210.94', # 各自設定
    'port':'3306',
    'password': 'Kyotsuu5', # 各自設定
    'database': 'Docomo_Hackathon' # 各自設定
}


class DATABASENAME(db.Model):
  __tablename__ = 'DATABASENAME'

@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index_test_flask_base.html')
  else:
    return redirect('/')

@app.route('/login')
def login():
  return redirect('/')

@app.route('/mypage')
def mypage():
  return redirect('/')

@app.route('personal_page')
def personal_page():
  return redirect('/')


