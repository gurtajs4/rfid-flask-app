import datetime
from ..db import SqliteManager as dbm
from ..models.models import Session


def create_session(user_id=0, key_id=0, timestamp=datetime.datetime.now()):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('''INSERT OR IGNORE INTO Session (user_id, key_id, timestamp)
            VALUES ( ?, ?, ? )''', (user_id, key_id, timestamp,))
    db.commit()
    cur.execute('SELECT id FROM Session WHERE key_id = ? AND user_id = ? ', (key_id, user_id,))
    session_id = cur.fetchone()[0]
    dbm.close_connection(db)
    return Session(session_id=session_id, key_id=key_id, user_id=user_id, timestamp=timestamp)


def get_sessions(limit=0):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM Session')
    results = cur.fetchall() if limit == 0 else cur.fetchmany(size=limit)
    sessions = [Session(res[0], res[1], res[2], res[3]) for res in results]
    dbm.close_connection(db)
    return sessions


def get_session(session_id=None, user_id=None, key_id=None, timestamp=None):
    if session_id is not None and user_id is not None and key_id is not None and timestamp is not None:
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [session_id, user_id, key_id, timestamp] if p is not None])
        sql_command = 'SELECT * FROM Session WHERE ' + 'id = ? ' if session_id is not None else ''
        + 'user_id = ? ' if user_id is not None else '' + 'key_id = ? ' if key_id is not None else ''
        + 'timestamp = ? ' if timestamp is not None else ''
        cur.execute(sql=sql_command, parameters=params)
        result = cur.fetchone()
        session = Session(session_id=result[0], key_id=result[1], user_id=result[2], timestamp=result[3])
        dbm.close_connection(db)
        return session
    else:
        return None
