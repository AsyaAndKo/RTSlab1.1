import numpy as np
import random
from math import sin
import matplotlib.pyplot as plt


# expected value
def expectation(x, N):
    return np.sum(x)/N


# standard deviation
def dispersion(x, mx, N):
    return np.sum((x - mx)**2)/N


def frequency(n, w):
    return w - n * number


# values for 11 variant
n = 10
w = 1500
N = 256
number = w/(n - 1)

# frequency
w_values = [frequency(n, w) for n in range(n)]
harmonics = np.zeros((n, N))
resulted = np.array([])

# generating harmonics
for n in range(n):
    amplitude = random.choice([i for i in range(-10, 10) if i != 0])
    phi = random.randint(-360, 360)
    for t in range(N):
        harmonics[n, t] = amplitude * sin(w_values[n] * t + phi)

# this part is showing plots for all generated harmonics, we don't really need them but still
# for i in harmonics:
#    plt.plot(i)
#    plt.show()

# last harmony
for i in harmonics.T:
    resulted = np.append(resulted, np.sum(i))

plt.figure(figsize=(20, 15))
plt.plot(resulted)
plt.grid(True)
plt.show()

mx = expectation(resulted, N)

dx = dispersion(resulted, mx, N)

print(f"Expected value: {mx}")
print(f"Deviation: {dx}")
