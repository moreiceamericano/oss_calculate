import sys
from PyQt5.QtWidgets import *
from decimal import Decimal, getcontext
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.result_display = QLineEdit("")
        getcontext().prec = 10
        self.pending_operation = None
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        layout_buttons = QGridLayout()

        buttons = [
            '%', 'CE', 'C', 'Backspace',
            '1/x', 'x^2', '√', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', '.', '='
        ]

        row, col = 0, 0
        
        for button_text in buttons:
            button = QPushButton(button_text)

            if button_text.isdigit():
                button.clicked.connect(lambda state, text=button_text: self.number_clicked(text))
            elif button_text in ['+', '-', '*', '/', '%']:
                button.clicked.connect(lambda state, text=button_text: self.operation_clicked(text))
            elif button_text == '=':
                button.clicked.connect(self.button_equal_clicked)
            elif button_text == 'C':
                button.clicked.connect(self.button_clear_clicked)
            elif button_text == 'CE':
                button.clicked.connect(self.button_ce_clicked)
            elif button_text == 'Backspace':
                button.clicked.connect(self.button_backspace_clicked)
            elif button_text == 'x^2':
                button.clicked.connect(self.square_button_clicked)
            elif button_text == '1/x':
                button.clicked.connect(self.reciprocal_button_clicked)
            elif button_text == '√':
                button.clicked.connect(self.sqrt_button_clicked)
            elif button_text == '+/-':
                button.clicked.connect(self.plus_minus_button_clicked)
            elif button_text == '%':
                button.clicked.connect(self.percent_button_clicked)
            elif button_text == '.':
                button.clicked.connect(self.dot_button_clicked)

            layout_buttons.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        main_layout.addWidget(self.result_display)
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)
        self.show()

    # methods
    # 숫자 버튼이 클릭되었을 때 호출되는 메서드
    def number_clicked(self, text):
        current_text = self.result_display.text()
        new_text = current_text + text
        self.result_display.setText(new_text)

    # 사칙연산 버튼이 클릭되었을 때 호출되는 메서드
    def operation_clicked(self, text):
        current_text = self.result_display.text()
        if current_text:
            self.pending_operation = text
            new_text = current_text + ' ' + text + ' '
            self.result_display.setText(new_text)

    # 등호(=) 버튼이 클릭되었을 때 호출되는 메서드
    def button_equal_clicked(self):
        try:
            result_text = self.result_display.text()
            result = eval(result_text)  # 입력된 텍스트를 평가하여 계산
            if '.' in result_text or '/' in result_text or '%' in result_text:
                result = Decimal(result)  # 소수점, 나누기, 나머지 연산일 경우 Decimal 형식으로 변환
            self.result_display.setText(str(result))
        except Exception as e:
            self.result_display.setText("Error")  # 예외 발생 시 "Error" 표시
        self.pending_operation = None

    # C 버튼이 클릭되었을 때 호출되는 메서드
    def button_clear_clicked(self):
        self.result_display.clear()
        self.pending_operation = None

    # Backspace 버튼이 클릭되었을 때 호출되는 메서드
    def button_backspace_clicked(self):
        result = self.result_display.text()
        result = result[:-1]
        self.result_display.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
