import numpy as np
import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
import tensorflow as tf
# from torch import *
# from keras import *
from tensorflow.keras import Sequential
class CarDekho:
    """CarDekho 2020 Data Analysis and Predictions"""
    def __init__(self,sales):
        self.sales=sales
    def data(sales):
        sales = pd.read_csv('data/cars_dataset.csv')
        print(sales.head())
        print(sales.describe())
    def model(model):
        model.sales_model=sales_model
        