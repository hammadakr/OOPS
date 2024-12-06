import numpy as np

def entropy(y):
    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    return -sum(p * np.log2(p) for p in probs)

def information_gain(y, y_left, y_right):
    p = len(y_left) / len(y)
    return entropy(y) - p * entropy(y_left) - (1 - p) * entropy(y_right)

def find_best_split(X, y):
    best_feature, best_threshold, best_gain = None, None, 0

    for feature in range(X.shape[1]):
        values = X[:, feature]
        unique_vals = np.unique(values)
        for threshold in unique_vals:
            left_idx = values < threshold
            y_left = y[left_idx]
            y_right = y[~left_idx]
            gain = information_gain(y, y_left, y_right)
            if gain > best_gain:
                best_feature, best_threshold, best_gain = feature, threshold, gain

    return best_feature, best_threshold, best_gain

def build_tree(X, y, max_depth=None, min_samples_split=2):
    if len(np.unique(y)) == 1 or len(y) < min_samples_split or (max_depth is not None and max_depth == 0):
        return unique_labels[np.bincount(y).argmax()]

    best_feature, best_threshold, best_gain = find_best_split(X, y)

    left_idx = X[:, best_feature] < best_threshold
    right_idx = ~left_idx

    left_tree = build_tree(X[left_idx], y[left_idx], max_depth - 1 if max_depth is not None else max_depth, min_samples_split)
    right_tree = build_tree(X[right_idx], y[right_idx], max_depth - 1 if max_depth is not None else max_depth, min_samples_split)

    return [best_feature, best_threshold, left_tree, right_tree]

def predict(X, tree):
    if isinstance(tree, str):
        return tree

    feature, threshold, left_tree, right_tree = tree
    if X[feature] < threshold:
        return predict(X, left_tree)
    else:
        return predict(X, right_tree)
    
data = np.array([
    [0, 0, 1, 1, "Non-mammal"],
    [0, 1, 0, 0, "Non-mammal"],
    [1, 0, 0, 0, "Non-Mammal"],
    [1, 0, 0, 1, "Mammal"],
    [1, 0, 1, 1, "Mammal"],
])

unique_labels, y = np.unique(data[:, -1], return_inverse=True)
X = data[:, :-1].astype(int)

tree = build_tree(X, y, max_depth=3)
print(tree)

new_sample = np.array([1, 1, 0, 0])
prediction = predict(new_sample, tree)
print(f"Prediction for the new sample: {prediction}")