#matplot 1-5

#line plot
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2,3,4,5,6,7,8,9,10])
y = x*2
fig = plt.figure(figsize = (5, 2.5))
plt.plot(x, y)
plt.show() 

#bar plot
import numpy as np
import matplotlib.pyplot as plt 
data = {'C':20, 'C++':15, 'Java':30, 'Python':35}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (5, 2.5)
plt.bar(courses, values, color ='blue', width = 0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

#scatter plot
import seaborn as sb 
df = sb.load_dataset('iris') 
sb.regplot(x = "sepal_length",y = "petal_length", ci = None,data = df) 

#bar chart
from matplotlib import pyplot as plt
import numpy as np
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)
plt.show()

#histogram
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color='white', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.show()

