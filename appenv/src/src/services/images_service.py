from ..db import SqliteManager


def get_pic_url(pic_id):
    if None is pic_id:
        return '/static/default.png'
    db = dbm.get_db()
    cur = db.cursor()
    sql_command = 'SELECT pic_url FROM ImageStore WHERE id = ?'
    params = (pic_id,)
    cur.execute(sql_command, params)
    result=cur.fetchone()
    print(result)
    pic_url=result[0]
    dbm.close_connection(db)
    return pic_url
