import datetime, TimeHelper
from DBHandler import *
import Constants

#delete user by username
def delete_user(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    sql = "DELETE FROM followed_users WHERE username = '{0}'".format(username)
    cursor.execute(sql)
    mydb.commit()


#add new username
def add_user(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, date_added) VALUES(%s,%s)",(username, now))
    mydb.commit()


#check if any user qualifies to be unfollowed
def check_unfollow_list():

    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    users_to_unfollow = []
    for r in results:
        date = datetime.datetime.strptime(r[2], '%Y-%m-%d').date()
        d = (datetime.datetime.now().date()-date).days
        print(d)
        if d >= Constants.DAYS_TO_UNFOLLOW:
            users_to_unfollow.append(r[1])
    return users_to_unfollow


#get all followed users
def get_followed_users():
    users = []
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    for r in results:
        users.append(r[0])

    return users