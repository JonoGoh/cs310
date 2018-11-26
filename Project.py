from __future__ import division
from Agent import Agent as ag
import random
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#-----Graph generation and setting parameter values-----
nodes = 51
NB = 3
# G = nx.circulant_graph(nodes,range(1,NB + 1))
G = nx.complete_graph(nodes)

rounds = range(10000)

o = 4 #opportunities per round
T = 3 #temptation to defect
H = -1 #hurt suffered by others as a result of an agent's defection
P = -9 #cost of being punished
E = -2 #enforcement cost
Pm = -9
Em = -2
d = 1/7 #learning step
y = 0.01 #exploration rate

#stuff for debugging
count = 0
interactions = 0

#relabel nodes: assign each node in the graph with an agent object with random
#values for the boldness and vengefulness
agents = []
for i in range(G.number_of_nodes()):
    agents.append(ag(i))
mapping = dict(zip(G.nodes(), agents))
nx.relabel_nodes(G, mapping, copy=False)

#interaction function
def interact(T,H,P,E):
    for i in G.nodes():
        i.reset_scores()
    for i in G.nodes():
        for a in range(o):
            S = random.random() #set the chance of being seen
            if i.boldness > S:
                i.DS += T
                for j in G.neighbors(i):
                    j.TS += H
                    if random.random() < S:
                        if random.random() < j.vengefulness:
                            i.DS += P
                            j.PS += E
                        else:
                            for k in filter(lambda x: x.name != i.name, G.neighbors(j)):
                                if random.random() < S:
                                    if random.random() < k.vengefulness:
                                        k.PS += Em
                                        j.POS += Pm

#learning function similar to qlearn (or wolf??)
def learn(y,d):
    for i in G.nodes():
        i.total()
    for i in G.nodes():
        temp = 0
        for j in G.neighbors(i):
            temp += j.TS
        avg = temp/len(list(G.neighbors(i)))
        if i.TS < avg:
            if random.random() < y:
                global count
                count += 1
                i.explore()
            else:
                if i.DS < 0:
                    if i.boldness - d < 0:
                        i.boldness = 0
                    else:
                        i.boldness = i.boldness - d
                else:
                    if i.boldness + d > 1:
                        i.boldness = 1
                    else:
                        i.boldness += d
                if i.PS < i.POS:
                    if i.vengefulness-d < 0:
                        i.vengefulness = 0
                    else:
                        i.vengefulness -= d
                else:
                    if i.vengefulness+d > 1:
                        i.vengefulness = 1
                    else:
                        i.vengefulness += d

#printing function mainly used for debugging.
def stats(r):
    ab = 0
    av = 0
    for n in G:
        ab += n.boldness
        av += n.vengefulness
    print('------------------------------------------------------------------------------------------------------------')
    print('ROUND ' + str(r+1))
    # print 'number of times explored: ' + str(count)
    print('average boldness: ' + str(ab/nodes))
    print('average vengefulness: ' + str(av/nodes))

#running the simulation
for r in rounds:
    interact(T,H,P,E)
    learn(y,d)
    # stats(r)
stats(rounds[-1])

# for i in G:
#     i.print_scores()
#
# nx.draw(G, with_labels=False)
# plt.draw()
#
# plt.show()
