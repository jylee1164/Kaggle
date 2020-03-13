import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl

import os
import pickle as pkl
import glob
import itertools

#from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, FunctionTransformer
import category_encoders as ce

#import da_func
#import data_preprocessing

%load_ext autoreload
%autoreload 2

root_path = '../../'
data_path = root_path + 'data/'

with open(root_path + 'etc/encoders/encoders.pkl', 'rb') as f:
    encoders = pkl.load(f)
    
with open(root_path + 'etc/encoders/encoding_functions.pkl', 'rb') as f:
    all_data = pkl.load(f)
    

train_df = pd.read_csv(data_path + 'org/train.csv')
test_df = pd.read_csv(data_path + 'org/test.csv')


for element in itertools.product(*all_data.values()):
    print(element)
    
    filename = ''
    
    new_train = train_id.copy()
    new_test = test_id.copy()
    
    for i, c in enumerate(all_data.keys()):
        tr_tmp = all_data[c][element[i]](train_df)
        ts_tmp = all_data[c][element[i]](test_df)
        
        new_train = pd.concat([new_train, tr_tmp], axis=1)
        new_test = pd.concat([new_test, ts_tmp], axis=1)
        
        filename = filename + '_' + element[i]

    filepath = data_path + 'encoded/' + filename[1:] + '/'
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    new_train.to_csv(filepath + 'train.csv', index=False)
    
    new_test.to_csv(filepath + 'test.csv', index=False)
