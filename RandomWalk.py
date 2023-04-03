'''
Author: Rogunt abc847111391@hotmail.com
Date: 2023-04-03 18:34:43
LastEditors: Rogunt abc847111391@hotmail.com
LastEditTime: 2023-04-03 21:59:14
FilePath: /StochasticProcesses/RandomWalk.py
Description:   在图上的随机游走

Copyright (c) 2023 by Rogunt abc847111391@hotmail.com, All Rights Reserved. 
'''
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import sympy

np.set_printoptions(precision=3)

class RandonWalkGraph():
    def __init__(self,save=False,fileName='animation.gif',show=True) -> None:
        self.start = None
        self.cur_none = None
        self.path = []
        self.fig,self.ax = plt.subplots(figsize=(6,4))
        ani = FuncAnimation(self.fig,self.update,frames=1000,init_func=self.init,interval=500)

        if show == True:
            plt.show()
        # if save == True:
        # TODO: Not Work
        #     ani.save(fileName, writer='imagemagick')
    
    def init(self) -> None:
        
        self.G = nx.gnm_random_graph(10,20) 
        self.layout = nx.spring_layout(self.G)
        self.transitionMatrix = self.transitionProbabilityMatrix()      # 计算概率转移矩阵
        self.end = random.sample(list(self.G.nodes),1)[0]               # 随机找个停止点
        if self.start == None:                                          # 如果没有初始点，随机找个初始点
            self.start = random.sample(list(self.G.nodes),1)[0]
        self.cur_node = self.start                                      # 更新当前点为起始点
        self.path.append(self.cur_node)                                 # 更新路径
        nodes_color = ['#1f78b4']*len(self.G.nodes)                     # 定义所有点颜色
        nodes_color[self.cur_node]='#ff0000'                            # 定义初始点颜色
        nx.draw(self.G,pos=self.layout,ax=self.ax,node_color=nodes_color,with_labels=True)  # 画图
        

    def update(self,i)->None:
        self.ax.clear()                                                 # 清空图片
        nodes_color = ['#1f78b4']*len(self.G.nodes)                     # 所有点颜色为蓝色（消除上次的当前点的红色）
        nodes_color[self.cur_node]='#ff0000'                            # 定义本次当前点的颜色（实际为上次循环，否则会少显示一次过程）
        if self.path[-1] !=self.end:                                    # 判断（上次）的当前点是否为终点
            if self.path[-1]==self.cur_node:
                pass
            else:
                self.path.append(self.cur_node)                         # 不是就将（上次）的当前点放进路径
        if(len(list(self.G.adj[self.cur_node]))>0 and self.cur_node != self.end):   # 判断上次当前点是否有临界点，并且是否是终点
            self.cur_node = random.sample(list(self.G.adj[self.cur_node]),1)[0]     # 从临接点中随机选取1个作为新的当前点（用在下一个循环中画图）
        nx.draw(self.G,pos=self.layout,ax=self.ax,node_color=nodes_color,with_labels=True)  # 画图
        self.ax.set_title("Start {}, End {}\nPath {}".format(self.start,self.end,self.path))    
    
    def transitionProbabilityMatrix(self) -> np.array:
        transMatrix = np.array(nx.adjacency_matrix(self.G).todense())                   # 获得邻接矩阵
        return np.array([x/x.sum() for x in transMatrix])   # 邻接矩阵每一行除以路径，获得概率
 

g = RandonWalkGraph(save=False,show=True)
print('一步转移概率矩阵\n',g.transitionMatrix)
print('路径：{}'.format(g.path))
probablity = 1
for k,point in enumerate(g.path):
    if k == len(g.path)-1:
        break
    # print('{}*{}='.format(probablity,g.transitionMatrix[point][g.path[k+1]]))
    probablity *= g.transitionMatrix[point][g.path[k+1]]            # 计算本次节点到下一个节点的概率，累成
    # print(probablity)
print('概率',probablity)
print('总计步数{}'.format(len(g.path)))