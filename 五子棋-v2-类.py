from sympy import false


class Wuziqi:
    def __init__(self, nrow, ncol):
        self.defaultPad = '--'
        self.nrow = nrow
        self.ncol = ncol
        self.validPos = {}
        self.board = self.initBoard()
        self.player1 = 'x-'
        self.player2 = 'o-'

        self.current_player = self.player1
        self.boardNumsMap = {self.player1:1, self.player2:-1, self.defaultPad:0}


    def getStrNum(self, x):
        return '0' + str(x) if x < 10 else str(x)

    def initBoard(self):
        board = [[self.defaultPad for _ in range(self.ncol)] for _ in range(self.nrow)]
        # 增加y前导
        for i in range(15):
            j = self.getStrNum(i+1)
            board[i] = [j] + board[i]
        # 增加x前导
        xprefix = [['00'] + [self.getStrNum(x) for x in list(range(1, 16))]]
        board  = xprefix + board

        for i in range(1, self.nrow+1):
            for j in range(1, self.ncol+1):
                self.validPos[(i, j)] = True
        return board

    def print_board(self):
        for row in self.board:
            print(' ' .join(row))
        print()

    def cal_score(self):
        # 检查水平、垂直、对角线是否有五个连续的棋子
        score = -1
        for target in range(5, 1, -1):
            for i in range(1, 15):
                for j in range(11):
                    if all(self.board[i][j + k]     == self.current_player for k in range(target)):
                        score = max(score, target)
                        return score
                    if all(self.board[i + k][j]     == self.current_player for k in range(target)):
                        score = max(score, target)
                        return score
                    if all(self.board[i + k][j + k] == self.current_player for k in range(target)):
                        score = max(score, target)
                        return score
                    if all(self.board[i + k][j - k] == self.current_player for k in range(target)):
                        score = max(score, target)
                        return score
        return score

    def get_action(self, player):
        while True:
            try:
                validSet = [k for k, v in self.validPos.items() if v==True]
                print(validSet)
                row, col = map(int, input(f"玩家 {player} 的回合，请输入您的落子位置（行 列）：").split())
                if self.validPos[(row, col)]:
                    return row, col
                else:
                    print("无效的移动，请输入棋盘内未被占用的位置。")
            except (ValueError, IndexError):
                print("输入格式错误，请输入两个数字，用空格分隔。")

    def take_action(self, row, col):
        self.board[row][col] = self.current_player
        self.validPos[(row, col)] = False
        next_state = []
        for i in range(1, self.nrow):
            tempcol = self.board[i][1:]
            tempcol = [self.boardNumsMap[j] for j in tempcol]
            next_state.append(tempcol)
        reward = self.cal_score()
        return next_state, reward


if __name__ == "__main__":
    wuziqi = Wuziqi(nrow=15, ncol=15)
    player1 = wuziqi.player1
    player2 = wuziqi.player2
    while True:
        wuziqi.print_board()

        # 可以把这里的get_move改成DQN
        row, col = wuziqi.get_action(wuziqi.current_player)
        state, reward = wuziqi.take_action(row, col)

        print(reward)
        print(state)
        if reward == 2:
            wuziqi.print_board()
            print(f"玩家 {wuziqi.current_player} 赢了！")
            break
        wuziqi.current_player = player2 if wuziqi.current_player==player1 else player1