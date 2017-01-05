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


def search_session(session_id=None, user_id=None, key_id=None, timestamp=None, limit=1):
    if not (session_id is None and user_id is None and key_id is None and timestamp is None):
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [session_id, user_id, key_id, timestamp] if p is not None])
        condition_operator = ' AND ' if limit == 1 else ' OR '
        sql_conditions = condition_operator.join(filter(
            lambda x: x is not '', [' id = ? ' if session_id is not None else '',
                                    ' user_id = ? ' if user_id is not None else '',
                                    ' key_id = ? ' if key_id is not None else '',
                                    ' timestamp = ? ' if timestamp is not None else '']))
        sql_command = 'SELECT * FROM Session WHERE ' + sql_conditions
        cur.execute(sql=sql_command, parameters=params)
        results = cur.fetchone() if limit == 1 else cur.fetchall()
        sessions = []
        for result in results:
            session = Session(session_id=result[0], key_id=result[1], user_id=result[2], timestamp=result[3])
            sessions.append(session)
        dbm.close_connection(db)
        return sessions[0] if limit == 1 else sessions
    else:
        return None


def delete_session(session_id=None, user_id=None, key_id=None, timestamp=None):
    if not (session_id is None and user_id is None and key_id is None and timestamp is None):
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [session_id, user_id, key_id, timestamp] if p is not None])
        sql_conditions = ' AND '.join(filter(
            lambda x: x is not '', [' id = ? ' if session_id is not None else '',
                                    ' user_id = ? ' if user_id is not None else '',
                                    ' key_id = ? ' if key_id is not None else '',
                                    ' timestamp = ? ' if timestamp is not None else '']))
        # delete session
        sql_command = 'DELETE FROM Session WHERE ' + sql_conditions
        cur.execute(sql=sql_command, parameters=params)
        db.commit()
        # check if session deleted
        sql_command = 'SELECT * FROM Session WHERE ' + sql_conditions + ' LIMIT 1 '
        cur.execute(sql=sql_command, parameters=params)
        result = cur.fetchone()
        dbm.close_connection(db)
        return None is result
    else:
        return None


def update_session(session_id, user_id=None, key_id=None, timestamp=None):
    if not (user_id is None and key_id is None and timestamp is None) and session_id is not None:
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [session_id, user_id, key_id, timestamp] if p is not None])
        sql_updates = ' AND '.join(filter(
            lambda x: x is not '', [' id = ? ' if session_id is not None else '',
                                    ' user_id = ? ' if user_id is not None else '',
                                    ' key_id = ? ' if key_id is not None else '',
                                    ' timestamp = ? ' if timestamp is not None else '']))
        # update session
        sql_command = 'UPDATE Session SET ' + sql_updates + ' WHERE id = ? '
        params += (session_id,)
        cur.execute(sql=sql_command, parameters=params)
        db.commit()
        # return updated session
        sql_command = 'SELECT * FROM Session WHERE id = ? LIMIT 1 '
        cur.execute(sql=sql_command, parameters=(session_id,))
        result = cur.fetchone()
        session = Session(session_id=result[0], user_id=result[1], key_id=result[2], timestamp=result[3])
        dbm.close_connection(db)
        return session
    else:
        return None
