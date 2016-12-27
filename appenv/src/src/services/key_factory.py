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


def get_key(key_id=None, tag_id=None, room_id=None):
    if key_id is not None and tag_id is not None and room_id is not None:
        db = dbm.get_db()
        cur = db.cursor()
        params = tuple([p for p in [key_id, tag_id, room_id] if p is not None])
        sql_command = 'SELECT * FROM Key WHERE ' + 'id = ? ' if key_id is not None else ''
        + 'tag_id = ? ' if tag_id is not None else '' + 'room_id = ? ' if room_id is not None else ''
        cur.execute(sql=sql_command, parameters=params)
        result = cur.fetchone()
        key = Key(key_id=result[1], tag_id=result[2], room_id=result[3])
        dbm.close_connection(db)
        return key
    else:
        return None
