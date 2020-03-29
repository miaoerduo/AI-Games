from game import Game
import numpy as np
import random

from IPython import embed
import sys

if __name__ == '__main__':

    game = Game()

    Q = np.zeros((game.observation_space, game.action_space))

    max_epoch = 100000
    lr = 0.3
    y = 0.8
    sigma = 0.3

    for i in range(max_epoch):
        if i % 1000 == 0:
            print('### {} / {}'.format(i, max_epoch))

        state = game.reset()
        player_id = 0
        while True:

            actions = game.actions()
            if np.random.random() < sigma:
                action = random.choice(actions)
            else:
                action = max(actions, key=lambda x: Q[state, x])

            new_state, reward = game.step((action, player_id))

            if reward == game.WIN:
                Q[state, action] = 10000
                break
            elif reward == game.DRAW:
                Q[state, action] = 0
                break

            reward_value = -100

            # enemy max score
            available_actions = game.actions()
            available_score = [Q[new_state, i] for i in available_actions]
            enemy_score = max(available_score)

            # update
            Q[state, action] = (1 - lr) * Q[state, action] + lr * (reward - y * enemy_score)

            player_id = 1 - player_id
            state = new_state

    # save Q
    save_filename = 'Q.npy'
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
