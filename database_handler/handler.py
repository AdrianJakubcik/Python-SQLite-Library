import sqlite3
import os
from sqlite3 import Error

class Database:

    def __init__(self, name = "DefaultName"):
        self._databaseName = name
        self._tableCount = None
        self._exists = False
        self._Connection = None

        _dir = "../Database_Files_Here"
        __file = self._file(_dir)
        assert self._isDatabaseFile(__file), f'{__file} is not a database file!'

        self._databaseName = self._parseFileName(__file)
        self._Connection = self._connection(__file)
        self._exists = True
        self._tableCount = self._countTables(self._Connection)
   

    def exists(self):
        return self._exists

    def getDatabaseName(self):
        return self._databaseName

    def tableCount(self):
        return self._tableCount

    def getConnection(self):
        return self._Connection

    
    def _file(self, _dir):
        assert len(os.listdir(_dir)) == 1, 'No or more files were found!'
        return os.listdir(_dir)[-1]

    def _isDatabaseFile(self, _file):
        filename, extension = os.path.splitext(_file)
        return True if extension == '.db' else False
    
    def _parseFileName(self, _file):
        filename, extension = os.path.splitext(_file)
        return filename

    def _connection(self, _database):
        _dbFile = "../Database_Files_Here/"+_database
        conn = None
        try:
            conn = sqlite3.connect(_dbFile)
            return conn
        except Error as e:
            raise Exception(e)

    def _creatDefaultDB(self):
        _file = '../Database_Files_Here/Default.db'
        conn = None
        try:
            conn = sqlite3.connect(_file)
        except Error as e:
            raise Exception(e)
        finally:
            if conn:
                conn.close()
                print('Default Database Was Created')
        

    def _countTables(self, _connection):
        cur = _connection.cursor()
        cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
        print(len(cur.fetchall()))
        return

    def _listAllTables(self, _connection):
        _list = []
        cur._connection.cursor()
        cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
        for res in cur.fetchall():
            _list.append(res)
        return _list
        
myDatabase = Database()