#начни тут создавать приложение 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QListWidget, QLineEdit, QTextEdit, QWidget, QButtonGroup, QGroupBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QMessageBox

app = QApplication([])
glav_widow = QWidget()
glav_widow.setWindowTitle('Умные заметки')
glav_widow.resize(900,800)


list_myzametki = QListWidget()
list_myzametki_label = QLabel('Мои заметки')

vvod_myzametki = QLineEdit('')
vvod_myzametki.setPlaceholderText('ddt')
vvod_text1 = QTextEdit() 

button_myzametki_creat = QPushButton('Создать заметку')
button_myzametki_delit = QPushButton('удалить заметку')
button_myzametki_savede = QPushButton('сохранить заметку')

list_myteg = QListWidget()
list_myteg_label = QLabel('Список тегов')

button_myteg_creat = QPushButton('добавить к заметке')
button_myteg_delit = QPushButton('открепить от заметки')
button_myteg_find = QPushButton('искать тег по заметке')


vvod_myteg_dobavit = QLineEdit('')
vvod_myteg_dobavit.setPlaceholderText('Введите тег...')
vvod_text_dobavit = QTextEdit() 

layout_line_1 = QVBoxLayout()
layout_line_2 = QVBoxLayout()

layout_line_3 = QHBoxLayout() #список заметок
layout_line_4 = QHBoxLayout() #создать/удалить заметку
layout_line_5 = QHBoxLayout() #сохранить заметку
layout_line_6 = QHBoxLayout() #список тегов
layout_line_7 = QHBoxLayout() #введите тег
layout_line_8 = QHBoxLayout() #добавить/открепить
layout_line_9 = QHBoxLayout() #искать заметку


layout_line_3.addWidget(list_myzametki)
layout_line_4.addWidget(button_myzametki_creat)
layout_line_4.addWidget(button_myzametki_delit)
layout_line_5.addWidget(button_myzametki_savede)
layout_line_6.addWidget(list_myteg)
layout_line_7.addWidget(vvod_myteg_dobavit)
layout_line_8.addWidget(button_myteg_creat)
layout_line_8.addWidget(button_myteg_delit)
layout_line_9.addWidget(button_myteg_find)

layout_line_1.addWidget(list_myteg_label)

layout_line_2.addLayout(layout_line_3)
layout_line_2.addLayout(layout_line_4)
layout_line_2.addLayout(layout_line_5)
layout_line_2.addLayout(layout_line_6)
layout_line_2.addLayout(layout_line_7)
layout_line_2.addLayout(layout_line_8)
layout_line_2.addLayout(layout_line_9)


glav_widow.setLayout(layout_line_2)
glav_widow.setLayout(layout_line_1)
glav_widow.show()
app.exec()
