def mp_neuron(inputs, weights, threshold):
    """
    McCulloch-Pitts Neuron Model
    :param inputs: List of binary input values (0 or 1)
    :param weights: List of corresponding weights
    :param threshold: Threshold value for activation
    :return: 1 if the weighted sum of inputs exceeds the threshold, 0 otherwise
    """
    assert len(inputs) == len(weights), "Number of inputs must match number of weights"
    activation = sum(x * w for x, w in zip(inputs, weights))
    return 1 if activation >= threshold else 0

def andnot(x1, x2):
    """
    ANDNOT function implementation
    :param x1: First input
    :param x2: Second input
    :return: Output of the ANDNOT function
    """
    # Weights for inputs: 1 for x1 and -1 for x2
    weights = [1, -1]
    # Threshold set to 0
    threshold = 0
    return mp_neuron([x1, x2], weights, threshold)

# Test cases
print("ANDNOT(0, 0) =", andnot(0, 0))
print("ANDNOT(0, 1) =", andnot(0, 1))
print("ANDNOT(1, 0) =", andnot(1, 0))
print("ANDNOT(1, 1) =", andnot(1, 1))
