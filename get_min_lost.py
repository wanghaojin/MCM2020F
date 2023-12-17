import calculate

i = 50
j = 5
alpha = 0.6
P, M, g, d, A, S, e = calculate.generate_simulation_input(i, j)
X_optimal, minimum_cost = calculate.solve_optimization_problem(i, j, alpha, P, M, g, d, A, S, e)
print("P:",P)
print("M:",M)
print("---------X_optimal:-------------")
print(X_optimal)
print("--------------------------------")
print("minimum_cost:", minimum_cost)
