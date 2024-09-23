from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

data = load_iris()
X, y = data.data, data.target
model = RandomForestClassifier()
model.fit(X, y)

with open('../../models/trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)
