import numpy as np

def generate_simulation_input(i, j):
    np.random.seed(0)
    M = np.random.randint(500, 2000, size=j)
    P = np.random.randint(100, 500, size=i)
    g = np.random.random(size=j)
    d = np.random.random(size=(i, j))
    A = np.random.randint(0, 2, size=(i, j))
    S = np.random.random(size=(i, j))
    e = np.random.random(size=j)
    return P, M, g, d, A, S, e

def greedy_optimization(i, j, alpha, P, M, g, d, A, S, e):
    X = np.zeros((i, j), dtype=int)
    island_indices = np.argsort(-P)
    country_indices = np.argsort(-M)
    for island in island_indices:
        refugees = P[island]
        for country in country_indices:
            if M[country] >= refugees:
                X[island, country] = refugees
                M[country] -= refugees
                break
            else:
                X[island, country] = M[country]
                refugees -= M[country]
                M[country] = 0
                while refugees > 0:
                    if index < 0:
                        assert("False!Countries can't help so many edps!")
                    index = len(country_indices) - 1
                    refugees -= M[country_indices[index]]
                    M[country_indices[index]] = 0
                    index -= 1
        country_indices = np.argsort(-M)

    return X
