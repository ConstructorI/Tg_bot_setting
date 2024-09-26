import sys
import telebot
import requests

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QTimeEdit, QAbstractSpinBox, QHeaderView
from PySide6.QtCore import QTimer, QTime
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtSql import QSqlQueryModel, QSqlQuery

from bot2 import gen
from gradio_client import Client

from base_data import Data
from MainWindow import Ui_MainWindow
from Pub_add import Ui_Pub_add
from Token_input import Ui_Token_input
from do_del import Ui_Del


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.base = Data()

        self.token = ""

        self.tray_act()
        self.conn_base()
        self.main_act()

    def tray_act(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("flower.ico"))

        tray_menu = QMenu()
        restore_action = QAction("Восстановить", self)
        restore_action.triggered.connect(self.show)
        tray_menu.addAction(restore_action)

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.exit_app)
        tray_menu.addAction(exit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.tray_icon.show()

    def main_act(self):
        self.ui_main.pushButton_2.setHidden(True)
        self.ui_main.pushButton_3.setHidden(True)
        self.ui_main.pushButton.clicked.connect(lambda: self.open_Token_input())
        self.ui_main.pushButton_3.clicked.connect(lambda: self.open_Pub_add())
        self.ui_main.pushButton_2.clicked.connect(lambda: self.quit())
        self.ui_main.tableView.doubleClicked.connect(lambda: self.open_del_from_base())

    '''
    Таймер и алгоритм проверки времени
    '''

    def timer_act(self):
        self.timer = QTimer(self)
        if self.token:
            self.timer.timeout.connect(lambda: self.check_time_and_process())
        self.timer.start(60000)  # 1 мин

    def check_time_and_process(self):
        print("проверка")
        query = QSqlQuery(self.base.create_connection())
        query.exec('SELECT ID, Время FROM database')
        while query.next():
            id_value = query.value(0)
            time_value = query.value(1)
            times = time_value.split(" ")
            for i in times:
                time_i = QTime.fromString(i, 'h:mm')
                print(time_i)
                if time_i.hour() == -1:
                    time_i = QTime.fromString(i, 'hh:mm')
                    print(time_i)
                if time_i.hour() == QTime.currentTime().hour() and time_i.minute() == QTime.currentTime().minute():
                    self.data_to_gen(id_value)

    def data_to_gen(self, id_value):
        query = QSqlQuery(self.base.create_connection())
        query.prepare('SELECT * FROM database WHERE ID = :id')
        query.bindValue(':id', id_value)
        if query.exec():
            if query.next():
                column1 = query.value(1)
                column2 = query.value(2)
                column3 = query.value(3)
                column4 = query.value(4)
                column5 = query.value(5)
                column6 = query.value(6)
                data = [column1, column2, column3, column4, column5, column6]
                print(data)
                self.generate(data)

    '''
    Работа с базой данных
    '''

    def conn_base(self):
        self.model = QSqlQueryModel(self)
        query = QSqlQuery(self.base.create_connection())
        query.prepare("SELECT * FROM database WHERE Токен = :token")
        query.bindValue(":token", self.token)
        query.exec()
        self.model.setQuery(query)
        self.ui_main.tableView.setModel(self.model)

        self.ui_main.tableView.setColumnHidden(0, True)
        self.ui_main.tableView.setColumnHidden(1, True)
        self.ui_main.tableView.setColumnHidden(3, True)
        self.ui_main.tableView.setColumnHidden(4, True)
        self.ui_main.tableView.setColumnHidden(5, True)
        self.ui_main.tableView.setColumnHidden(7, True)
        self.ui_main.tableView.setColumnWidth(2, 200)
        self.ui_main.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui_main.tableView.setColumnWidth(2, 200)

    def add_to_base(self):
        ch_name = self.ui_Pub_add.lineEdit.text()
        ch_ID = self.ui_Pub_add.lineEdit_2.text()
        pt_text = self.ui_Pub_add.plainTextEdit.toPlainText()
        if self.ui_Pub_add.checkBox_2.isChecked():
            pt_pic = True
        else:
            pt_pic = False
        token = self.token
        if self.ui_Pub_add.checkBox.isChecked():
            rand = True
        else:
            rand = False
        time = self.ui_Pub_add.timeEdit.text()
        if self.time_edits:
            for time_i in self.time_edits:
                time += " " + time_i.text()
        self.base.add_new_query(ch_ID, ch_name, pt_text, pt_pic, rand, time, token)
        self.Pub_add.close()
        self.conn_base()

    def open_del_from_base(self):
        self.DoDel = QtWidgets.QDialog()
        self.ui_do_del = Ui_Del()
        self.ui_do_del.setupUi(self.DoDel)
        self.DoDel.show()
        self.ui_do_del.pushButton.clicked.connect(lambda: self.delete())
        self.ui_do_del.pushButton_2.clicked.connect(lambda: self.DoDel.close())

    def delete(self):
        id = self.ui_main.tableView.selectedIndexes()[0].row()
        base_id = str(self.model.record(id).value("ID"))
        self.base.delete_query(base_id)
        self.conn_base()
        self.DoDel.close()

    def quit(self):
        self.token = ""
        self.conn_base()
        self.ui_main.label_2.setText("Название бота")
        self.ui_main.label_3.setText("Пикча бота")
        self.ui_main.pushButton.setHidden(False)
        self.ui_main.pushButton_2.setHidden(True)

    '''
    Окно добавления токена
    '''

    def open_Token_input(self):
        self.Token_input = QtWidgets.QDialog()
        self.ui_Token_input = Ui_Token_input()
        self.ui_Token_input.setupUi(self.Token_input)
        self.Token_input.show()
        self.ui_Token_input.pushButton.clicked.connect(lambda: self.save_Token_input())
        self.ui_Token_input.pushButton_2.clicked.connect(lambda: self.close_Token_input())

    def get_profile_photo(self, token, photos, bot):
        if photos.total_count > 0:
            file_id = photos.photos[0][-1].file_id
            file_info = bot.get_file(file_id)
            file_path = file_info.file_path

            url = f'https://api.telegram.org/file/bot{token}/{file_path}'
            response = requests.get(url)
            return response.content
        return None

    def save_Token_input(self):
        token = self.ui_Token_input.lineEdit.text()
        self.token = token
        bot = telebot.TeleBot(token)
        bot_info = bot.get_me()
        photos = bot.get_user_profile_photos(bot_info.id)
        self.ui_main.label_2.setText(str(bot_info.username))
        image_data = self.get_profile_photo(token, photos, bot)
        if image_data:
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap = pixmap.scaled(50, 50)
            self.ui_main.label_3.setPixmap(pixmap)
        else:
            self.ui_main.label_3.setText(" Нет фото ")
        self.ui_main.pushButton.setHidden(True)
        self.ui_main.pushButton_2.setHidden(False)
        self.ui_main.pushButton_3.setHidden(False)
        self.conn_base()
        self.timer_act()
        self.Token_input.close()

    def close_Token_input(self):
        self.Token_input.close()

    '''
    Окно добавления публикации
    '''

    def open_Pub_add(self):
        self.Pub_add = QtWidgets.QDialog()
        self.ui_Pub_add = Ui_Pub_add()
        self.ui_Pub_add.setupUi(self.Pub_add)
        self.Pub_add.show()
        self.time_edits = []
        self.ui_Pub_add.pushButton.clicked.connect(lambda: self.add_time())
        self.ui_Pub_add.pushButton_2.clicked.connect(lambda: self.remove_time_edit())
        self.ui_Pub_add.pushButton_3.clicked.connect(lambda: self.add_to_base())

    def add_time(self):
        time_edit = QTimeEdit()
        time_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.ui_Pub_add.verticalLayout_5.addWidget(time_edit)
        print(self.time_edits)
        self.time_edits.append(time_edit)

    def remove_time_edit(self):
        if self.time_edits:
            time_edit = self.time_edits[-1]
            time_edit.deleteLater()
            time_edit.setParent(None)
            self.time_edits.remove(time_edit)

    def close_Pub_add(self):
        self.Pub_add.close()

    '''
    Чтоб трей и таймер работали норм
    '''

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.show_notification("Уведомление", "Программа всё ещё работает. "
                                              "Выйти можно через иконку на панели.")

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def show_notification(self, title, message):
        self.tray_icon.showMessage(title, message, QSystemTrayIcon.Information, 5000)

    def exit_app(self):
        QApplication.quit()

    def generate(self, data):
        bot = telebot.TeleBot(self.token)
        if data[4]:
            rand_text = "Вот текст: " + gen() + "\n"
        else:
            rand_text = ""
        query1 = rand_text + data[2] + ". МАКСИМАЛЬНАЯ ДЛИНА ТВОЕГО ОТВЕТА - 1000 СИМВОЛОВ."
        try:
            client = Client("Qwen/Qwen2-72B-Instruct")
            joke = client.predict(
                query=query1,
                history=[],
                system="You are a helpful assistant",
                api_name="/model_chat"
            )
        except Exception as e:
            print(e)
            client = Client("Qwen/Qwen2-7b-instruct-demo")
            joke = client.predict(
                query=query1,
                history=[],
                system="You are a helpful assistant",
                api_name="/model_chat"
            )
        second_element = joke[1]
        nested_list = second_element[0]
        text1 = nested_list[1].strip('"')
        print(text1)
        if data[3]:
            query2 = "У меня есть текст:" + text1 + \
                     "Тебе необходимо КОРОТКО описать картинку, " \
                     "будто это основное изображение для этого текста. " \
                     "Ответ должет быть на АНГЛИЙСКОМ языке. " \
                     "ТОЛЬКО ОПИСАНИЕ КАРТИНКИ, УДАЛИ ВСЁ ОСТАЛЬНОЕ. Не добавляй пояснения. " \
                     "УДАЛИ ПОЯСНЕНИЕ, ОСТАВЬ ТОЛЬКО ОПИСАНИЕ КАРТИНКИ"
            try:
                client = Client("Qwen/Qwen2-72B-Instruct")
                joke = client.predict(
                    query=query2,
                    history=[],
                    system="You are a middleman who takes input and creates data for the best artists.",
                    api_name="/model_chat"
                )
            except Exception as e:
                print(e)
                client = Client("Qwen/Qwen2-7b-instruct-demo")
                joke = client.predict(
                    query=query2,
                    history=[],
                    system="You are a middleman who takes input and creates data for the best artists.",
                    api_name="/model_chat"
                )
            second_element = joke[1]
            nested_list = second_element[0]
            text2 = nested_list[1].strip('"')
            print(text2)

            try:
                client = Client("black-forest-labs/FLUX.1-schnell")
                result = client.predict(
                    prompt=text2,
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    num_inference_steps=4,
                    api_name="/infer"
                )
                img = open(result[0], 'rb')
                bot.send_photo(int(data[0]), img, caption=text1)
            except Exception as e:
                print(e)

                try:
                    client = Client("multimodalart/FLUX.1-merged")
                    result = client.predict(
                        prompt=text2,
                        seed=0,
                        randomize_seed=True,
                        width=1024,
                        height=1024,
                        guidance_scale=3.5,
                        num_inference_steps=8,
                        api_name="/infer"
                    )
                    img = open(result[0], 'rb')
                    bot.send_photo(int(data[0]), img, caption=text1)
                except Exception as e:
                    print(e)

                    client = Client("stabilityai/stable-diffusion-3-medium")
                    result = client.predict(
                        prompt=text2,
                        negative_prompt="incorrect human body shape, low quality, text",
                        seed=0,
                        randomize_seed=True,
                        width=1024,
                        height=1024,
                        guidance_scale=5,
                        num_inference_steps=28,
                        api_name="/infer"
                    )
                    img = open(result[0], 'rb')
                    bot.send_photo(int(data[0]), img, caption=text1)
        else:
            bot.send_message(int(data[0]), text1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
