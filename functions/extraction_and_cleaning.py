"""Load & Combine DataFrame"""
import glob
import pandas as pd

def read_my_csv_files(path):
    """return pandas list of DataFrames"""
    filenames = glob.glob(path + "/*.csv")
    return  [pd.read_csv(i, encoding='utf-8') for i in filenames]

def combine_df_list(lis):
    """return one giant DataFrame"""
    return pd.concat(lis, ignore_index=True, axis=0, join='outer')

def read_bronze():
    """return full DataFrame"""
    return  combine_df_list(read_my_csv_files("data/bronze"))