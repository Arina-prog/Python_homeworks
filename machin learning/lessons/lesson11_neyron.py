import numpy as np


class GoToWalkANN:
    def __init__(self, weather, mood, friends):
        self.weather = weather
        self.mood = mood
        self.friends = friends

    def activation(self, signal):
        if signal >= 0.5:
            return 1
        else:
            return 0

    def predict(self):
        input_layer = np.array([self.weather, self.mood, self.friends])

        weights_from_input_to_hidden_1 = [0.227, 0.268, 0]
        weights_from_input_to_hidden_2 = [0, 0.150, 0.354]

        weights_from_input_to_hidden = np.array([weights_from_input_to_hidden_1, weights_from_input_to_hidden_2])

        weights_from_hidden_to_output = np.array([-1, 1])

        hidden_input = np.dot(weights_from_input_to_hidden, input_layer)
        print("hidden input ", hidden_input)

        hidden_output = np.array([self.activation(x) for x in hidden_input])
        print("hidden_output ", hidden_output)

        output_input = np.dot(weights_from_hidden_to_output, hidden_output)
        print("output layer", output_input)

        output = self.activation(output_input)
        print("output ", output)
        if output == 1:
            print("go to walk")
        else:
            print("don't go")


model = GoToWalkANN(0, 1, 0)
model.predict()





