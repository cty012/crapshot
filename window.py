from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
import pyscreenshot as ps

import modes as m


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(400, 200, 320, 180)
        self.setWindowTitle("Crapshot")

        self.label = None
        self.button = None

        self.add_label("Choose a method", (20, 10), (200, 60))
        self.add_button("tictactoe", (20, 70), (80, 80), func=self.clicked)
        self.add_button("reversi", (110, 70), (80, 80), func=self.clicked)
        self.add_button("mosaic", (200, 70), (80, 80), func=self.clicked)

    def add_label(self, text, pos, size):
        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setGeometry(pos[0], pos[1], size[0], size[1])

    def add_button(self, text, pos, size, func=None):
        self.button = QPushButton(self)
        self.button.setText(text)
        self.button.setGeometry(pos[0], pos[1], size[0], size[1])
        if func is not None:
            self.button.clicked.connect(self.clicked(self.button.text()))

    def clicked(self, command):
        def screenshot():
            self.hide()
            img = ps.grab()
            window = eval(f'm.{command}').MainWindow(parent=self, img=img)
            window.show()
        return screenshot
