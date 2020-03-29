# 井字棋 (Tic Tac Toe)

这里是井字棋的两种训练的逻辑。

训练:

```bash
python train.py
# 或者 python train2.py
```

大概几分钟就可以完成需要，并且将模型保存在 `Q.npy` 文件中。

测试:

```bash
python test.py Q.npy human -- 玩家先手
python test.py Q.npy ai -- AI先手
```

使用 `1-9` 控制下棋的位置:

```text
1 2 3
4 5 6
7 8 9
```

就可以进行游戏。

```text
python test.py Q.npy ai
AI first
ai turn
[[1 0 0]
 [0 0 0]
 [0 0 0]]
please 1-9 to move in chess: 2
your turn:
[[1 2 0]
 [0 0 0]
 [0 0 0]]
ai turn
[[1 2 0]
 [0 0 0]
 [1 0 0]]
please 1-9 to move in chess: 4
your turn:
[[1 2 0]
 [2 0 0]
 [1 0 0]]
ai turn
[[1 2 0]
 [2 1 0]
 [1 0 0]]
please 1-9 to move in chess: 3
your turn:
[[1 2 2]
 [2 1 0]
 [1 0 0]]
ai turn
[[1 2 2]
 [2 1 0]
 [1 0 1]]
You LOST
```

在训练中，其实可以得到结论，就是无论先手或者后手，最终其实都可以至少达到和棋的局面。