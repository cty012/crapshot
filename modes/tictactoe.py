from PyQt5.QtWidgets import *
import random


class MainWindow(QMainWindow):
    def __init__(self, parent=None, img=None):
        super(MainWindow, self).__init__(parent)
        self.img = img
        self.setGeometry(300, 200, 300, 350)
        self.setWindowTitle('Tic-Tac-Toe')

        self.remain = 9
        self.num = [0, 0, 0, 0, 0, 0, 0, 0]
        self.vis1 = False
        self.vis2 = False
        self.vis3 = False
        self.vis4 = False
        self.vis5 = False
        self.vis6 = False
        self.vis7 = False
        self.vis8 = False
        self.vis9 = False
        self.selected = []

        layout4 = QGridLayout()

        self.button0 = QLabel(self)
        self.button0.setText('To verify your identity,\nplease win the Tic Tac Toe game')
        self.button0.setGeometry(20, 305, 280, 45)

        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)
        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.button7 = QPushButton(self)
        self.button8 = QPushButton(self)
        self.button9 = QPushButton(self)

        self.button1.setGeometry(0, 0, 100, 100)
        self.button2.setGeometry(100, 0, 100, 100)
        self.button3.setGeometry(200, 0, 100, 100)
        self.button4.setGeometry(0, 100, 100, 100)
        self.button5.setGeometry(100, 100, 100, 100)
        self.button6.setGeometry(200, 100, 100, 100)
        self.button7.setGeometry(0, 200, 100, 100)
        self.button8.setGeometry(100, 200, 100, 100)
        self.button9.setGeometry(200, 200, 100, 100)

        self.button1.clicked.connect(self.click1)
        self.button2.clicked.connect(self.click2)
        self.button3.clicked.connect(self.click3)
        self.button4.clicked.connect(self.click4)
        self.button5.clicked.connect(self.click5)
        self.button6.clicked.connect(self.click6)
        self.button7.clicked.connect(self.click7)
        self.button8.clicked.connect(self.click8)
        self.button9.clicked.connect(self.click9)

    def click1(self):
        if self.vis1:
            return
        self.button1.setText('X')
        self.vis1 = True
        self.selected.append(1)
        self.randomMove()

    def click2(self):
        if self.vis2:
            return
        self.button2.setText('X')
        self.vis2 = True
        self.selected.append(2)
        self.randomMove()

    def click3(self):
        if self.vis3:
            return
        self.button3.setText('X')
        self.vis3 = True
        self.selected.append(3)
        self.randomMove()

    def click4(self):
        if self.vis4:
            return
        self.button4.setText('X')
        self.vis2 = True
        self.selected.append(4)
        self.randomMove()

    def click5(self):
        if self.vis5:
            return
        self.button5.setText('X')
        self.vis5 = True
        self.selected.append(5)
        self.randomMove()

    def click6(self):
        if self.vis6:
            return
        self.button6.setText('X')
        self.vis6 = True
        self.selected.append(6)
        self.randomMove()

    def click7(self):
        if self.vis7:
            return
        self.button7.setText('X')
        self.vis7 = True
        self.selected.append(7)
        self.randomMove()

    def click8(self):
        if self.vis8:
            return
        self.button8.setText('X')
        self.vis8 = True
        self.selected.append(8)
        self.randomMove()

    def click9(self):
        if self.vis9:
            return
        self.button9.setText('X')
        self.vis9 = True
        self.selected.append(9)
        self.randomMove()

    def compclick1(self):
        self.button1.setText('O')
        self.vis1 = True

    def compclick2(self):
        self.button2.setText('O')
        self.vis2 = True

    def compclick3(self):
        self.button3.setText('O')
        self.vis3 = True

    def compclick4(self):
        self.button4.setText('O')
        self.vis4 = True

    def compclick5(self):
        self.button5.setText('O')
        self.vis5 = True

    def compclick6(self):
        self.button6.setText('O')
        self.vis6 = True

    def compclick7(self):
        self.button7.setText('O')
        self.vis7 = True

    def compclick8(self):
        self.button8.setText('O')
        self.vis8 = True

    def compclick9(self):
        self.button9.setText('O')
        self.vis9 = True

    def randomMove(self):
        self.remain -= 2
        if self.remain < 0:
            self.final()
            return
        x = random.randrange(1, self.remain + 2)
        cnt = 0
        if not self.vis1:
            cnt += 1
            if cnt == x:
                self.compclick1()
        if not self.vis2:
            cnt += 1
            if cnt == x:
                self.compclick2()
        if not self.vis3:
            cnt += 1
            if cnt == x:
                self.compclick3()
        if not self.vis4:
            cnt += 1
            if cnt == x:
                self.compclick4()
        if not self.vis5:
            cnt += 1
            if cnt == x:
                self.compclick5()
        if not self.vis6:
            cnt += 1
            if cnt == x:
                self.compclick6()
        if not self.vis7:
            cnt += 1
            if cnt == x:
                self.compclick7()
        if not self.vis8:
            cnt += 1
            if cnt == x:
                self.compclick8()
        if not self.vis9:
            cnt += 1
            if cnt == x:
                self.compclick9()

    def final(self):
        for i in self.selected:
            self.num[(i - 1) // 3] += 1
            self.num[3 + (i - 1) % 3] += 1
            if i == 1 or i == 5 or i == 9:
                self.num[6] += 1
            if i == 3 or i == 5 or i == 7:
                self.num[7] += 1
        res = False
        for i in self.num:
            if i >= 3:
                res = True
        if res:
            self.button0.clear()
            self.button0.setText('YOU WIN!!! Now you may see the screenshot!')
            self.img.save('capture.png', 'PNG')
            self.img.show()
        else:
            self.button0.clear()
            self.button0.setText('YOU LOST!!! You cannot view the screenshot!')
