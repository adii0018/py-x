A = np.array([[4, -2],
              [1, 1]])

values, vectors = np.linalg.eig(A)

print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
