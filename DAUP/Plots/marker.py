import matplotlib.pyplot as plt
#SampleData
x =[1, 2, 3, 4, 5]
y=[10, 20, 30, 25, 40]
#Plot LineGraphwithCustomMarkers
plt.plot(x, y,
marker='o', #CircleMarker('s'forSquare, 'd'forDia
markersize=10, #MarkerSize
markerfacecolor='red',#FillColorof
markeredgecolor='black',#BorderColorofMarker 
linestyle='-',
color='r',
label="Line withMarkers")
#AddingElements
plt.title("Line Plot withCustomMarkers") #Title
plt.xlabel("X-Axis") # X-axis Label
plt.ylabel("Y-Axis") #Y-axisLabel
plt.legend() # Legend
#ShowtheGraph
plt.show()