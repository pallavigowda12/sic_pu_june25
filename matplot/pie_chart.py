import matplotlib.pyplot as plt

# Data
labels = ['AI', 'ML', 'Data Science', 'Others']
sizes = [30, 40, 20, 10]
colors = ['gold', 'lightgreen', 'skyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)  # Highlight 'ML' slice

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Tech Interest Distribution')
plt.axis('equal')  # Ensures pie is a circle
plt.show()
