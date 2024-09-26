from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('database.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'Cannot open database',
                                           'SI data cannot open', QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec('CREATE TABLE IF NOT EXISTS database (ID integer primary key AUTOINCREMENT, ID\xa0канала INTEGER, '
                   'Название\xa0канала TEXT, Промпт\xa0текста TEXT, Пикча BOOL, Рандом\xa0текст BOOL, '
                   'Время TEXT, Токен TEXT)')
        return db

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        else:
            QtWidgets.QMessageBox.critical(None, 'Ой', 'Введите все значения' + str(type(query_values)),
                                           QtWidgets.QMessageBox.Cancel)

        query.exec()
        return query

    def row_counter(self):
        row_count = 0
        query = QtSql.QSqlQuery()
        query.exec("SELECT * FROM database")
        while (query.next()):
            row_count = row_count + 1
        return row_count

    def add_new_query(self, ch_ID, ch_name, pt_text, pt_pic, rand, time, token):
        sql_query = (
            'INSERT INTO database (ID\xa0канала, Название\xa0канала, Промпт\xa0текста, Пикча, '
            'Рандом\xa0текст, Время, Токен) '
            'VALUES (?, ?, ?, ?, ?, ?, ?)')
        self.execute_query_with_params(sql_query, [ch_ID, ch_name, pt_text, pt_pic, rand, time, token])

    def update_query(self, ch_ID, ch_name, pt_text, pt_pic, rand, time, token, id):
        sql_query = ("UPDATE database SET ID\xa0канала=?, Название\xa0канала=?, Промпт\xa0текста=?, "
                     "Пикча=?, Рандом\xa0текст=?, Время=?, Токен=? WHERE ID=?")
        self.execute_query_with_params(sql_query, [ch_ID, ch_name, pt_text, pt_pic, rand, time, token, id])

    def delete_query(self, id):
        sql_query = "DELETE FROM database WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])
