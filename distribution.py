import score
from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import Counter

mark = []
max_score = 0
min_score = 1000

print("---------------init:---------------")
for person in tqdm(range(200000)):
    mark.append(score.init())
    max_score = mark[-1] if max_score <= mark[-1] else max_score
    min_score = mark[-1] if min_score >= mark[-1] else min_score

print("---------------init done!----------")
print("---------------map:----------------")
for person in tqdm(range(200000)):
    mark[person] = score.discrete_linear_map(mark[person], min_score, max_score)

print("--------------map done!------------")

count = Counter(mark)
values, counts = zip(*sorted(count.items()))

plt.bar(values, counts, width=1.5)
plt.xlabel('year')
plt.ylabel('popularity')
plt.title('when to transform')
plt.savefig('year.png')
plt.close()
