from ..db import SqliteManager as dbm
from ..models.models import User


def create_user(tag_id, first_name="", last_name="", email="", role_id=1, pic_id=1):
    if None is tag_id:
        return None
    db = dbm.get_db()
    cur = db.cursor()
    affected_count = cur.execute('''INSERT OR REPLACE INTO User (tag_id, first_name, last_name, email, role_id, pic_id)
                VALUES ( ?, ?, ?, ?, ?, ? )''', (tag_id, first_name, last_name, email, role_id, pic_id,))
    db.commit()
    if affected_count > 0:
        cur.execute(
            'SELECT id FROM User WHERE tag_id = ? AND first_name = ? AND last_name = ? AND email = ? AND role_id = ? AND pic_id = ?',
            (tag_id, first_name, last_name, email, role_id, pic_id,))
        result = cur.fetchone()
        user_id = int(result[0])
        dbm.close_connection(db)
        return User(user_id=user_id, tag_id=tag_id, first_name=first_name, last_name=last_name, email=email,
                    role_id=role_id, pic_id=pic_id)
    else:
        dbm.close_connection(db)
        return None


def get_users(limit=0):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM User')
    results = cur.fetchall() if limit == 0 else cur.fetchmany(size=limit)
    users = [User(res[0], res[1], res[2], res[3], res[4], res[5], res[6]) for res in results]
    dbm.close_connection(db)
    return users


def search_user(user_id=None, tag_id=None, first_name=None, last_name=None, email=None, role_id=1, pic_id=1, limit=1,
                exclusive=False):
    if not (user_id is None and tag_id is None and first_name is None and last_name is None):
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [user_id, tag_id, first_name, last_name, role_id, pic_id] if p is not None])
        condition_operator = ' AND ' if exclusive else ' OR '
        sql_conditions = condition_operator.join(filter(
            lambda x: x is not '', ['id = ? ' if user_id is not None else '',
                                    'tag_id = ? ' if tag_id is not None else '',
                                    'first_name = ? ' if first_name is not None else '',
                                    'last_name = ? ' if last_name is not None else '',
                                    'role_id = ? ' if role_id is not None else '',
                                    'pic_id = ? ' if pic_id is not None else '']))
        sql_command = 'SELECT * FROM User WHERE ' + sql_conditions
        cur.execute(sql_command, params)
        results = [cur.fetchone()] if limit == 1 else cur.fetchall()
        dbm.close_connection(db)
        if None is results or 0 == len(results):
            return None
        users = []
        if len(results) > 1:
            users = [User(res[0], res[1], res[2], res[3], res[4], res[5], res[6]) for res in results]
        else:
            users[0] = User(results[0], results[1], results[2], results[3], results[4], results[5], results[6])
        return users[0] if limit == 1 else users
    else:
        return None


def delete_user(user_id, delete_history=False):
    if None is not user_id:
        db = dbm.get_db()
        cur = db.cursor()
        params = (user_id,)
        # delete user
        sql_command = 'DELETE FROM User WHERE id = ? '
        cur.execute(sql_command, params)
        db.commit()
        # check if user deleted
        sql_command = 'SELECT * FROM User WHERE id = ? '
        cur.execute(sql_command, params)
        result = cur.fetchone()
        # delete all sessions where user_id matches selected user
        linked_sessions = None
        if True == delete_history:
            sql_command = 'DELETE FROM Session WHERE user_id = ? '
            cur.execute(sql_command, params)
            db.commit()
            # check if matched sessions deleted
            sql_command = 'SELECT * FROM Session WHERE user_id = ? '
            cur.execute(sql_command, params)
            linked_sessions = cur.fetchall()
        dbm.close_connection(db)
        return None is result and None is linked_sessions
    else:
        return False


def update_user(user_id, tag_id=None, first_name=None, last_name=None, email=None, role_id=1, pic_id=1):
    if not (tag_id is None and first_name is None and email is None and last_name is None) and user_id is not None:
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [tag_id, first_name, last_name, email, role_id, pic_id] if p is not None])
        updates_separator = ' , '
        sql_updates = updates_separator.join(filter(
            lambda x, y: x is not '', ['tag_id = ? ' if tag_id is not None else '',
                                       'first_name = ? ' if first_name is not None else '',
                                       'last_name = ? ' if last_name is not None else '',
                                       'email = ? ' if email is not None else '',
                                       'role_id = ? ' if role_id is not None else '',
                                       'pic_id = ? ' if pic_id is not None else '']))
        # update user
        sql_command = 'UPDATE User SET' + sql_updates + 'WHERE id = ?'
        params += (user_id,)
        params *= 2
        cur.execute(sql_command, params)
        db.commit()
        # return updated user
        sql_command = 'SELECT * FROM User WHERE id = ? LIMIT 1 '
        cur.execute(sql_command, (user_id,))
        result = cur.fetchone()
        user = User(user_id=result[0], tag_id=result[1], first_name=result[2], last_name=result[3], email=result[4],
                    role_id=result[5], pic_id=result[6])
        dbm.close_connection(db)
        return user
    else:
        return None
