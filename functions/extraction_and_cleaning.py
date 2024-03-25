import pandas as pd 
import glob

def read_my_csv_files(path):
    filenames = glob.glob(path + "/*.csv")
    return  [pd.read_csv(i) for i in filenames]

def combine_df_list(list):
    return pd.concat(list)

def read_bronze():
    return  combine_df_list(read_my_csv_files("data/bronze"))
