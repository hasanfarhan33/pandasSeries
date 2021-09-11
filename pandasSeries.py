import numpy as np
import pandas as pd

labels = ["a", "b", "c"]
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

print(pd.Series(data = my_data))
print("")
print(pd.Series(data = my_data, index=labels))
print("")
print(pd.Series(my_data, labels))
print("")
print(pd.Series(arr, labels))
print("")
print(pd.Series(d))

print("")
ser1 = pd.Series([1,2,3,4],['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)

print("")
ser2 = pd.Series([1, 43, 5, 2], ['USA', "Germany", "Italy", "England"])
print(ser2)

print("")
print(ser1['USA'])
print(ser2["Germany"])

print("")
print(ser1 + ser2)

print("")
