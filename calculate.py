import numpy as np

def generate_simulation_input(i, j):
    """
    生成模拟输入数据，确保所有岛屿的难民总数量小于等于所有国家容纳难民的总数量。

    参数:
    i : 岛屿数量
    j : 国家数量

    返回:
    P, M, g, d, A, S, e
    """
    np.random.seed(0)  # 设置随机种子以保证可重复性

    # 各个国家能容纳难民的最高数量 (M)
    M = np.random.randint(500, 5000, size=j)

    # 确保所有岛屿的难民总数量小于等于所有国家容纳难民的总数量
    total_capacity = np.sum(M)
    P = np.random.randint(100, total_capacity // i + 1, size=i)

    # 各个国家的 GDP (g)
    g = np.random.random(size=j)

    # 各个岛屿到各个国家的距离 (d)
    d = np.random.random(size=(i, j))

    # 各个岛屿与各个国家语言是否相通 (A)
    A = np.random.randint(0, 2, size=(i, j))

    # 各个岛屿与各个国家气候相似度 (S)
    S = np.random.random(size=(i, j))

    # 各个国家的碳排放数量 (e)
    e = np.random.random(size=j)

    return P, M, g, d, A, S, e

def calculate_cost(X, g, d, A, S, e, P, alpha):
    # 计算成本矩阵 C
    C = g * np.log(d + A + S + 2.8)

    # 计算文化保存程度 Z
    Z = np.sum(X / P[:, None], axis=1)

    # 定义目标函数
    objective_value = alpha * np.sum(C * X) + (1 - alpha) * np.sum(Z) * np.sum(C) / (X.shape[0] * X.shape[1])
    return objective_value

def get_neighbor(X, i, j, P, M):
    new_X = np.copy(X)
    # 示例：随机选择一个岛屿，改变其难民的分配
    island = np.random.choice(i)
    new_X[island, :] = 0
    country = np.random.choice(j)
    new_X[island, country] = P[island]
    return new_X

def solve_optimization_problem(i, j, alpha, P, M, g, d, A, S, e):
    # 初始化
    current_solution = np.zeros((i, j))
    for idx, p in enumerate(P):
        current_solution[idx, np.random.choice(j)] = p  # 初始分配

    best_solution = np.copy(current_solution)
    current_cost = calculate_cost(current_solution, g, d, A, S, e, P, alpha)
    best_cost = current_cost

    T = 1.0  # 初始温度
    T_min = 0.00001  # 最小温度
    alpha_temp = 0.9  # 温度下降率

    while T > T_min:
        for _ in range(100):  # 在当前温度下尝试若干次
            new_solution = get_neighbor(current_solution, i, j, P, M)
            new_cost = calculate_cost(new_solution, g, d, A, S, e, P, alpha)
            cost_diff = new_cost - current_cost

            # 接受更好的解，或以一定概率接受更差的解
            if cost_diff < 0 or np.random.rand() < np.exp(-cost_diff / T):
                current_solution = new_solution
                current_cost = new_cost
                if current_cost < best_cost:
                    best_solution = current_solution
                    best_cost = current_cost

        T *= alpha_temp  # 降低温度

    return best_solution, calculate_cost(best_solution, g, d, A, S, e, P, alpha)