import  matplotlib.pyplot as plt

#  Give X & Y Axis values for each graph

#line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
plt.plot(x, y)
plt.title('Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

#bar graph
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]
plt.barh(categories, values)
plt.title('Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

#pie chart
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [10, 20, 15, 25, 30]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

#scatter plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()