'''
Author: Rogunt abc847111391@hotmail.com
Date: 2023-04-03 12:55:49
LastEditors: Rogunt abc847111391@hotmail.com
LastEditTime: 2023-04-03 21:57:26
FilePath: /StochasticProcesses/mygraph.py
Description: 
随机游走，图，未用Class封装，该代码可以直接对图片进行保存
Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

start = None
cur_node = None
path = []



def update(i,n,layout,G,ax,end):
    global cur_node,path
    ax.clear()
    nodes_color = ['#1f78b4']*len(G.nodes)
    nodes_color[cur_node]='#ff0000'
    if path[-1] !=end:
        if path[-1]==cur_node:
            pass
        else:
            path.append(cur_node)

    if(len(list(G.adj[cur_node]))>0 and cur_node != end):
        cur_node = random.sample(list(G.adj[cur_node]),1)[0]
    nx.draw(G,pos=layout,ax=ax,node_color=nodes_color,with_labels=True)
    global start
    ax.set_title("Start {}, End {}\nPath {}".format(start,end,path))



def random_walk_animation():
    global start,cur_node
    fig, ax = plt.subplots(figsize=(6,4))
    
    # G=nx.barbell_graph(5,2) 
    G=nx.gnm_random_graph(10,20)
    layout = nx.spring_layout(G)
    end = random.sample(list(G.nodes),1)[0]
    
    if start == None:
        start = random.sample(list(G.nodes),1)[0]
    cur_node = start
    path.append(cur_node)
    nodes_color = ['#1f78b4']*len(G.nodes)
    nodes_color[cur_node]='#ff0000'
    nx.draw(G,pos=layout,ax=ax,node_color=nodes_color,with_labels=True)
    
    ani = FuncAnimation(fig,update,frames=100,interval=500,fargs=(12,layout,G,ax,end))
    ani.save('animation_1.gif', writer='imagemagick')
    # plt.show()


       


random_walk_animation()