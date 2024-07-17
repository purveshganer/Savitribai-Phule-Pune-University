import numpy as np

class ARTNetwork:
    def __init__(self, input_size, vigilance_parameter):
        self.input_size = input_size
        self.vigilance_parameter = vigilance_parameter
        self.W = None
        self.reset()

    def reset(self):
        self.W = np.random.rand(self.input_size)

    def normalize(self, X):
        norm = np.linalg.norm(X)
        if norm == 0:
            return X
        return X / norm

    def match(self, X):
        return np.dot(self.W, self.normalize(X))

    def learn(self, X, max_iterations=100):
        for _ in range(max_iterations):
            y = self.match(X)
            if y >= self.vigilance_parameter:
                return True
            else:
                self.W = np.maximum(self.W, X)
                self.W = self.normalize(self.W)
        return False

input_size = 4
vigilance_parameter = 0.9
art_net = ARTNetwork(input_size, vigilance_parameter)

data = [
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
]

for pattern in data:
    art_net.learn(pattern)
]

test_patterns = [
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]
]

print("Test Results:")
for pattern in test_patterns:
    match = art_net.match(pattern)
    print(f"Pattern: {pattern}, Match: {match}")
