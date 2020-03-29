import numpy as np


class Game:

    WIN = 0
    DRAW = 1
    NORMAL = 2
    OCCUPIED = 3

    def __init__(self):
        self.board = np.zeros((3, 3), dtype=np.uint8)
        self.observation_space = 3 ** 9  # white, black, empty
        self.action_space = 3 * 3

    def reset(self):
        self.board = np.zeros((3, 3), dtype=np.uint8)
        return 0

    def judge_win(self, x, y):
        # row
        line = self.board[x,:].flatten()
        if line.sum() > 0 and line[0] == line[1] == line[2]:
            return True
        # col
        line = self.board[:,y].flatten()
        if line.sum() > 0 and line[0] == line[1] == line[2]:
            return True
        # x
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        if self.board[2][0] != 0 and self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return True

        return False

    def state(self):
        s = 0
        for x in self.board.flatten():
            s *= 3
            s += x
        return s

    def actions(self):
        a = []
        for idx, x in enumerate(self.board.flatten()):
            if x == 0:
                a.append(idx)
        return a

    def step(self, action):
        # action: position, player_id
        # return: 新的state，是否可行，赢，游戏结束
        row = action[0] // 3
        col = action[0] % 3

        if self.board[row][col] != 0:
            return self.state(), self.OCCUPIED
        self.board[row][col] = action[1] + 1
        if self.judge_win(row, col):
            return self.state(), self.WIN
        if self.board.all():
            return self.state(), self.DRAW
        return self.state(), self.NORMAL


