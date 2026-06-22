import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

# Create 2 subplots (1 row, 2 columns)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# First Subplot
ax[0].plot(x, y1,
           marker='o',          # Marker
           label='Dataset 1')   # Legend Label

ax[0].set_title("Plot 1")
ax[0].set_xlabel("X-Axis")      # X Label
ax[0].set_ylabel("Y-Axis")      # Y Label
ax[0].legend()                  # Legend

# Second Subplot
ax[1].plot(x, y2,
           marker='s',          # Marker
           label='Dataset 2')   # Legend Label

ax[1].set_title("Plot 2")
ax[1].set_xlabel("X-Axis")      # X Label
ax[1].set_ylabel("Y-Axis")      # Y Label
ax[1].legend()                  # Legend

# Adjust spacing
plt.tight_layout()

# Display plot
plt.show()