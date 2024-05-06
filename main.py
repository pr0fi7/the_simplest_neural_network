import numpy as np

class NeuralNetwork:
    def __init__(self):
        # Seed the random number generator for reproducibility
        np.random.seed(1)

        # Initialize weights randomly with mean 0
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    # Sigmoid activation function
    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Derivative of the sigmoid function
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Train the neural network
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Forward pass
            output = self.think(training_set_inputs)

            # Calculate error
            error = training_set_outputs - output

            # Backpropagation
            adjustment = np.dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Update weights
            self.synaptic_weights += adjustment

    # Perform forward pass
    def think(self, inputs):
        return self.__sigmoid(np.dot(inputs, self.synaptic_weights))


if __name__ == "__main__":
    # Initialize neural network
    neural_network = NeuralNetwork()

    print("Random starting synaptic weights:")
    print(neural_network.synaptic_weights)

    # Define the training set
    training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = np.array([[0, 1, 1, 0]]).T

    # Train the neural network
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print("New synaptic weights after training:")
    print(neural_network.synaptic_weights)

    # Test the neural network with a new situation
    print("Considering new situation [1, 0, 0] -> ?:")
    print(neural_network.think(np.array([1, 0, 0])))
