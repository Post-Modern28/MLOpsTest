from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
import pickle

data = load_wine()
X, y = data.data, data.target
model = RandomForestClassifier()
model.fit(X, y)


with open('../../models/trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)
