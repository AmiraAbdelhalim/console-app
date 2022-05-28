# imports
import MySQLdb
import env


db = MySQLdb.connect(env.HOST, env.DBUSER, env.DBPASSWORD, env.DBNAME)


# create user table
def create_user(first_name, last_name, email, password, confirmation_password, mobile_phone):
    user = """insert into users (first_name, last_name, email, password, confirm_password, mobile_phone) 
    values (%s, %s, %s, %s, %s, %s);"""
    data = (first_name, last_name, email, password, confirmation_password, mobile_phone)
    cursor = db.cursor()
    try:
        cursor.execute(user, data)
        db.commit()
        print(cursor.fetchone())
        return True
    except:
        db.rollback()
        return False
    finally:
        cursor.close()


# get one user
def find_user(email, password):
    """
    for login
    :return:
    """
    retrieve_user = f'select * from users where email=%s and password=%s;'
    cursor = db.cursor()
    try:
        cursor.execute(retrieve_user, (email, password))
        user = cursor.fetchone()
        return user
    except:
        db.rollback()
        return None
    finally:
        cursor.close()
