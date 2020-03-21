import pandas as pd
import numpy as np
from tqdm import tqdm
import copy

if __name__ == '__main__':
    file_path = 'F:\\used_car\\'
    train_file = 'formatted_used_car_train_20200313.csv'
    test_file = 'formatted_used_car_testA_20200313.csv'
    pd.set_option('display.max_columns', None)
    df_train = pd.read_csv(file_path+train_file,header=0,index_col=0)
    df_test = pd.read_csv(file_path+test_file,header=0,index_col=0)
    df_view = [[],[]]
    columns = []
    for i in range(df_train.shape[1]):
        groupby_name = df_train.columns[i]
        if groupby_name == 'price':
            continue
        assert groupby_name!='price'
        columns.append(groupby_name)
        #print('\ngroupby '+groupby_name)
        ###单个特征最大出现次数
        #print('max count: ' + str(df_train.groupby(groupby_name)['price'].count().max()))
        df_view[0].append(copy.copy(df_train.groupby(groupby_name)['price'].count().max()))
        ###特征类总类型数量
        #print('numbers of index: '+str(df_train.groupby(groupby_name)['price'].count().count()))
        df_view[1].append(copy.copy(df_train.groupby(groupby_name)['price'].count().count()))
    df_view = pd.DataFrame(df_view)
    df_view.columns = columns
    df_view.index = ['max count','numbers of index']
    print(df_view.head(2))
    print('numbers of data:' + str(df_train.shape[0]))
