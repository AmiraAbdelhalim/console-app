# imports
import MySQLdb
import env


db = MySQLdb.connect(env.HOST, env.DBUSER, env.DBPASSWORD, env.DBNAME)


def create_project(user_id, title, details, total_target, start_date, end_date):
    insert_sql = """insert into projects (user_id, title, details, total_target, start_date, end_date) 
    values (%s, %s, %s, %s, %s, %s);"""
    data = (user_id, title, details, total_target, start_date, end_date)
    cursor = db.cursor()
    try:
        cursor.execute(insert_sql, data)
        db.commit()
        return True
    except:
        db.rollback()
        return False
    finally:
        cursor.close()


def get_all_projects():
    select_sql = """select * from projects;"""
    cursor = db.cursor()
    try:
        cursor.execute(select_sql)
        all_projects = cursor.fetchall()
        return all_projects
    except:
        db.rollback()
        return None
    finally:
        cursor.close()


def get_project_by_title(title):
    select_sql = f'select title, details, total_target, start_date, end_date from projects where title={title}'
    cursor = db.cursor()
    try:
        cursor.execute(select_sql)
        project = cursor.fetchone()
        return project
    except:
        db.rollback()
        return None
    finally:
        cursor.close()


def delete_project(user_id, title):
    delete_sql = f'delete from projects where user_id=%s and title=%s;'

    cursor = db.cursor()
    try:
        cursor.execute(delete_sql, (user_id, title))
        db.commit()
        return True
    except:
        db.rollback()
        return False
    finally:
        cursor.close()

