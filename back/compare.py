# import sqlite3, pymysql

######## make demo data ########
# connection = sqlite3.connect('./test.db')
# connection.row_factory = sqlite3.Row
# cursor = connection.cursor()
# cursor.execute("DROP TABLE user")
# cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, name TEXT, birthplace TEXT, hobby1 TEXT, hobby2 TEXT, hobby3 TEXT)")
# persons = [(1, 'takahashi', '高橋芳樹', '滋賀県', '車', 'キャンプ', 'demo'), (2, 'tanaka', '田中百合', '滋賀県', 'キャンプ', '車', 'demo1'), (3, 'demo', 'デモ', 'demo', 'demo', 'demo', 'demo')]
# cursor.executemany("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?)", persons)
################################

import re

def compare(username1, username2, connection):
  common = {}
  not_common = {}
  common_hb = []
  not_common_hb = []

  usernames = [username1, username2]
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM user WHERE username=? OR username=?", usernames)
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

  return common, not_common

######## usage ########
# a, b = compare('takahashi', 'tanaka', connection)

######## result ########
# print(a)
# > {'birthplace': '滋賀県', 'hobby': ['キャンプ', '車']}
# print(b)
# > {'id': 2, 'username': 'tanaka', 'name': '田中百合', 'hobby': ['demo1']}