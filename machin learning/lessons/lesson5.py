from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

wheather = ["sunny", "sunny", "rain", "overcast", "rain", "rain"]
temperature = ["hot", "warm", "cold", "zov", "warm", "cold"]
game = ["yes", "no", "yes", "yes", "no", "no"]

le = LabelEncoder()
wheather_encoded = le.fit_transform(wheather)
temperature_encoded = le.fit_transform(temperature)
game_encoded = le.fit_transform(game)
# print(wheather_encoded, "\n", temperature_encoded, "\n", game_encoded)
# features = zip(wheather_encoded, temperature_encoded)
# print(list(features))
label = game_encoded
features = zip(wheather_encoded, temperature_encoded)
model = GaussianNB()
model.fit(list(features), label)
print(model.predict([[0, 1]]))

