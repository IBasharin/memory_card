from cProfile import label
from PyQt5. QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 400)
window.setWindowTitle('Memory cards')

btn = QPushButton('Ответить')
label_question = QLabel('Какой национальности не существует?')
grbbox_answer = QGroupBox('Варианты ответа:')
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')  
rbtn_4 = QRadioButton('4')

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
h_line_main_3.addStretch(1)
h_line_main_3.addWidget(btn, stretch=2)
h_line_main_3.addStretch(1)

v_line_main.addLayout(h_line_main_1, stretch=2)
v_line_main.addLayout(h_line_main_2, stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line_main_3, stretch=1)
v_line_main.addStretch(1)

window.setLayout(v_line_main)

window.show()
app.exec()
