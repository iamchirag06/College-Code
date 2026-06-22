import matplotlib.pyplot as plt 
x = [1, 2, 3, 4] 
y1 = [10, 20, 25, 30] 
y2 = [5, 15, 20, 25] 
fig, ax = plt.subplots(1, 2) 
# First subplot 
ax[0].plot(x, y1) 
ax[0].set_title("Plot 1") 
# Second subplot 
ax[1].plot(x, y2) 
ax[1].set_title("Plot 2") 
plt.show()