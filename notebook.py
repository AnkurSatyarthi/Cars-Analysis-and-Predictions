import numpy as np
import pandas as pd
# from torch import *
# from keras import *
try:
    # class CarDekho:
    #     """CarDekho 2020 Data Analysis and Predictions"""
    #     def __init__(self,sales):
    #         self.sales=sales
    #     def data(sales):
    #         sales = pd.read_csv('data/cars_dataset.csv')
    #         print(sales.head())
    #         print(sales.describe())
    #     def model(model):
    #         model.sales_model=sales_model
    sales=pd.read_csv('data/cars_dataset.csv')
    # print(sales.describe())
    # print(sales.head())
    print(sales)
    # y=sales

except:
    # import tensorflow as tf
    # from tensorflow.keras import Sequential
    # from tensorflow.keras.layers import Dense
    sales=pd.read_csv('data/cars_dataset.csv')
    sales.describe();
    # model=Sequential([Dense(units=1)])    