#!/usr/bin/env python3
"""
Created on Sun Apr 12 15:59:06 2020

@author: alfredospagna

#switching from the BOXPLOT to simple Lineplots

"""

import pandas as pd
import seaborn as sns 
sns.set(style="white",font_scale=1.6)
import matplotlib.pyplot as plt
import os

savefigs = True
figs_dir = '../Analysis_21Feb2020/Figure2LinePlot/'

if savefigs:
    # Make the figures folder if it doesn't yet exist
    if not os.path.isdir('../Analysis_21Feb2020/Figure2LinePlot/'):
        os.makedirs('../Analysis_21Feb2020/Figure2LinePlot/')
        

def export_fig(axis, text, fname):
    if savefigs:
        axis.text()
        axis.savefig(fname, bbox_inches='tight')

###########################################
df = pd.read_csv ("DCT_V - ERR_plots.csv", sep= ";")
df.head()

dy="Error Rate (%)"; dx="SOA"; dhue="Condition"
mypal = "Greys_d"; dcol = "Panel"; 

g = sns.catplot(x=dx, y=dy, data=df, hue=dhue, col=dcol,
                dodge = True, kind = "point",
                order = ['long', 'short'], legend = False,
                linestyles=["-", "-", "--", "--"],
                palette=["black", "grey", "black", "grey"])

plt.legend(loc='middle', ncol = 4, bbox_to_anchor=(0.15, -0.1))

import matplotlib.lines as mlines
CC = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='CC')
CI = mlines.Line2D([], [], color='grey', marker='o', markersize=10, label='CI')
IC = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='IC', linestyle='--')
II = mlines.Line2D([], [], color='grey', marker='o', markersize=10, label='II', linestyle='--')

plt.legend(handles=[CC, CI, IC, II], loc='middle', 
           ncol = 4, bbox_to_anchor=(0.5, -0.15))


g.set(ylim=(0, 40))
g.set_ylabels("Error Rate (%)")

if savefigs:
    plt.savefig('../Analysis_21Feb2020/Figure2LinePlot/DCT_V - ACC_plots.pdf', bbox_inches='tight')


###########################################
df = pd.read_csv ("DCT_V - RT_plots.csv", sep= ";")
df.head()

dy="Reaction Time (ms)"; dx="SOA"; dhue="Condition"
mypal = "Greys_d"; dcol = "Panel"; 

g = sns.catplot(x=dx, y=dy, data=df, hue=dhue, col=dcol, 
                dodge = True, share = False, kind = "point",
                order = ['long', 'short'], legend = False,
                linestyles=["-", "-", "--", "--"],
                palette=["black", "grey", "black", "grey"])

g.set(ylim=(500, 1450))
g.set_ylabels("Reaction Time (ms)")

if savefigs:
    plt.savefig('../Analysis_21Feb2020/Figure2LinePlot/DCT_V - RT_plots.pdf', bbox_inches='tight')


# ###########################################
df = pd.read_csv ("DCT_SM - ERR_plots.csv", sep= ";")
df.head()
dy="Error Rate (%)"; dx="SOA"; dhue="Condition"
mypal = "Greys_d"; dcol = "Panel"; 

g = sns.catplot(x=dx, y=dy, data=df, hue=dhue, col=dcol,
                dodge = True, kind = "point", 
                order = ['long', 'short'], legend = False,
                linestyles=["-", "-", "--", "--"],
                palette=["black", "grey", "black", "grey"])

g.set(ylim=(0, 40))
g.set_ylabels("Error Rate (%)")

if savefigs:
    plt.savefig('../Analysis_21Feb2020/Figure2LinePlot/DCT_SM - ACC_plots.pdf', bbox_inches='tight')


# ###########################################
df = pd.read_csv ("DCT_SM - RT_plots.csv", sep= ";")
df.head()
dy="Reaction Time (ms)"; dx="SOA"; dhue="Condition"
mypal = "Greys_d"; dcol = "Panel"; 

g = sns.catplot(x=dx, y=dy, data=df, hue=dhue, col=dcol,
                dodge = True, kind = "point",
                order = ['long', 'short'], legend = False,
                linestyles=["-", "-", "--", "--"],
                palette=["black", "grey", "black", "grey"])

g.set(ylim=(500, 1450))
g.set_ylabels("Reaction Time (ms)")

if savefigs:
    plt.savefig('../Analysis_21Feb2020/Figure2LinePlot/DCT_SM - RT_plots.pdf', bbox_inches='tight')
