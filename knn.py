def calculate_distance(q, x):
    return (q[0] - x[0]) ** 2 + (q[1] - x[1]) ** 2

x = [
    [4, 3], [6, 7], [7, 8], [5, 5], [8, 8],
    [9, 6], [10, 10], [4, 2], [6, 5], [7, 9],
    [5, 7], [8, 7], [9, 9], [10, 8], [3, 3],
    [4, 4], [5, 6], [6, 9], [7, 10], [9, 5]
]

y = [
    0, 1, 1, 0, 1,
    1, 1, 0, 0, 1,
    0, 1, 1, 1, 0,
    0, 0, 1, 1, 1
]

def knn(q, k):
    n = len(x)
    distances = [(calculate_distance(q, x[i]), i) for i in range(n)]
    distances.sort()
    k_nearest = distances[:k]
    votes = [y[i] for _, i in k_nearest]
    return max(set(votes), key=votes.count)

q = [1, 2]
k = 5

result = knn(q, k)
print("FAIL" if result == 0 else "PASS")