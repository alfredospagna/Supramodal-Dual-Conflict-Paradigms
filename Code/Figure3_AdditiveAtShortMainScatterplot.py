#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:56:57 2020

@author: alfredospagna
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="white",font_scale=1)

savefigs = True
figs_dir = './Figures/'

if savefigs:
    # Make the figures folder if it doesn't yet exist
    if not os.path.isdir('./Figures/'):
        os.makedirs('./Figures/')

data = pd.read_csv('AdditiveAtShortMainScatterplot_column.csv')

import matplotlib.lines as mlines
darkgrey_line = mlines.Line2D([], [], color='darkgrey', marker='o', markersize=10, label='V-DCT')
black_line = mlines.Line2D([], [], color='black', marker='o', markersize=10, label='SM-DCT')


ax = sns.lmplot(x="Entropy", y="T2-locked RTs", hue = "Task", data=data, 
                palette=dict(V_DCT="darkgrey", SM_DCT="black"))


plt.legend(handles=[darkgrey_line, black_line], loc='middle', ncol = 1, 
          bbox_to_anchor=(1.35, 0.95))


if savefigs:
    plt.savefig('../Figures/Figure 4.pdf', bbox_inches='tight')