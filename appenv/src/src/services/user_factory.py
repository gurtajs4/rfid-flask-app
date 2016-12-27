from ..db import SqliteManager as dbm
from ..models.models import User


def create_user(tag_id=0, first_name="", last_name="", pic_url=None):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('''INSERT OR IGNORE INTO User (tag_id, first_name, last_name, pic_url)
            VALUES ( ?, ?, ?, ? )''', (tag_id, first_name, last_name, pic_url,))
    db.commit()
    cur.execute('SELECT id FROM User WHERE tag_id = ? ', (tag_id,))
    user_id = cur.fetchone()[0]
    dbm.close_connection(db)
    return User(user_id=user_id, tag_id=tag_id, first_name=first_name, last_name=last_name, pic_url=pic_url)


def get_users(limit=0):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM User')
    results = cur.fetchall() if limit == 0 else cur.fetchmany(size=limit)
    users = []
    for res in results:
        users.append(User(res[0], res[1], res[2], res[3], res[4]))
    dbm.close_connection(db)
    return users


def get_user(user_id=None, tag_id=None, first_name=None, last_name=None, pic_url=None):
    if user_id is not None and tag_id is not None and first_name is not None and last_name is not None:
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [user_id, tag_id, first_name, last_name] if p is not None])
        sql_command = 'SELECT * FROM User WHERE ' + 'id = ? ' if user_id is not None else ''
        + 'tag_id = ? ' if tag_id is not None else '' + 'first_name = ? ' if first_name is not None else ''
        + 'last_name = ? ' if last_name is not None else '' + 'pic_url = ? ' if pic_url is not None else ''
        cur.execute(sql=sql_command, parameters=params)
        result = cur.fetchone()
        user = User(user_id=result[0], tag_id=result[1], first_name=result[2], last_name=result[3],
                    pic_url=result[4])
        dbm.close_connection(db)
        return user
    else:
        return None
