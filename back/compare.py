# import sqlite3, pymysql

######## make demo data ########
# connection = sqlite3.connect('./test.db')
# connection.row_factory = sqlite3.Row
# cursor = connection.cursor()
# cursor.execute("DROP TABLE user")
# cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, usename TEXT, name TEXT, birthplace TEXT, hobby1 TEXT, hobby2 TEXT, hobby3 TEXT)")
# persons = [(1, 'takahashi', '高橋芳樹', '滋賀県', '車', 'キャンプ', 'demo'), (2, 'tanaka', '田中百合', '滋賀県', 'キャンプ', '車', 'demo1'), (3, 'demo', 'デモ', 'demo', 'demo', 'demo', 'demo')]
# cursor.executemany("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?)", persons)
################################
from flask import Flask, redirect, render_template, request,url_for, jsonify
import pymysql
import json
import re
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
class compare_info:
  def MakeCommonInfoSentence(common, username2):
    kyotsu = {"koumokumei":{},"setsumei":{}}
    birthplace = common.get("birthplace")
    job = common.get("job")
    university = common.get("university")
    c_prefecture = common.get("c_prefecture")
    visit = common.get("visit")
    recent_shopping = common.get("recent_shopping")
    fav_food = common.get("fav_food")
    fav_movie = common.get("fav_movie")
    fav_anime = common.get("fav_anime")
    hobby = common.get("hobby")

    if(birthplace):
        kyotsu["koumokumei"]["birthplace"] = birthplace
        kyotsu["setsumei"]["birthplace"] = username2 + "さんも" + birthplace + "出身のようです。「学部・学科はどこでしたか？」「サークルはどこですか？」"
    if(job):
        kyotsu["koumokumei"]["job"] = job
        kyotsu["setsumei"]["job"] = username2 + "さんも" + job + "をされているようです。「最近あった面白い仕事は？」「今何年目？」"
    if(university):
        kyotsu["koumokumei"]["university"] = university
        kyotsu["setsumei"]["university"] = username2 + "さんも" + university + "出身のようです。「学部・学科はどこでしたか？」「サークルはどこですか？」"
    if(c_prefecture):
        kyotsu["koumokumei"]["c_prefecture"] = c_prefecture
        kyotsu["setsumei"]["c_prefecture"] = username2 + "さんも" + c_prefecture + "に住んでいるようです。「" + c_prefecture + "の遊び場といえば？」「" + c_prefecture + "に住んでいて困ることは？」"
    if(visit):
        kyotsu["koumokumei"]["visit"] = visit
        kyotsu["setsumei"]["visit"] = username2 + "さんも" + visit + "に最近行ったようです。「" + visit + "の名産といえば？」「" + visit + "のどこを観光しましたか？」"
    if(recent_shopping):
        kyotsu["koumokumei"]["recent_shopping"] = recent_shopping
        kyotsu["setsumei"]["recent_shopping"] = username2 + "も最近" + recent_shopping + "を買ったようです。「" + recent_shopping + "をどうして買いましたか？」「" + recent_shopping + "の良さは？」"
    if(fav_food):
        kyotsu["koumokumei"]["fav_food"] = fav_food
        kyotsu["setsumei"]["fav_food"] = username2 + "さんも" + fav_food + "が好きなようです。「" + fav_food + "が好きな理由は？」「いつから好きですか？」"
    if(fav_movie):
        kyotsu["koumokumei"]["fav_movie"] = fav_movie
        kyotsu["setsumei"]["fav_movie"] = username2 + "さんも" + fav_movie + "の映画が好きなようです。「" + fav_movie + "が好きな理由は？」「いつから好きですか？」"
    if(fav_anime):
        kyotsu["koumokumei"]["fav_anime"] = fav_anime
        kyotsu["setsumei"]["fav_anime"] = username2 + "さんも" + fav_anime + "のアニメが好きなようです。「" + fav_anime + "が好きな理由は？」「いつから好きですか？」"
    if(len(hobby)):
        kyotsu["setsumei"]["hobby"]=[]
        for i in range(len(hobby)):
            kyotsu["setsumei"]["hobby"].append(username2 + "さんも" + hobby[i] + "が好きなようです。「" + hobby[i] + "が好きな理由は？」「いつから好きですか？」「最近いつしましたか？」")
    return kyotsu
  def MakeUnCommonInfoSentence(not_common, username2):
    kyotsu = {"koumokumei":{},"setsumei":{}}
    birthplace = not_common.get("birthplace")
    job = not_common.get("job")
    university = not_common.get("university")
    c_prefecture = not_common.get("c_prefecture")
    visit = not_common.get("visit")
    recent_shopping = not_common.get("recent_shopping")
    fav_food = not_common.get("fav_food")
    fav_movie = not_common.get("fav_movie")
    fav_anime = not_common.get("fav_anime")
    hobby = not_common.get("hobby")

    if(birthplace):
        kyotsu["koumokumei"]["birthplace"] = birthplace
        kyotsu["setsumei"]["birthplace"] = username2 + "さんは" + birthplace + "出身のようです。「学部・学科はどこでしたか？」「サークルはどこですか？」"
    if(job):
        kyotsu["koumokumei"]["job"] = job
        kyotsu["setsumei"]["job"] = username2 + "さんは" + job + "をされているようです。「最近あった面白い仕事は？」「今何年目？」"
    if(university):
        kyotsu["koumokumei"]["university"] = university
        kyotsu["setsumei"]["university"] = username2 + "さんは" + university + "出身のようです。「学部・学科はどこでしたか？」「サークルはどこですか？」"
    if(c_prefecture):
        kyotsu["koumokumei"]["c_prefecture"] = c_prefecture
        kyotsu["setsumei"]["c_prefecture"] = username2 + "さんは" + c_prefecture + "に住んでいるようです。「" + c_prefecture + "の遊び場といえば？」「" + c_prefecture + "に住んでいて困ることは？」"
    if(visit):
        kyotsu["koumokumei"]["visit"] = visit
        kyotsu["setsumei"]["visit"] = username2 + "さんは" + visit + "に最近行ったようです。「" + visit + "の名産といえば？」「" + visit + "のどこを観光しましたか？」"
    if(recent_shopping):
        kyotsu["koumokumei"]["recent_shopping"] = recent_shopping
        kyotsu["setsumei"]["recent_shopping"] = username2 + "も最近" + recent_shopping + "を買ったようです。「" + recent_shopping + "をどうして買いましたか？」「" + recent_shopping + "の良さは？」"
    if(fav_food):
        kyotsu["koumokumei"]["fav_food"] = fav_food
        kyotsu["setsumei"]["fav_food"] = username2 + "さんは" + fav_food + "が好きなようです。「" + fav_food + "が好きな理由は？」「いつから好きですか？」"
    if(fav_movie):
        kyotsu["koumokumei"]["fav_movie"] = fav_movie
        kyotsu["setsumei"]["fav_movie"] = username2 + "さんは" + fav_movie + "の映画が好きなようです。「" + fav_movie + "が好きな理由は？」「いつから好きですか？」"
    if(fav_anime):
        kyotsu["koumokumei"]["fav_anime"] = fav_anime
        kyotsu["setsumei"]["fav_anime"] = username2 + "さんは" + fav_anime + "のアニメが好きなようです。「" + fav_anime + "が好きな理由は？」「いつから好きですか？」"
    if(len(hobby)):
        kyotsu["setsumei"]["hobby"]=[]
        for i in range(len(hobby)):
            kyotsu["setsumei"]["hobby"].append(username2 + "さんは" + hobby[i] + "が好きなようです。「" + hobby[i] + "が好きな理由は？」「いつから好きですか？」「最近いつしましたか？」")
    return kyotsu
  def compare(self, username1, username2):
    common = {}
    not_common = {}
    common_hb = []
    not_common_hb = []

    usernames = [username1, username2]
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user WHERE usename=? OR usename=?", usernames)
    user = cursor.fetchall()
    cursor.close()

    for i in range(len(user[1])):

      # hobby
      if re.compile(r'^hobby').search(user[1].keys()[i]):
        b_len = len(common_hb)
        for j in range(len(user[0])):
          if re.compile(r'^hobby').search(user[0].keys()[j]):
            if user[1][i] == user[0][j]:
              common_hb.append(user[0][j])

        if len(common_hb) == b_len:
          not_common_hb.append(user[1][i])

      # other
      else:
        if user[1][i] == user[0][i]:
          common[user[0].keys()[i]] = user[0][i]
        else:
          not_common[user[0].keys()[i]] = user[1][i]

    common['hobby'] = common_hb
    not_common['hobby'] = not_common_hb

    return self.MakeCommonInfoSentence(common, username2), self.MakeUnCommonInfoSentence(not_common, username2)

  ######## usage ########
  # a, b = compare('takahashi', 'tanaka', connection)

  ######## result ########
  # print(a)
  # > {'birthplace': '滋賀県', 'hobby': ['キャンプ', '車']}
  # print(b)
  # > {'id': 2, 'username': 'tanaka', 'name': '田中百合', 'hobby': ['demo1']}