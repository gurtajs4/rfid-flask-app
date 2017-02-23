import os
import xlrd
import xlwt
from ..db import SqliteManager as dbm
from ..models.models import Key
from ..config import DATA_EXCEL_PATH as xls_store_path


def switch(argument):
    switcher = {
        0: 'key_id',
        1: 'block',
        2: 'sector',
        3: 'floor',
        4: 'room_id',
        5: 'floor'
    }
    return switcher.get(argument, 'nothing')


def seed(filename):
    file_location = os.path.join(xls_store_path, filename)
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_name('keys')
    data = []
    for i in range(1, sheet.nrows):
        room_dict = {
            switch(0): 0
        }
        for j in range(sheet.ncols):
            field_name = switch(j)
            field_value = sheet.cell_value(i, j)
            room_dict[field_name] = field_value
        data.append(room_dict)
    db = dbm.get_db()
    cur = db.cursor()
    results = []
    for i in range(len(data)):
        row = data[i]
        room_id = int(row[switch(4)])
        block_name = row[switch(1)]
        sector_name = row[switch(2)]
        floor = int(row[switch(3)])
        room_repr = block_name + sector_name + str(floor) + '-' + str(room_id)
        # tag_id = row['tag_id']
        params = tuple([p for p in (room_id, block_name, sector_name, floor, room_repr)])
        cur.execute('''INSERT OR IGNORE INTO Key (room_id, block_name, sector_name, floor, room_repr)
            VALUES ( ?, ?, ?, ?, ?, )''', params)
        db.commit()
        cur.execute('SELECT id FROM Room WHERE room_id = ? ', (room_id,))
        room_pk = cur.fetchone()[0]
        data[i]['id'] = room_pk
        results.append(Key(room_pk, tag_id, room_id, block_name, sector_name, floor, room_repr))
    dbm.close_connection(db)
    return results


def make_template():
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('keys')
    for s in range(1, 6):
        col_name = switch(s)
        sheet.write(0, s, col_name)
    file_location = os.path.join(xls_store_path, 'data_template.xls')
    workbook.save(file_location)
