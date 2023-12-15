import random
import numpy as np
def discrete_linear_map(value, old_min, old_max, new_min=2, new_max=30, step=2):
    if value > 0:
        mapped_value = ((old_max - value) / (old_max - old_min)) * (new_max - new_min) + new_min
        discrete_mapped_value = round(mapped_value / step) * step
        return max(new_min, min(discrete_mapped_value, new_max))
    else:
        discrete_value = int(np.clip(np.random.normal(25, 10), 2, 50) // 2 * 2)
        return discrete_value
        
a = 0 
b = 120
step = 2  

mapped_a = discrete_linear_map(a, a, b, 2, 30, step)
mapped_b = discrete_linear_map(b, a, b, 2, 30, step)

print(f"映射后的a: {mapped_a}")
print(f"映射后的b: {mapped_b}")
for x in range(50):
    # value = random.uniform(-120,b)
    # value = 0 if value < 0 else value
    value = 0
    print(value,":",discrete_linear_map(value,a,b,2,30,step))