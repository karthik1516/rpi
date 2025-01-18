import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        label = QLabel('Hello, World!')
        layout.addWidget(label)
        self.setLayout(layout)

        self.setWindowTitle('Hello PyQt')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HelloWorld()
    sys.exit(app.exec_())
    