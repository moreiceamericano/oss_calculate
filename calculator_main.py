import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.result_display = QLineEdit("")  
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

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
