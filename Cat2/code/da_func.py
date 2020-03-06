import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def countplot_cols(df, col_lists, ncols=3, dropna=True):
    if dropna == False:
        df = df.loc[:, col_lists].copy()
        df = df.fillna('NaN')
    nrows = len(col_lists) // ncols
    if len(col_lists) % ncols != 0:
        nrows += 1

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(7*ncols, 7*nrows))
    for i, c in enumerate(col_lists):
        value_count = df[c].value_counts(dropna=dropna)
        value_count.index = value_count.index.astype(str)
        total = len(df[c])

        ax = axes[i//ncols, i%ncols]
        sns.countplot(x=c, data=df[[c]], ax=ax)
        
        x_ticks = [x.get_text() for x in ax.get_xticklabels()]
        for p, t in zip(ax.patches, x_ticks):            
            height = p.get_height()
            ax.text(p.get_x()+p.get_width()/2.,
                    height,
                    "%d (%.2f %%)" % (value_count[t], value_count[t]/total * 100),
                    fontdict={'size':14},
                    ha="center") 

        ax.title.set_text(c)

    
    plt.tight_layout()
    plt.show()
    

def countplot_cols_hc(df, col_lists, ncols=3, dropna=True):
    # high cardinality
    if dropna == False:
        df = df.loc[:, col_lists].copy()
        df = df.fillna('NaN')
    nrows = len(col_lists) // ncols
    if len(col_lists) % ncols != 0:
        nrows += 1

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(7*ncols, 24*nrows))
    for i, c in enumerate(col_lists):
        value_count = df[c].value_counts(dropna=dropna)
        value_count.index = value_count.index.astype(str)
        total = len(df[c])

        ax = axes[i//ncols, i%ncols]
        sns.countplot(y=c, data=df[[c]], ax=ax)

        ax.title.set_text(c)

    
    plt.tight_layout()
    plt.show()