from PyQt5.QtWidgets import *
import random
from PIL import ImageDraw


class MainWindow(QMainWindow):
    def __init__(self, parent=None, img=None):
        super(MainWindow, self).__init__(parent)
        self.img = img
        self.setWindowTitle('Reversi')
        self.setGeometry(400, 100, 820, 890)

        self.board = [[QPushButton(self) for j in range(8)] for i in range(8)]
        self.init_board()

        self.skip_button = QPushButton('skip', self)
        self.skip_button.setGeometry(360, 830, 100, 40)
        self.skip_button.clicked.connect(self.onskip)

    def init_board(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j].setGeometry(j * 100 + 10, i * 100 + 10, 100, 100)
                self.board[i][j].clicked.connect(self.onclick((i, j)))
        self.board[3][3].setStyleSheet('background-color: #0000ff')
        self.board[3][4].setStyleSheet('background-color: #ff0000')
        self.board[4][3].setStyleSheet('background-color: #ff0000')
        self.board[4][4].setStyleSheet('background-color: #0000ff')

    def in_bound(self, pos):
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

    def get_color(self, pos):
        return self.board[pos[0]][pos[1]].palette().button().color()

    def detect_direction(self, pos, step, color_name):
        cur = self.step(pos, step)
        more_than_one = False
        while self.in_bound(cur):
            cur_color = self.get_color(cur)
            if cur_color.name() == {'#ff0000': '#0000ff', '#0000ff': '#ff0000'}[color_name]:
                cur = self.step(cur, step)
                more_than_one = True
            elif cur_color.name() == color_name:
                return cur if more_than_one else None
            else:
                return None
        return None

    def detect(self, pos, color_name):
        target_l = self.detect_direction(pos, (-1, 0), color_name)
        target_t = self.detect_direction(pos, (0, -1), color_name)
        target_r = self.detect_direction(pos, (1, 0), color_name)
        target_b = self.detect_direction(pos, (0, 1), color_name)
        target_tl = self.detect_direction(pos, (-1, -1), color_name)
        target_tr = self.detect_direction(pos, (1, -1), color_name)
        target_br = self.detect_direction(pos, (1, 1), color_name)
        target_bl = self.detect_direction(pos, (-1, 1), color_name)
        return [i for i in [
            target_l, target_t, target_r, target_b, target_tl, target_tr, target_br, target_bl
        ]if i is not None]

    def onclick(self, pos):
        def move():
            targets = self.detect(pos, '#0000ff')
            if len(targets) == 0:
                return
            self.board[pos[0]][pos[1]].setStyleSheet('background-color: #0000ff')
            for target in targets:
                self.reverse(pos, target)
            self.random_move('#ff0000')
            self.detect_win()
        return move

    def onskip(self):
        # detect if cannot skip
        moves = self.find_all_moves('#0000ff')
        if len(moves) > 0:
            return
        # opponent moves
        self.random_move('#ff0000')
        self.detect_win()

    def step(self, pos, step):
        return pos[0] + step[0], pos[1] + step[1]

    def reverse(self, start, finish):
        color = self.get_color(start)
        step = [
            0 if start[0] == finish[0] else (1 if start[0] < finish[0] else -1),
            0 if start[1] == finish[1] else (1 if start[1] < finish[1] else -1),
        ]
        cur = self.step(start, step)
        while cur[0] != finish[0] or cur[1] != finish[1]:
            self.board[cur[0]][cur[1]].setStyleSheet(f'background-color: {color.name()}')
            cur = self.step(cur, step)

    def find_all_moves(self, color_name):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if self.get_color((i, j)).name() in ['#ff0000', '#0000ff']:
                    continue
                if len(self.detect((i, j), color_name)) > 0:
                    all_moves.append((i, j))
        return all_moves

    def random_move(self, color_name):
        moves = self.find_all_moves(color_name)
        if len(moves) == 0:
            return
        pos = random.choice(self.find_all_moves(color_name))
        targets = self.detect(pos, color_name)
        if len(targets) > 0:
            self.board[pos[0]][pos[1]].setStyleSheet(f'background-color: {color_name}')
        for target in targets:
            self.reverse(pos, target)

    def detect_win(self):
        for i in range(8):
            for j in range(8):
                if self.get_color((i, j)).name() not in ['#ff0000', '#0000ff']:
                    return
        # find unoccupied blocks
        blocks = []
        for i in range(8):
            for j in range(8):
                if self.get_color((i, j)).name() == '#ff0000':
                    blocks.append((i, j))
        size = (self.img.size[0] + 4) // 8, (self.img.size[1] + 4) // 8
        # removed unoccupied blocks
        draw = ImageDraw.Draw(self.img)
        for block in blocks:
            rect = (
                (size[0] * block[1], size[1] * block[0]),
                (size[0] * (block[1] + 1), size[1] * (block[0] + 1)),
            )
            draw.rectangle(rect, outline='black', fill='black')
        self.img.save('capture.png', 'PNG')
        self.img.show()
