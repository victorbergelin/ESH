import prodmaketrain
import numpy as np

res = prodmaketrain.main()
X = [x[1:] for x in res[0]]
Y = [y[1:] for y in res[1]]

NUMFEATS = len(X[0])
print("Number of variabiables is: " + str(NUMFEATS))

# DOCS
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

# Build a forest and compute the feature importances
forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(X, Y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# HEADERS
header = ['max','median', 'average', 'sumsqtot', 'sumsq25', 'sumsq75', 'std', 'sumdiff']

# Print the feature ranking
print("Feature ranking:")

for f in range(NUMFEATS):
    print("%d. feature %d (%s) (%f)" % (f + 1, indices[f], header[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(NUMFEATS), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(NUMFEATS), indices)
plt.xlim([-1, NUMFEATS])
plt.show()
