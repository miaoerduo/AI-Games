import sys
import numpy as np

from game import Game

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: python test.py model human/ai')
        exit(-1)

    Q = np.load(sys.argv[1])

    human_first = True
    if sys.argv[2] == 'human':
        print('YOU first')
        human_first = True
    else:
        print('AI first')
        human_first = False

    g = Game()
    state = g.reset()

    player_id = 0
    if not human_first:
        actions = g.actions()
        action = max(actions, key=lambda x: -Q[state][x])
        state, _ = g.step((action, player_id))
        player_id = 1 - player_id

    print('ai turn')
    print(g.board)

    while True:
        while True:
            while True:
                action = input('please 1-9 to move in chess: ')
                if not action:
                    continue
                action = int(action)
                if 1 <= action <= 9:
                    break
            state, s = g.step((action - 1, player_id))
            if s == g.OCCUPIED:
                print('your cannot do that, the pos is occupied')
                continue
            break

        print('your turn:')
        print(g.board)

        if s == g.WIN:
            print('you WIN!')
            break
        if s == g.DRAW:
            print("Draw")
            break

        player_id = 1 - player_id

        # ai turn
        actions = g.actions()
        action = max(actions, key=lambda x: Q[state][x])
        state, s = g.step((action, player_id))
        player_id = 1 - player_id

        print('ai turn')
        print(g.board)

        if s == g.WIN:
            print('You LOST')
            break
        if s == g.DRAW:
            print('DRAW')
            break






