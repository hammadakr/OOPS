import numpy as np

X = np.array([[5, 10], [7, 4], [12, 5], [8, 13]])

def perform_pca(data, n_components):
    data_meaned = data - np.mean(data, axis=0)
 
    covariance_matrix = np.cov(data_meaned.T)

    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    selected_eigenvectors = eigenvectors[:, :n_components]

    reduced_data = np.dot(data_meaned, selected_eigenvectors)

    return reduced_data, eigenvalues, selected_eigenvectors

n_components = 1
reduced_data, eigenvalues, eigenvectors = perform_pca(X, n_components)

print("Reduced Data:\n", reduced_data)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)