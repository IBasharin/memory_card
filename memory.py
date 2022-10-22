from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 400)
window.setWindowTitle('Memory cards')

btn = QPushButton('Ответить')
label_question = QLabel('Какой национальности не существует?')
grbbox_answer = QGroupBox('Варианты ответа:')
radio_group = QButtonGroup()
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')  
rbtn_4 = QRadioButton('4')

radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

def show_question():
    btn.clicked.connect(show_resuolt)
    grbbox_answer.show()
    grpbox_results.hide()
    btn.setText('Ответить')
    btn.clicked.connect(show_resuolt)
    radio_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_group.setExclusive(True)

def show_resuolt():
    grbbox_answer.hide()
    grpbox_results.show()
    btn.setText('Следующий вопрос')
    btn.clicked.connect(show_question)

btn.clicked.connect(show_resuolt)

grpbox_results = QGroupBox('Результат ответа')
label_right_answer = QLabel('Правильный ответ:')
v_line_results = QVBoxLayout()

v_line_results.addWidget(label_right_answer, alignment=Qt.AlignCenter)
grpbox_results.setLayout(v_line_results)

h_line_ans = QHBoxLayout()
v_line_ans_1 = QVBoxLayout()
v_line_ans_2 = QVBoxLayout()

v_line_ans_1.addWidget(rbtn_1)
v_line_ans_1.addWidget(rbtn_2)
v_line_ans_2.addWidget(rbtn_3)
v_line_ans_2.addWidget(rbtn_4)
h_line_ans.addLayout(v_line_ans_1)
h_line_ans.addLayout(v_line_ans_2)

grbbox_answer.setLayout(h_line_ans)

v_line_main = QVBoxLayout()
h_line_main_1 = QHBoxLayout()
h_line_main_2 = QHBoxLayout()
h_line_main_3 = QHBoxLayout()

h_line_main_1.addWidget(label_question, alignment=Qt.AlignCenter)
h_line_main_2.addWidget(grbbox_answer)
h_line_main_2.addWidget(grpbox_results)
h_line_main_3.addStretch(1)
h_line_main_3.addWidget(btn, stretch=2)
h_line_main_3.addStretch(1)

v_line_main.addLayout(h_line_main_1, stretch=2)
v_line_main.addLayout(h_line_main_2, stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line_main_3, stretch=1)
v_line_main.addStretch(1)


grbbox_answer.hide()


window.setLayout(v_line_main)



window.show()
app.exec()
