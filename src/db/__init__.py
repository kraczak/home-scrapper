# SQLite database using WAL journal mode and 64MB cache.

from peewee import SqliteDatabase

db = SqliteDatabase('app.db', pragmas={'journal_mode': 'wal', 'cache_size': -1024 * 64})
