import matplotlib.pyplot as plt

# Marks of students
marks = [45, 50, 55, 60, 65, 70, 72, 75, 80, 82,
         85, 88, 90, 92, 95, 78, 68, 58, 48, 73]

plt.figure(figsize=(6,4))

plt.hist(marks, bins=5, edgecolor='black')

plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()