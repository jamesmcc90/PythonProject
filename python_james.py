# Data Visualisation using Python#

# Pandas is used for working with tabular data

# Matplotlib is used for data visualization

import pandas as pd
import matplotlib.pyplot as plt
import pylab

df = pd.read_csv('BalanceDetails_20210806.csv',  encoding = "ISO-8859-1")
print(df)

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(5, 8))

fig = pylab.gcf()
fig.canvas.manager.set_window_title('Matplotlib with Python')

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()