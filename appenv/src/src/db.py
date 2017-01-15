import sqlite3
from .config import DATABASE_URI


class SqliteManager:
    def __init__(self, drop_create=False):
        if drop_create:
            self.db_init()

    @staticmethod
    def get_db():
        db = sqlite3.connect(database=DATABASE_URI, timeout=5)
        return db

    @staticmethod
    def close_connection(db):
        if db is not None:
            db.close()

    def db_init(self):
        db = self.get_db()
        db.executescript('''
            DROP TABLE IF EXISTS UserSession;
            DROP TABLE IF EXISTS Session;
            DROP TABLE IF EXISTS User;
            DROP TABLE IF EXISTS UserRole;
            DROP TABLE IF EXISTS ImageStore;
            DROP TABLE IF EXISTS Key;

            PRAGMA foreign_keys = "1";

            CREATE TABLE Key (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                room_id    INTEGER NOT NULL UNIQUE,
                tag_id     INTEGER NOT NULL UNIQUE
            );

            CREATE TABLE UserRole (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name       TEXT
            );

            CREATE TABLE ImageStore (
                id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name        TEXT NOT NULL,
                location    TEXT NOT NULL,
                UNIQUE(name, location)
            );

            CREATE TABLE User (
                id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                tag_id          INTEGER NOT NULL UNIQUE,
                first_name      TEXT,
                last_name       TEXT,
                email           TEXT,
                role_id         INTEGER NOT NULL,
                pic_id          INTEGER NOT NULL,
                FOREIGN KEY (pic_id) REFERENCES ImageStore(id),
                FOREIGN KEY (role_id) REFERENCES UserRole(id)
            );

            CREATE TABLE UserSession (
                id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                user_id       INTEGER NOT NULL UNIQUE,
                timestamp     TEXT,
                UNIQUE(user_id, timestamp),
                FOREIGN KEY (user_id) REFERENCES User(id)
            );

            CREATE TABLE Session (
                id                 INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                key_id             INTEGER NOT NULL,
                user_id            INTEGER NOT NULL,
                started_on         TEXT,
                closed_on          TEXT,
                UNIQUE(key_id, user_id, timestamp),
                FOREIGN KEY(key_id) REFERENCES Key(id),
                FOREIGN KEY(user_id) REFERENCES User(id)
            );

            INSERT INTO UserRole (name) VALUES ("Professor");
            INSERT INTO UserRole (name) VALUES ("Student");
            ''')
        db.commit()
        self.close_connection(db)
