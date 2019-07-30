import numpy as np

################################
## MOMENTS POINT ESTIMATE NORMAL
################################

n = 1000000
X = np.random.normal(loc=75, scale=10, size=n)

m1 = sum(X) / n
m2 = sum( X **2 ) / n

mu = m1
sig = np.sqrt(m2 - mu ** 2)

print('Estimate:')
print(f'  mu = {mu}')
print(f'  sig = {sig}')