import numpy as np


class CoffeeTeaANN:
    def __init__(self, coffee, tea, wother, sugre):
        self.coffee = coffee
        self.tea = tea
        self.wother = wother
        self.sugre = sugre

    def activation(self, signal):
        if signal >= 0.5:
            return 1
        else:
            return 0

    def predict(self):
        input_layer = np.array([self.coffee, self.tea, self.wother, self.sugre])

        weights_from_input_to_hidden_1 = [0.227, 0, 0.4, 0.32]
        weights_from_input_to_hidden_2 = [0.325, 0, 0.4, 0]
        weights_from_input_to_hidden_3 = [0, 0.256, 0.4, 0.256]
        weights_from_input_to_hidden_4 = [0, 0.42, 0.4, 0]

        weights_from_input_to_hidden = np.array([weights_from_input_to_hidden_1, weights_from_input_to_hidden_2,
                                                 weights_from_input_to_hidden_3, weights_from_input_to_hidden_4])

        weights_from_hidden_to_output = np.array([1, -1, -1, 1])

        hidden1_input = np.dot(weights_from_input_to_hidden, input_layer)
        print("hidden input ", hidden1_input)

        hidden1_output = np.array([self.activation(x) for x in hidden1_input])
        print("hidden1_output ", hidden1_output)
        hidden2_input = weights_from_hidden_to_output

        weights_from_input_to_hidden2_1 = [0.53, 0.32, 0, 0]
        weights_from_input_to_hidden2_2 = [0, 0, 0.32, 0.41]
        weights_from_input_to_hidden2 = np.array([weights_from_input_to_hidden2_1, weights_from_input_to_hidden2_2])
        weights_from_hidden2_to_output = np.array([-1,1])
        hidden2_input = np.dot(weights_from_input_to_hidden2, hidden2_input)
        print("hidden2 input ", hidden2_input)

        hidden2_output = np.array([self.activation(x) for x in hidden2_input])
        print("hidden2_output ", hidden2_output)

        output_input = np.dot(weights_from_hidden2_to_output, hidden2_output)
        print("output layer", output_input)

        output = self.activation(output_input)
        print("output ", output)
        if output == 1:
            print("tea")
        else:
            print("coffe")


model = CoffeeTeaANN(1, 0, 0,1)
model.predict()
