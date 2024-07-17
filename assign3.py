import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation >= 0 else 0

    def train(self, training_inputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Define training data and labels for even and odd numbers (in ASCII)
training_data = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # ASCII for 0
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # ASCII for 2
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # ASCII for 4
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # ASCII for 6
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],  # ASCII for 8
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # ASCII for 1
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # ASCII for 3
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # ASCII for 5
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1],  # ASCII for 7
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1]   # ASCII for 9
])
labels = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])  # 1 for even, 0 for odd

# Initialize and train the perceptron
perceptron = Perceptron(input_size=10)
perceptron.train(training_data, labels)

# Test the perceptron
test_cases = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # ASCII for 0 (even)
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # ASCII for 2 (even)
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # ASCII for 9 (odd)
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1]   # ASCII for 7 (odd)
]

for test_case in test_cases:
    prediction = perceptron.predict(test_case)
    number_ascii = ''.join([str(bit) for bit in test_case])
    number_decimal = int(number_ascii, 2)
    print(f"The perceptron predicts that the ASCII number {number_ascii} (decimal: {number_decimal}) is {'even' if prediction == 1 else 'odd'}.")
