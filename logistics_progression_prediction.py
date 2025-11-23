import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def logistic_regression_prediction(z, threshold=0.5):
    # Compute probability using sigmoid
    prob = sigmoid(z)

    # Classification decision
    if prob >= threshold:
        decision = 1
    else:
        decision = 0


    # Output
    print("Linear output z:", z)
    print("Probability:", prob)
    print("Predicted class:", decision)

# Example
z = 1.72
logistic_regression_prediction(z)
