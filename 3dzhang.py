'''
Author: 张晟楠
Date: 2023-04-02 20:23:02
LastEditors: Rogunt abc847111391@hotmail.com
LastEditTime: 2023-04-03 21:58:37
FilePath: /StochasticProcesses/3dzhang.py
Description: 
3D随机游走，我缩小了比例尺大小，限制了移动空间大小
Copyright (c) 2023 by Rogunt abc847111391@hotmail.com, All Rights Reserved. 
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
global stop_positions
# c表示散点的数量
r, c = 3, 1
positions = np.random.randint(-10, 10, (r, c))
stop_positions = np.random.randint(-10, 10, (r, c))
colors = np.random.random((c, 3))
fig = plt.figure()
ax = plt.axes(projection='3d')
scatters = ax.scatter3D(positions[0], positions[1], positions[2], marker='*', s=60, c=colors)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)


def update(i):
    global positions, stop_positions
    positions = np.where(positions == stop_positions, stop_positions, positions + np.random.choice((1, -1), (r, c)))
    positions = np.where((positions > -10) & (positions < 10),
                         positions, np.sign(positions) * 10)
    # 更新散点位置
    # scatters.set_offsets(positions.T)
    scatters = ax.scatter3D(positions[0], positions[1], positions[2], marker=',', s=1, c=colors)

    yield scatters


# 创建动画
ani_scatters = animation.FuncAnimation(fig, update, interval=1, blit=True)
plt.show()
