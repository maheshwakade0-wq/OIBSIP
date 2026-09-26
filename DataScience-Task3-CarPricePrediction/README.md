# Task 3 - Car Price Prediction with Machine Learning

Objective: Predict selling price of used car from features like brand, year, km driven, fuel type, transmission.

Dataset: Kaggle - Vehicle Dataset from CarDekho
Link: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

Tech Stack: Python, Pandas, Scikit-learn, Matplotlib, Seaborn

Steps:
- Data Cleaning: null handling, duplicate removal, Petrol/petrol fix
- Feature Engineering: Car Age = Current Year - Year, Brand from Name
- EDA: Selling price distribution, Price vs Fuel (Box plot), Price vs Car Age (Scatter)
- Encoding: One-Hot for fuel, transmission, seller_type
- Correlation heatmap
- Train/Test split (80/20)
- Models: Linear Regression, Random Forest Regressor
- Evaluation: MAE, RMSE, R2 Score
- Feature Importance chart for best model

Result: Random Forest performed best. Car Age and Brand are top factors for price.

Author: Mahesh Wakade - OIBSIP Data Science
