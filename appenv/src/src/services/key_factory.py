from ..db import SqliteManager as dbm
from ..models.models import Key


def create_key(tag_id=0, room_id=0):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('''INSERT OR IGNORE INTO Key (tag_id, room_id)
            VALUES ( ?, ? )''', (tag_id, room_id,))
    db.commit()
    cur.execute('SELECT id FROM Key WHERE room_id = ? ', (room_id,))
    key_id = cur.fetchone()[0]
    dbm.close_connection(db)
    return Key(key_id=key_id, tag_id=tag_id, room_id=room_id)


def get_keys(limit=0):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM Key')
    results = cur.fetchall() if limit == 0 else cur.fetchmany(size=limit)
    keys = [Key(res[0], res[1], res[2]) for res in results]
    dbm.close_connection(db)
    return keys


def search_key(key_id=None, tag_id=None, room_id=None, limit=1):
    if not (key_id is None and tag_id is None and room_id is None):
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [key_id, tag_id, room_id] if p is not None])
        condition_operator = ' AND ' if limit == 1 else ' OR '
        sql_conditions = condition_operator.join(filter(
            lambda x: x is not '', [' id = ? ' if key_id is not None else '',
                                    ' tag_id = ? ' if tag_id is not None else '',
                                    ' room_id = ? ' if room_id is not None else '']))
        sql_command = 'SELECT * FROM Key WHERE ' + sql_conditions
        cur.execute(sql=sql_command, parameters=params)
        results = cur.fetchone() if limit == 1 else cur.fetchall()
        keys = []
        for result in results:
            key = Key(key_id=result[1], tag_id=result[2], room_id=result[3])
            keys.append(key)
        dbm.close_connection(db)
        return keys[0] if limit == 1 else keys
    else:
        return None


def delete_key(key_id=None, tag_id=None, room_id=None, delete_history=False):
    if not (key_id is None and tag_id is None and room_id is None):
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [key_id, tag_id, room_id] if p is not None])
        sql_conditions = ' AND '.join(filter(
            lambda x: x is not '', [' id = ? ' if key_id is not None else '',
                                    ' tag_id = ? ' if tag_id is not None else '',
                                    ' room_id = ? ' if room_id is not None else '']))
        if True == delete_history and None is key_id:
            sql_command = 'SELECT * FROM Key WHERE ' + sql_conditions + ' LIMIT 1 '
            cur.execute(sql=sql_command, parameters=params)
            key_id = cur.fetchone()[0]
        # delete key
        sql_command = 'DELETE FROM Key WHERE ' + sql_conditions
        cur.execute(sql=sql_command, parameters=params)
        db.commit()
        # check if key deleted
        sql_command = 'SELECT * FROM Key WHERE ' + sql_conditions + ' LIMIT 1 '
        cur.execute(sql=sql_command, parameters=params)
        result = cur.fetchone()
        # delete all sessions where key_id matches selected key
        linked_sessions = None
        if True == delete_history:
            sql_command = 'DELETE FROM Session WHERE key_id = ? '
            params = key_id
            cur.execute(sql=sql_command, parameters=params)
            db.commit()
            # check if matched sessions deleted
            sql_command = 'SELECT * FROM Session WHERE key_id = ? '
            cur.execute(sql=sql_command, parameters=params)
            linked_sessions = cur.fetchall()
        dbm.close_connection(db)
        return None is result and None is linked_sessions
    else:
        return False


def update_key(key_id, tag_id=None, room_id=None):
    if not (tag_id is None and room_id is None) and key_id is not None:
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [key_id, tag_id, room_id] if p is not None])
        sql_updates = ' AND '.join(filter(
            lambda x: x is not '', [' id = ? ' if key_id is not None else '',
                                    ' tag_id = ? ' if tag_id is not None else '',
                                    ' room_id = ? ' if room_id is not None else '']))
        # update key
        sql_command = 'UPDATE Key SET ' + sql_updates + ' WHERE id = ?'
        params += (key_id,)
        cur.execute(sql=sql_command, parameters=params)
        db.commit()
        # return updated key
        sql_command = 'SELECT * FROM Key WHERE id = ? LIMIT 1 '
        cur.execute(sql=sql_command, parameters=(key_id,))
        result = cur.fetchone()
        key = Key(key_id=result[1], tag_id=result[2], room_id=result[3])
        dbm.close_connection(db)
        return key
    else:
        return None
