from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error
import streamlit as st
# Define the 'prediction()' function.
@st.cache()
def prediction(car_df, carwidth, enginesize, horsepower, drive_wheel_fwb, car_comp_buick):
  x = car_df.iloc[:,:-1]
  y = car_df['price']
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
  lin_reg = LinearRegression()
  lin_reg.fit(x_train,y_train) 
  score = lin_reg.score(x_train,y_train)
  price = lin_reg.predict([[car_width,engine_size,horse_power,drive_wheel_fwb,car_comp_buick]])
  price = price[0]
  y_test_predict = lin_reg.predict(x_test)
  test_r2_score = r2_score(y_test, y_test_predict)
  test_mae = mean_absolute_error(y_test, y_test_predict)
  test_msle = mean_squared_log_error(y_test, y_test_predict)
  test_rmse = np.sqrt(mean_squared_error(y_test, y_test_predict))
  return price, score, test_r2_score, test_mae, test_msle, test_rmse 