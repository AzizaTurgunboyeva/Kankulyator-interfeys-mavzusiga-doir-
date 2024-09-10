from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator.by Aziza")
        self.setGeometry(300, 200, 420, 540)
        self.setStyleSheet("background-color:black;")
        self.setFixedSize(420, 540)
        
        self.layout()  

    def layout(self):
        layout = QVBoxLayout()
        grid = QGridLayout()

        
        self.input = QLineEdit(self)
        self.input.setMaxLength(20)
        self.input.setAlignment(Qt.AlignRight)
        self.input.setStyleSheet("""
            font-size: 25px;
            background-color: black;
            border: none;
            color: white;
            font-weight: bold;
        """)
        layout.addWidget(self.input)

        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        #buttonlar
        for (text, row, col) in buttons:
            button = QPushButton(text, self)
            button.setStyleSheet("""
                font-size: 22px;
                background-color: #102e91;
                font-family: Lucida Console;
                font-weight: bold;
            """)
            button.clicked.connect(lambda checked, txt=text: self.onButtonClick(txt))
            grid.addWidget(button, row, col)

        # C tugmaga
        delete_button = QPushButton('Delete', self)
        delete_button.setStyleSheet("""
            font-size: 22px;
            background-color: #d32f2f;
            font-family: Lucida Console;
            font-weight: bold;
        """)
        delete_button.clicked.connect(self.clearInput)
        grid.addWidget(delete_button, 0, 0,1,2)

        cancel_button = QPushButton('Back', self)
        cancel_button.setStyleSheet("""
            font-size: 22px;
            background-color: #d32f2f;
            font-family: Lucida Console;
            font-weight: bold;
        """)
        cancel_button.clicked.connect(self.backspace)
        grid.addWidget(cancel_button, 0,2, 1,2)

        layout.addLayout(grid)
        self.setLayout(layout)

    def onButtonClick(self, char):
        if char == '=':
            self.calculate()
        else:
            self.input.setText(self.input.text() + char)

    def clearInput(self):
        self.input.clear()

    def backspace(self):
        current_text = self.input.text()
        self.input.setText(current_text[:-1])

    def calculate(self):
        expression = self.input.text()
        try:
            
            result = eval(expression, {"__builtins__": None}, {})
            # format
            formatted_result = "{:.10g}".format(result)
            self.input.setText(formatted_result)
        except Exception:
            self.input.setText("Error")


app = QApplication([])
calculator = Calculator()
calculator.show()
app.exec_()
