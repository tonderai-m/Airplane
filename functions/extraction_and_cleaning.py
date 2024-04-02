"""This is having some issues when reading the data frame and keeping everything together something wrong"""
import pandas as pd 
import glob

def read_my_csv_files(path):
    filenames = glob.glob(path + "/*.csv")
    return  [pd.read_csv(i, encoding='utf-8') for i in filenames]

def combine_df_list(list):
    return pd.concat(list, ignore_index=True, axis=0, join='outer',)

def read_bronze():
    return  combine_df_list(read_my_csv_files("data/bronze"))

