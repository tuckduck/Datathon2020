from sklearn.linear_model import ElasticNetCV
from sklearn.datasets import make_regression

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

import numpy as np
data = np.genfromtxt('output.csv', delimiter=',')

params = {'max_depth':range(1,7,2),"max_leaf_nodes":[None,5000]}

caus_sep_data = []

for i in range(1,14,1):
	caus_sep_data.append(data[data[:,0] == i])
for i in range(13):
	data2 = caus_sep_data[i]

	print(str(i) + "------")
	X = data2[:, 1:5]
	y = data2[:, 5]
	y = y.astype(int)
	rfc = RandomForestClassifier(n_estimators = 20)
	print("cross validating")
	rfcCV = GridSearchCV(rfc, params)
	print("validated")

	rfcCV.fit(X, y)

	y_pred = rfcCV.predict(X)

	print(accuracy_score(y, y_pred))
	