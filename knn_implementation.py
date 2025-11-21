# PART 2 - KNN Implementation

import math

# --- BONUS: Normalization Function ---
def normalize_data(data):
    # data is a list of points: [ [features], label ]
    # Extract all features into columns
    num_features = len(data[0][0])
    mins = [float('inf')] * num_features
    maxs = [float('-inf')] * num_features
    
    # Find min and max for each feature
    for features, _ in data:
        for i in range(len(features)):
            mins[i] = min(mins[i], features[i])
            maxs[i] = max(maxs[i], features[i])
    
    # Apply normalization (min-max scaling)
    normalized = []
    for features, label in data:
        norm_features = []
        for i in range(len(features)):
            if maxs[i] == mins[i]:  # avoid division by zero
                norm_features.append(0)
            else:
                norm_features.append((features[i] - mins[i]) / (maxs[i] - mins[i]))
        normalized.append((norm_features, label))
    
    return normalized


# --- KNN Prediction Function ---
def predict_knn(new_point, data, k, normalize=False):

    # Optional: Normalize data
    if normalize:
        data = normalize_data(data)
        # Normalize new point using same scaling logic
        # Extract mins and maxs again
        num_features = len(new_point)
        mins = [min(item[0][i] for item in data) for i in range(num_features)]
        maxs = [max(item[0][i] for item in data) for i in range(num_features)]

        new_point = [
            (new_point[i] - mins[i]) / (maxs[i] - mins[i]) if maxs[i] != mins[i] else 0
            for i in range(num_features)
        ]

    # Step 1: Compute distances
    distances = []
    for features, label in data:
        dist = math.dist(new_point, features)
        distances.append((dist, label))

    # Step 2: Sort by distance
    distances.sort(key=lambda x: x[0])

    # Step 3: Get k nearest labels
    neighbors = [distances[i][1] for i in range(k)]

    # Step 4: Majority vote
    prediction = max(set(neighbors), key=neighbors.count)
    return prediction


# --- SAMPLE DATA ---
# Format: ([features], label)
dataset = [
    ([5.1, 3.5], "A"),
    ([4.9, 3.0], "A"),
    ([6.2, 3.4], "B"),
    ([5.9, 3.0], "B"),
]

new_point = [5.5, 3.2]

print("Prediction:", predict_knn(new_point, dataset, k=3, normalize=True))
