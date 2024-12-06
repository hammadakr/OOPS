import random

def calculate_distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def calculate_centroid(cluster):
    x_sum, y_sum = 0, 0
    for point in cluster:
        x_sum += point[0]
        y_sum += point[1]
    return [x_sum / len(cluster), y_sum / len(cluster)]

def k_means_clustering(k, data, max_iterations=100):

    centroids = random.sample(data, k)

    for iteration in range(max_iterations):
        clusters = [[] for _ in range(k)]


        for point in data:
            distances = [calculate_distance(point, centroid) for centroid in centroids]
            nearest_centroid_index = distances.index(min(distances))
            clusters[nearest_centroid_index].append(point)

        new_centroids = [calculate_centroid(cluster) for cluster in clusters]

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return clusters, centroids

def predict(q, centroids):
    distances = [calculate_distance(q, centroid) for centroid in centroids]
    nearest_centroid_index = distances.index(min(distances))
    return nearest_centroid_index

data = [
    [4, 3], [6, 7], [7, 8], [5, 5], [8, 8],
    [9, 6], [10, 10], [4, 2], [6, 5], [7, 9],
    [5, 7], [8, 7], [9, 9], [10, 8], [3, 3],
    [4, 4], [5, 6], [6, 9], [7, 10], [9, 5]
]

k = 3

clusters, centroids = k_means_clustering(k, data)

print(f"Final centroids Values: {centroids}\n")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")

q = [8, 5]
predicted_cluster = predict(q, centroids)
print(f"\nThe point {q} belongs to Cluster {predicted_cluster + 1}")