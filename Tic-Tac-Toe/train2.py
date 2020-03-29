from game import Game
import numpy as np
import random

if __name__ == '__main__':

    game = Game()

    Q = np.zeros((game.observation_space, game.action_space))

    max_epoch = 100000
    lr = 0.3
    y = 0.8

    for i in range(max_epoch):
        if i % 1000 == 0:
            print('### {} / {}'.format(i, max_epoch))
        state0 = game.reset()
        player_id = 0
        sigma = 0.3

        while True:

            actions = game.actions()
            if np.random.random() < sigma:
                action = random.choice(actions)
            else:
                action = max(actions, key=lambda x: Q[state0][x])

            state1, reward1 = game.step((action, player_id))

            if reward1 == game.WIN:
                Q[state0, action] = 10000
                break
            if reward1 == game.DRAW:
                Q[state0, action] = 0
                break

            # snapshot for cur board
            board = game.board.copy()

            # predict enemy's action
            available_actions = game.actions()
            enemy_action = max(available_actions, key=lambda x: Q[state1, x])
            state2, reward2 = game.step((enemy_action, 1 - player_id))

            if reward2 == game.WIN:
                Q[state0, action] = -10000
                break
            if reward2 == game.DRAW:
                Q[state0, action] = 0
                break

            # update
            reward_value = -100
            available_actions = game.actions()
            available_score = [Q[state2, i] for i in available_actions]
            max_score = max(available_score)
            Q[state0, action] = (1 - lr) * Q[state0, action] + lr * (reward_value + y * max_score)

            player_id = 1 - player_id
            game.board = board
            state0 = state1

    # save Q
    save_filename = 'Q2.npy'
    Q.dump(save_filename)
    print('Q saved in {}'.format(save_filename))

    # sample
    print("=== SAMPLE ===")
    state = game.reset()
    player_id = 0
    while True:
        # generate action
        actions = game.actions()
        action = max(actions, key=lambda x: Q[state][x])
        state, s = game.step((action, player_id))
        print('player: {}'.format(player_id))
        print(game.board)
        player_id = 1 - player_id
        if s != game.NORMAL:
            break