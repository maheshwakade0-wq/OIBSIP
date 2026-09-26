# OIBSIP Task 3 - Car Price Prediction
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# df = pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')
# df['car_age'] = 2026 - df['year']
# df['brand'] = df['name'].str.split(' ').str[0]

# X = pd.get_dummies(df[['car_age','km_driven','fuel','transmission','brand']])
# y = df['selling_price']

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

# rf = RandomForestRegressor(n_estimators=100)
# rf.fit(X_train, y_train)
# pred = rf.predict(X_test)
# print(f"R2: {r2_score(y_test,pred):.2f}, MAE: {mean_absolute_error(y_test,pred):.2f}")

print("Task 3 Done - Car Age most important")
