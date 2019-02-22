#Below are the following financial data for ABD company for a year
#months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
#expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]

#Import all 3 packages(numpy, pandas and matplotlib). Make that they have been installed before hand.
#Copy the above lists to your python editor/IDE of choice.
#From the above data, calculate the profit using numpy
#Write a python program to extract data from month and profit into a dictionary to be named ‘Fin_status’ 
#Write a Python program to convert the dictionary to a Pandas series
#Write a matplotlib program to create a line graph (using the panda series data) where x-axis is for months and y-axis is for profit. Also label your graph
#Explain what insights you can get from the graph



#WITH ONLINE EDITOR:

import numpy as np
import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]

r_list = np.array(revenue)
e_list = np.array(expenses)

profit = np.subtract(r_list, e_list)
print("Profit = %s" % (profit))

Fin_status = dict(zip(months,profit))
print("Fin_status = %s " % (Fin_status))

Fin_status_pandaseries = pd.Series(Fin_status, index = months, name = "ABD Company")
print(Fin_status_pandaseries)


#WITH JUPYTER NOTEBOOK:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
r_list = np.array(revenue)
e_list = np.array(expenses)
profit = np.subtract(r_list, e_list)
Fin_status = dict(zip(months,profit))
Fin_status_pandaseries = pd.Series(Fin_status, index = months, name = "ABD Company")
plt.xticks(np.arange(len(Fin_status_pandaseries.index)),Fin_status_pandaseries.index)
Fin_status_pandaseries.plot()
plt.xlabel('months')
plt.ylabel('profit')
plt.show()
