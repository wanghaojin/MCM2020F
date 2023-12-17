import calculate

i = 20
j = 5
alpha = 0.6
P, M, g, d, A, S, e = calculate.generate_simulation_input(i, j)
print("P:",P)
print("M:",M)
X_optimal = calculate.greedy_optimization(i, j, alpha, P, M, g, d, A, S, e)
print("---------X_optimal:-------------")
print(X_optimal)
