#%%
import numpy as np
import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# load datasets of titanics from seaborn
titanic = sns.load_dataset('titanic')

# %%
# summary of the data
titanic.info()
# describe of the data
titanic.describe()
# count of the missing values of all columns in the data
titanic.isnull().sum()
# %%
