from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
X, y = make_regression(n_samples=1000, noise=0.05, n_features=100)
X_shape = X.shape
y_shape = y.shape
if X_shape == (1000, 100) and y_shape == (1000,):
    print("Shapes are correct!")
else:
    print(f"Shapes mismatch! X.shape: {X_shape}, y.shape: {y_shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=42)
clf = MLPRegressor(max_iter=1000)
clf.fit(X_train, y_train)
print(f"R2 Score for Training Data = {clf.score(X_train, y_train)}")
print(f"R2 Score for Test Data = {clf.score(X_test, y_test)}")
