import random
import numpy as np
def getscore(Distance,Language,Climate,Ecolomy,Acquaintance):
    if Acquaintance == 1:
        return Distance + Language + Climate + Ecolomy
    else:
        return 0    
    
def init():
    Distance = random.gauss(25,5)
    Language = 30 if random.uniform(0,1) <= 0.7 else 0
    Climate = random.gauss(15,5)
    Ecolomy = random.gauss(15,25)
    Acquaintance = 1 if random.uniform(0,1) <= 0.5 else 0
    return getscore(Distance,Language,Climate,Ecolomy,Acquaintance)

def discrete_linear_map(value, old_min, old_max, new_min=2, new_max=30, step=2):
    if value > 0:
        mapped_value = ((old_max - value) / (old_max - old_min)) * (new_max - new_min) + new_min
        discrete_mapped_value = round(mapped_value / step) * step
        return max(new_min, min(discrete_mapped_value, new_max))
    else:
        discrete_value = int(np.clip(np.random.normal(25, 10), 2, 50) // 2 * 2)
        return discrete_value

    
    