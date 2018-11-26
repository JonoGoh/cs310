# import plotly.plotly as py
# import plotly.graph_objs as go
import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(2)

def simulation():
    for x in range(5):
        interact(T, H, P, E)
        learn(γ, δ)

def interact():
    for each agent i do
        DSi = 0
        PSi = 0
        POSi = 0
        TSi = 0
    for each agent i do
        for each opportunity to defect o do
            if Bi > So then
            DSi = DSi +T
            for each agent j : j 6= i do
                TSj = TSj +H
                if see(j,i,So) then
                    if punish (j,i,Vj) then
                        DSi = DSi +P
                        PSj = PSj +E
                    else
                        for each agent k : k 6= i∧k 6= j do
                            if see(k, j,So) then
                                if punish (k, j,Vj) then
                                    PSk = PSk +E
                                    POSj = POSj +P

def learn(γ, δ):
    Temp = 0
    for each agent i do
        TSi = TSi +DSi +PSi +POSi
        Temp = Temp+TSi
    AvgS = Temp/no agents
    for each agent i do
        if TSi < AvgS then
            if explore(γ) then
                Bi = random()
                Vi = random()
            else
                if DSi < 0 then
                    if Bi −δ < 0 then
                        Bi = 0
                    else
                        Bi = Bi −δ
                else
                    if Bi +δ > 1 then
                        Bi = 1
                    else
                        Bi = Bi +δ
                if PSi < POSi then
                    if Vi −δ < 0 then
                        Vi = 0
                    else
                        Vi = Vi −δ
                else
                if Vi +δ > 1 then
                        Vi = 1
                    else
                        Vi = Vi +δ

nx.draw(G, with_labels=True)
plt.draw()
plt.show()
