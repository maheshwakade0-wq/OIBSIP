# OIBSIP - Data Science Task 1: Iris Flower Classification
# Author: Mahesh Wakade

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
print(df.head())

# 2. Visualization
sns.pairplot(df, hue='species', palette='Set2')
# plt.show()

# 3. Train-Test Split
X = df.iloc[:, :-1]
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Training
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 5. Prediction & Evaluation
y_pred = model.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 6. Predict New Sample
sample = [[5.1, 3.5, 1.4, 0.2]] # Example - should be Setosa
prediction = model.predict(sample)
print(f"\nPredicted Species: {iris.target_names[prediction][0]}")
