from PyQt5.QtWidgets import *
import random


class MainWindow(QMainWindow):
    def __init__(self, parent=None, img=None):
        super(MainWindow, self).__init__(parent)
        self.img = img
        self.orig_img = img.copy()
        self.setWindowTitle('Mosaic')
        self.setGeometry(300, 200, 620, 690)

        self.can_move = True
        self.board = [[QPushButton(self) for j in range(4)] for i in range(4)]
        self.empty = (3, 3)
        self.init_board()

        self.confirm_button = QPushButton('confirm', self)
        self.confirm_button.setGeometry(260, 630, 100, 40)
        self.confirm_button.clicked.connect(self.onconfirm)

    def init_board(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j].setText(str(i * 4 + j + 1))
                self.board[i][j].setGeometry(j * 150 + 10, i * 150 + 10, 150, 150)
                self.board[i][j].clicked.connect(self.onclick((i, j)))
        self.board[3][3].setHidden(True)
        self.shuffle()

    def onclick(self, pos):
        def move():
            if not self.can_move or not self.next_to(pos, self.empty):
                return
            self.move_block(pos)
        return move

    def onconfirm(self):
        if not self.can_move:
            return
        self.can_move = False
        # crop image
        size = (self.img.size[0] + 2) // 4, (self.img.size[1] + 2) // 4
        for i in range(4):
            for j in range(4):
                num = int(self.board[i][j].text())
                x, y = (num - 1) // 4, (num - 1) % 4
                print(4 * i + j + 1, 4 * x + y + 1)
                crop_rect = (
                    y * size[0], x * size[1],
                    (y + 1) * size[0], (x + 1) * size[1]
                )
                crop_img = self.orig_img.crop(crop_rect)
                self.img.paste(crop_img, (j * size[0], i * size[1]))
        self.img.save('capture.png', 'PNG')
        self.img.show()

    def move_block(self, pos):
        # change empty tag
        target = self.empty
        self.empty = pos
        # exchange number
        text1, text2 = self.board[pos[0]][pos[1]].text(), self.board[target[0]][target[1]].text()
        self.board[pos[0]][pos[1]].setText(text2)
        self.board[target[0]][target[1]].setText(text1)
        # hide and unhide
        self.board[pos[0]][pos[1]].setHidden(True)
        self.board[target[0]][target[1]].setHidden(False)

    def next_to(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

    def in_bound(self, pos):
        return 0 <= pos[0] < 4 and 0 <= pos[1] < 4

    def shuffle(self):
        num = random.randint(270, 360)
        print(num)
        for n in range(num):
            i, j = self.empty
            possible_moves = [pos for pos in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)] if self.in_bound(pos)]
            self.move_block(random.choice(possible_moves))
