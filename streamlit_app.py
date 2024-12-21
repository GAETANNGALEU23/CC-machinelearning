import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

#chargement des donnees
def load_data():
    train = pd.read_csv("train.csv")
    test = pd.read.csv("test.csv")
    return train, test

train, test = load_data() 

