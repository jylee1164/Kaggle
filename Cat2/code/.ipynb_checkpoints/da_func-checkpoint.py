import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def countplot_cols(df, col_lists, hue=None, ncols=3, dropna=True, annot=True):
    if dropna == False:
        new_df = df.loc[:, col_lists].copy()
        if hue is not None:
            new_df[hue] = df[hue]
        new_df = df
        df = df.fillna('NaN')
    nrows = len(col_lists) // ncols
    if len(col_lists) % ncols != 0:
        nrows += 1

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(7*ncols, 7*nrows))
    for i, c in enumerate(col_lists):
        if nrows > 1:
            ax = axes[i//ncols, i%ncols]
        else:
            ax = axes[i%ncols]
        sns.countplot(x=c, hue=hue, data=df, ax=ax)
        
        if annot:
            x_ticks = [x.get_text() for x in ax.get_xticklabels()]

            value_count = df[c].value_counts(dropna=dropna)
            value_count.index = value_count.index.astype(str)
            total = len(df[c])
            
            for p, t in zip(ax.patches, x_ticks):            
                height = p.get_height()
                if hue is not None:
                    #print(height)
                    txt = "%d (%.2f %%) / %d (%.2f %%)" % (height, height/total * 100,
                                                           value_count[t]-height, (value_count[t]-height)/total * 100)
                else:
                    txt = "%d (%.2f %%)" % (value_count[t], value_count[t]/total * 100)
                ax.text(p.get_x()+p.get_width()/2.,
                        height,
                        txt,
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

        if nrows > 1:
            ax = axes[i//ncols, i%ncols]
        else:
            ax = axes[i%ncols]
        sns.countplot(y=c, data=df[[c]], ax=ax)

        ax.title.set_text(c)

    
    plt.tight_layout()
    plt.show()
    
    
def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))
