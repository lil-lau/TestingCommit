import sqlite3 as sql
import crypt
import logging as f

conn = sql.connect('seenit.db')
c = conn.cursor()
salt = '2y'

# register-insert new user
def insert(id, name, email, pwd):
    h_pwd = crypt.crypt(pwd,salt)
    query = "INSERT INTO user (u_id, u_name, pwd, email) VALUES (" + str(id) + ",'" + name + "','" + h_pwd + "','" + email + "')"
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("insert user successfully\n")
            print ("insert successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("insert user error\n")
            print ("insert error")

def read_one(u_id):
    query = "SELECT * FROM user WHERE u_id=" + str(u_id)
    with conn:
        try:
            c.execute(query)
            users = c.fetchall()
            user_info = users[0]
            f.writing("read one user successfully\n")
            print ("User Info read successfully")
            return user_info
        except:
            f.writing("read one user error\n")
            print("User Info read error")

# login-get user id with name and password input
def login(name, pwd):
    h_pwd = crypt.crypt(pwd,salt)
    query = "SELECT u_id FROM user WHERE u_name='" + name + "'AND pwd='" + h_pwd + "'"
    with conn:
        try:
            c.execute(query)
            users = c.fetchall()
            _id = users[0][0]
            f.writing("login successfully\n")
            print ("login successfully")
            return _id
        except:
            f.writing("login error\n")
            print("login error")

# admin delete account
def delete(id):
    query = "DELETE FROM user WHERE u_id=" + str(id)
    # print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("delete user successfully\n")
            print ("delete successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("delete error\n")
            print ("delete error")

# get all users
def read_all():
    with conn:
        try:
            c.execute('SELECT * FROM user')
            users = c.fetchall()
            f.writing("read all users successfully\n")
            print ("read successfully")
            return users
        except:
            f.writing("read all users error\n")
            print("read error")

# update account info
def update(id, name, pwd, email):
    h_pwd = crypt.crypt(pwd,salt)
    query = "UPDATE user SET u_name='" + name + "', pwd='" + h_pwd + "', email='" + email + "' WHERE u_id=" + str(id)
    print (query)
    with conn:
        try:
            c.execute(query)
            f.writing("update user successfully\n")
            print ("update successfully")
            conn.commit()
        except:
            conn.rollback()
            f.writing("update user error\n")
            print ("update error")

# insert(7,'b','b@email')