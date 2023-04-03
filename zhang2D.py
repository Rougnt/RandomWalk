'''
Author: 张晟楠
Date: 2023-04-03 21:08:37
LastEditors: Rogunt abc847111391@hotmail.com
LastEditTime: 2023-04-03 21:59:47
FilePath: /StochasticProcesses/zhang2D.py
Description: 
2D随机游走，已弃用
Copyright (c) 2023 by Rogunt abc847111391@hotmail.com, All Rights Reserved. 
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
global stop_positions
# c表示散点的数量
r, c = 2, 50
positions = np.random.randint(-10, 10, (r, c))
stop_positions = np.random.randint(-39, 39, (r, c))
colors = np.random.random((c, 3))
fig, ax = plt.subplots()
scatters = ax.scatter(positions[0], positions[1], marker='*', s=60, c=colors)
plt.xlim(-40, 40)
plt.ylim(-40, 40)


def update(i):
    global positions, stop_positions
    positions = np.where(positions == stop_positions, stop_positions, positions + np.random.choice((1, -1), (r, c)))
    positions = np.where((positions > -39) & (positions < 39),
                         positions, np.sign(positions) * 39)
    # 更新散点位置
    scatters.set_offsets(positions.T)

    yield scatters


# 创建动画
ani_scatters = animation.FuncAnimation(fig, update, interval=30, blit=True)
plt.show()