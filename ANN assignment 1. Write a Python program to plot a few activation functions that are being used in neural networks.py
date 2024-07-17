import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha*x)

# Define range for x values
x = np.linspace(-5, 5, 100)

# Calculate activation functions
sigmoid_y = sigmoid(x)
relu_y = relu(x)
tanh_y = tanh(x)
leaky_relu_y = leaky_relu(x)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, sigmoid_y, label='Sigmoid', color='b')
plt.title('Sigmoid Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, relu_y, label='ReLU', color='r')
plt.title('ReLU Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, tanh_y, label='Tanh', color='g')
plt.title('Hyperbolic Tangent (Tanh) Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, leaky_relu_y, label='Leaky ReLU', color='m')
plt.title('Leaky ReLU Activation Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
