import matplotlib.pyplot as plt
#SampleData
x =[1, 2, 3, 4, 5]
y1 =[10, 20, 30, 40, 50]
y2 =[5, 15, 25, 35, 45]
#Plot TwoLines
plt.plot(x,y1,marker='o',linestyle='-',color='b',label="Line 1")

plt.plot(x, y2, marker='s', linestyle='--',
color='r', label="Line 2") # Adding Elements
plt.title("Graph with Legend at Lowerright")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#AddLegendinlowerright
plt.legend(loc="lower right") #Youcanchangethistootherpositions
#ShowGraph
plt.show()