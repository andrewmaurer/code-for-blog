import numpy as np

################################
## MOMENTS POINT ESTIMATE NORMAL
################################

n = 1000000
X = np.random.normal(loc=75, scale=10, size=n)

m1 = sum(X) / n
m1 = sum(X) / n

mu = m1
sig = np.sqrt(m2 - mu ** 2)

print('Estimate:')
print(f'  mu = {mu}')
print(f'  sig = {sig}')

#################################
## MOMENTS POINT ESTIMATION BINOMIAL
#################################

n = 10000
X = np.random.binomial(n=100, p=0.2, size=n)

m1 = sum(X) / n
m2 = sum( X ** 2 ) / n

p = 1 - ( m2 - m1 ** 2 ) / m1
k = m1 / p

print('Estimate:')
print(f'  k = {k}')
print(f'  p = {p}')


################################
## MOMENTS POINT ESTIMATE UNIFORM
################################

n = 10000
X = np.random.uniform(low=50, high=100, size=n)

m1 = sum(X) / n
m1 = sum(X) / n



print('Estimate:')
print(f'  a = {a}')
print(f'  b = {b}')

