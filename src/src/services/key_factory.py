from ..db import SqliteManager as dbm
from ..models.models import Key


def create_key(tag_id, room_id):
    if None is tag_id or None is room_id:
        return None
    db = dbm.get_db()
    try:
        cur = db.cursor()
        affected_count = cur.execute('''INSERT OR REPLACE INTO Key (tag_id, room_id)
            VALUES ( ?, ? )''', (tag_id, room_id,))
        db.commit()
        if affected_count > 0:
            cur.execute('SELECT id FROM Key WHERE tag_id = ? AND room_id = ? ', (tag_id, room_id,))
            result = cur.fetchone()
            print(result)
            key_id = int(result[0])
            dbm.close_connection(db)
            return Key(key_id=key_id, tag_id=tag_id, room_id=room_id)
        else:
            raise "Affected rows: ", affected_count
    except:
        return None
    finally:
        dbm.close_connection(db)


def get_keys(limit=0):
    db = dbm.get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM Key')
    results = cur.fetchall() if limit == 0 else cur.fetchmany(size=limit)
    keys = [Key(res[0], res[1], res[2]) for res in results]
    dbm.close_connection(db)
    return keys


def search_key(key_id=None, tag_id=None, room_id=None, limit=1, exclusive=False):
    if not (key_id is None and tag_id is None and room_id is None):
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [key_id, tag_id, room_id] if p is not None])
        condition_operator = ' AND ' if exclusive else ' OR '
        sql_conditions = condition_operator.join(filter(
            lambda x: x is not '', [' id = ? ' if key_id is not None else '',
                                    ' tag_id = ? ' if tag_id is not None else '',
                                    ' room_id = ? ' if room_id is not None else '']))
        sql_command = 'SELECT * FROM Key WHERE ' + sql_conditions
        print('From server - key factory - search sql command: %s' % sql_command)
        cur.execute(sql_command, params)
        results = [cur.fetchone()] if limit == 1 else cur.fetchall()
        print('From server - key factory - search results: %s' % results)
        dbm.close_connection(db)
        if None is results or 0 == len(results) or None is results[0]:
            return None
        else:
            keys = []
            if len(results) > 1:
                keys = [Key(res[0], res[1], res[2]) for res in results]
            else:
                res = results[0]
                keys.append(Key(res[0], res[1], res[2]))
            return keys[0] if limit == 1 else keys
    else:
        return None


def delete_key(key_id=None, tag_id=None, room_id=None, delete_history=False):
    if not (key_id is None and tag_id is None and room_id is None):
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [key_id, tag_id, room_id] if p is not None])
        condition_operator = ' AND '
        sql_conditions = condition_operator.join(filter(
            lambda x: x is not '', [' id = ? ' if key_id is not None else '',
                                    ' tag_id = ? ' if tag_id is not None else '',
                                    ' room_id = ? ' if room_id is not None else '']))
        if True == delete_history and None is key_id:
            sql_command = 'SELECT * FROM Key WHERE ' + sql_conditions + ' LIMIT 1 '
            cur.execute(sql_command, params)
            key_id = cur.fetchone()[0]
        # delete key
        sql_command = 'DELETE FROM Key WHERE ' + sql_conditions
        cur.execute(sql_command, params)
        db.commit()
        # check if key deleted
        sql_command = 'SELECT * FROM Key WHERE ' + sql_conditions + ' LIMIT 1 '
        cur.execute(sql_command, params)
        result = cur.fetchone()
        # delete all sessions where key_id matches selected key
        linked_sessions = None
        if True == delete_history:
            sql_command = 'DELETE FROM Session WHERE key_id = ? '
            params = key_id
            cur.execute(sql_command, params)
            db.commit()
            # check if matched sessions deleted
            sql_command = 'SELECT * FROM Session WHERE key_id = ? '
            cur.execute(sql_command, params)
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
        condition_operator = ' AND '
        sql_updates = condition_operator.join(filter(
            lambda x: x is not '', [' id = ? ' if key_id is not None else '',
                                    ' tag_id = ? ' if tag_id is not None else '',
                                    ' room_id = ? ' if room_id is not None else '']))
        # update key
        sql_command = 'UPDATE Key SET ' + sql_updates + ' WHERE id = ?'
        params += (key_id,)
        # params *= 2
        cur.execute(sql_command, params)
        db.commit()
        # return updated key
        sql_command = 'SELECT * FROM Key WHERE id = ? LIMIT 1 '
        cur.execute(sql_command, (key_id,))
        result = cur.fetchone()
        key = Key(key_id=result[0], tag_id=result[1], room_id=result[2])
        dbm.close_connection(db)
        return key
    else:
        return None