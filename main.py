import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

weight_mean = df['Weight(Pounds)'].mean()
print("The mean of the weight is : "+str(weight_mean))

weight_median = df['Weight(Pounds)'].median()
print("The median of the weight is : "+str(weight_median))

weight_mode = df['Weight(Pounds)'].mode()
print("The mode of the weight is : "+str(weight_mode))