import pandas as pd
import numpy as np
from tqdm import tqdm
import copy

if __name__ == '__main__':
    df = pd.read_csv('F:\\used_car\\used_car_train_20200313.csv')
    r_df = []
    columns = df.columns[0].split(' ')
    print(columns)
    for i in tqdm(range(df.shape[0])):
        temp = []
        temp = ' '.join(str(i) for i in df.iloc[i]).split(' ')
        r_df.append(copy.copy(temp))
    r_df = pd.DataFrame(r_df)
    r_df.columns = columns
    r_df.index = r_df['SaleID']
    r_df = r_df.drop(r_df.columns.values.tolist()[0],axis=1)
    r_df.to_csv('F:\\used_car\\formatted_used_car_train_20200313.csv')

    df2 = pd.read_csv('F:\\used_car\\used_car_testA_20200313.csv')
    r_df = []
    columns = df2.columns[0].split(' ')
    for i in tqdm(range(df2.shape[0])):
        temp = []
        temp = ' '.join(str(i) for i in df2.iloc[i]).split(' ')
        r_df.append(copy.copy(temp))
    r_df = pd.DataFrame(r_df)
    r_df.columns = columns
    r_df.index = r_df['SaleID']
    r_df = r_df.drop(r_df.columns.values.tolist()[0],axis=1)
    r_df.to_csv('F:\\used_car\\formatted_used_car_testA_20200313.csv')
