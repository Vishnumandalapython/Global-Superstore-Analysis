import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import logging
from log_code import setup_logging
import sys
# Create logger for this script
logger = setup_logging("main")

path = 'C:\\Users\\vishn\\Downloads\\Retail_Analysis_Project\\Global_Superstore2.csv.zip'






df = pd.read_csv(path,compression='zip', encoding='latin1')



# ---------- Load Dataset ----------
try:
    path = 'C:\\Users\\vishn\\Downloads\\Retail_Analysis_Project\\Global_Superstore2.csv.zip'
    logger.info("Loading dataset...")

    df = pd.read_csv(path, compression='zip', encoding='latin1')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    logger.info(f"\n{df.head()}")
    logger.info(f"Dataset loaded successfully with shape {df.shape}")
    logger.info(f"Columns: {list(df.columns)}")
    df.info()

    logger.info(f'the head of the dataframe: {df.head()}')
    logger.info(f'null values : {df.isnull().sum()}')

    colms_to_drop = ['Row ID',
    'Customer ID',
    'Product ID']
    df.drop(columns = colms_to_drop, inplace = True)
    df.drop("Postal Code",axis= 1, inplace = True)
    logger.info(f'drop null values : {df.dropna().isnull().sum()}')
    logger.info(f'the null values are drop')


    df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst = True)
    df['Ship Date'] =  pd.to_datetime(df['Ship Date'],dayfirst= True)
    logger.info(f'null values : {df.describe()}')


    df['Shipping_days']= (df['Ship Date'] - df['Order Date']).dt.days
    df['Profit_Margin'] = df['Profit'] / df['Sales']
    logger.info(f'shape after : {df.shape}')

    df['Order year'] =df['Order Date'].dt.year
    df['Order month'] = df['Order Date'].dt.month
    df['Order month_name'] = df['Order Date'].dt.month_name()
    df['Order quarter'] = df['Order Date'].dt.quarter
    logger.info(f'the sample of the  data  set {df.sample(3)}')
    #-----------------------------------------------------------------------------
    logger.info(f'the duplicates of the  data  set {df.duplicated().sum()}')
    print("Total Sales:", df['Sales'].sum())
    print("Total Profit:", df['Profit'].sum())
    print("Total Orders:", df['Order Date'].nunique())

    print("region sales :", df.groupby('Region')['Sales'].sum().sort_values(ascending=False))
    print("region profit :", df.groupby('Profit')['Sales'].sum().sort_values(ascending=False))

    print(df.groupby('Category')['Profit'].sum().sort_values(ascending=False))
    print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))
    print(df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False))

    print(df[df['Profit'] < 0].groupby('Sub-Category')['Profit'].sum().sort_values())
    print(df.columns)
    print(df.shape)
    #shipping operations
    print(df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10))


    df['Shipping_days'] =  (df['Ship Date'] - df['Order Date']).dt.days
    print(df['Shipping_days'].head(5))

    df.to_csv("cleaned_superstore_data.csv", index=False)


    df.to_csv(r"C:\\Users\\vishn\\Downloads\\Retail_Analysis_Project\\cleaned_superstore_data.csv", index=False)


except Exception:
    logger.exception("Error loading dataset")
    error_type, error_msg, error_line = sys.exc_info()
    logger.info(f'line no {error_line.tb_lineno}: due to{error_msg}')

