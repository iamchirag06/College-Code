import matplotlib.pyplot as plt
import numpy as np

# x-values from 0 to 10
x = np.linspace(0, 10, 100)

# Sine and Cosine values
y1 = np.sin(x)
y2 = np.cos(x)

# First subplot - Sine Wave
plt.subplot(1, 2, 1)
plt.plot(x, y1, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()

# Second subplot - Cosine Wave
plt.subplot(1, 2, 2)
plt.plot(x, y2, label='cos(x)')
plt.title('Cosine Wave')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.legend()

# Adjust layout to prevent overlap
plt.tight_layout()

plt.show()