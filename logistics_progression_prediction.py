# PART 2 - Logistics Progression Prediction

import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Example model output
z = 1.72

prob = sigmoid(z)
print("Probability:", prob)

# Decision threshold = 0.5
if prob >= 0.5:
    print("Class: 1")
else:
    print("Class: 0")
