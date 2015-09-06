import prodmaketrain

res = prodmaketrain.main()
X = res[0]
y = res[1]
print(X[0])
print(len(X[0]))

# DOCS
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

# Build a classification task using 3 informative features
#X, y = make_classification(n_samples=900,
#                           n_features=9,
#                           n_informative=3,
#                           n_redundant=0,
#                           n_repeated=0,
#                           n_classes=2,
#                           random_state=0,
#                           shuffle=False)

# Build a forest and compute the feature importances
forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(X, y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# HEADERS
header = ['max','median', 'average', 'sumsqtot', 'sumsq25', 'sumsq75', 'std', 'sumdiff']

# Print the feature ranking
print("Feature ranking:")

for f in range(8):
    print("%d. feature %d (%s) (%f)" % (f + 1, indices[f], header[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(9), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(9), indices)
plt.xlim([-1, 9])
plt.show()
