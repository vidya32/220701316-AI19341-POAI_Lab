import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))

def plot_decision_boundary(X, y, model, title):
    X1, X2 = np.meshgrid(np.arange(X[:, 0].min()-1, X[:, 0].max()+1, 0.1),
                         np.arange(X[:, 1].min()-1, X[:, 1].max()+1, 0.1))
    
    plt.contourf(X1, X2, model.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha=0.75, cmap=ListedColormap(('red', 'green')))
    
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=ListedColormap(('red', 'green')))
    plt.title(title)
    plt.xlabel('Age')
    plt.ylabel('Estimated Salary')
    plt.show()
plot_decision_boundary(X_train, y_train, classifier, 'Decision Tree (Training set)')
plot_decision_boundary(X_test, y_test, classifier, 'Decision Tree (Test set)')
