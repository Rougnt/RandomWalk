'''
Author: 张晟楠
Date: 2023-04-02 16:29:16
LastEditors: Rogunt abc847111391@hotmail.com
LastEditTime: 2023-04-03 21:06:39
FilePath: /StochasticProcesses/2DrandomWalk.py
Description: 二维随机游走

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
global stop_positions
# c表示散点的数量
r, c = 2, 10
lim = 40        # 定义坐标尺寸
positions = np.random.randint(-int(lim/3), int(lim/3), (r, c)).T        # 定义初始点位置
stop_positions = np.random.randint(-lim, lim, (r, c)).T                 # 定义停止位置
colors = np.random.random((c, 3))                                       # 定义c个点的颜色（rgb）
fig, ax = plt.subplots()                                        
scatters = ax.scatter(positions.T[0], positions.T[1], marker='*', s=60, c=colors)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)


def update(i):
    global positions, stop_positions
    offsets = np.random.choice((1,0, -1), (r, c)).T         # 定义移动方向，八个方向
    offsets[np.tile((positions==stop_positions)[:,0]&(positions==stop_positions)[:,1],(2,1)).T]=0   # 判断点是否到达了终点
    if offsets.any():   # 如果有任何一个点没到达终点，都要更新
        positions = positions + offsets # 更新位置
        positions[positions>lim-1]=lim  # 防止越界
        positions[positions<-(lim-1)]=-(lim)
        # 更新散点位置
        scatters.set_offsets(positions)
        # scatters = ax.scatter(positions.T[0],positions.T[1],marker='.',s=60,c=colors)
        yield scatters


# 创建动画
ani_scatters = animation.FuncAnimation(fig, update, interval=100, blit=True)
plt.show()
