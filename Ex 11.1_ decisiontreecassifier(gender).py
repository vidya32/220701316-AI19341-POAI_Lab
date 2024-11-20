from sklearn import tree 
 
clf = tree.DecisionTreeClassifier() 
X=[[181, 80, 91], [182, 90, 92], [183, 100, 92], [184, 200, 93], [185, 300, 94], [186,
 400, 95], [187, 500, 96], [189, 600, 97], [190, 700, 98], [191, 800, 99], [192, 900, 100],
 [193, 1000, 101]] 
Y=['male', 'male', 'female', 'male' , 'female', 'male', 'female' , 'male' , 'female', 'male' ,
 'female' , 'male' ] 
clf = clf.fit(X, Y) 

predictionf = clf.predict([[181, 80, 91]])
predictionm = clf.predict([[183, 100, 92]])

print(predictionf)
print(predictionm)
