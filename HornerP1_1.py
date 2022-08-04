import matplotlib.pyplot as plt
import numpy as np

# x axis values
x = np.linspace(1.92,2.08, num=8000)

y = (x-2)**9

plt.plot(x, y)
plt.title('P1(x)')
plt.show()