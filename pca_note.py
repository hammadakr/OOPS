import numpy as np

def pca_self(X, n_component):
  X_meaned = X-np.mean(X,axis=0)
  cov_matrix = np.cov(X_meaned.T)
  eig_values, eig_vectors = np.linalg.eig(cov_matrix)
  sorted_indices = np.argsort(eig_values)[::-1]
  eig_values = eig_values[sorted_indices]
  eig_vectors = eig_vectors[:, sorted_indices]
  selected_eig_vectors = eig_vectors[:, :n_component]
  reduced_value = np.dot(X_meaned, eig_vectors)
  return reduced_value, eig_values, eig_vectors

X = np.array([[5,10], [7,4], [12, 5], [8,13]])
n_component = 1

reduced_data,eig_values, eig_vectors = pca_self(X,n_component)

for i in range(0,n_component+1):
  print(f"\nPrinciple Component {i+1} : \n", reduced_data[:, i])
  print(f"\nEigen value {i+1} : \n", eig_values[i])
  print(f"\nEigen Vector {i+1} : \n", eig_vectors[:, i])
 