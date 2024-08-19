import numpy as np
from math import pi
import matplotlib.pyplot as plt

def delta(x: float, epsilon: float) -> float:
    "Function converging to the Dirac delta-function. "
    return epsilon/(pi*(epsilon**2+x**2))

eps_values = [0.01, 0.1, 1]
x_values = np.linspace(-1,1,1001)


fig, ax = plt.subplots(3, 1, sharex = True)
fig.suptitle("Dirac delta visualisation")

for i in range(len(eps_values)):
    ax[i].plot(x_values, delta(x_values, eps_values[i]))
    ax[i].title.set_text(f"epsilon = {eps_values[i]}: ")
ax[2].set_xlabel("x")
plt.show()
