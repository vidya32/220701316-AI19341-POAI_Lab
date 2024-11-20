from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Generate sample data
X, y = make_circles(n_samples=1000, noise=0.05)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the MLP classifier
clf = MLPClassifier(max_iter=1500)  # Increased max_iter
clf.fit(X_train, y_train)

# Print R2 scores for training and test data
print("R2 Score for Training Data:", clf.score(X_train, y_train))
print("R2 Score for Test Data:", clf.score(X_test, y_test))

sns.scatterplot(x=X_train[:, 0], y=X_train[:, 1], hue=y_train)

plt.title("Train Data")
plt.show()

# Predict on the test data
y_pred = clf.predict(X_test)

# Visualize the results
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Combine data and hue for predicted data
data_pred = pd.DataFrame({"x": X_test[:, 0], "y": X_test[:, 1], "class": y_pred})
sns.scatterplot(data=data_pred, x="x", y="y", hue="class", ax=ax[0])
ax[0].set_title("Predicted Data")

# Combine data and hue for test data
data_test = pd.DataFrame({"x": X_test[:, 0], "y": X_test[:, 1], "class": y_test})
sns.scatterplot(data=data_test, x="x", y="y", hue="class", ax=ax[1])
ax[1].set_title("Test Data")

plt.show()
