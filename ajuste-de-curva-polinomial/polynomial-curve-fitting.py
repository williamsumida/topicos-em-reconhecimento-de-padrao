import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import pprint as pp
from operator import itemgetter
import math


def get_datasets(data):
    train = {'x': [], 'y': []}
    test  = {'x': [], 'y': []}

    for i in range(len(data)):
        if i%2 == 0:
            train['x'].append(i)
            train['y'].append(data[i])
        else:
            test['x'].append(i)
            test['y'].append(data[i])
    train['y'].reverse()
    test['y'].reverse()
    return train, test


def get_result_dataset(curve, test):
    result = {'x': [], 'y': []}
    for x in test['x']:
        result['x'].append(x)
        result['y'].append(curve(x))
    return result


def mean_squared_error(test, result):
    mse=0
    for i in range(len(test['y'])):
        mse += abs(test['y'][i] - result['y'][i])**2
    mse = mse/len(test['y'])
    mse = math.sqrt(mse)  
    return mse 

def plot_scatter_data(data):
    plt.scatter(data['x'], data['y'])
    plt.show()

def plot_correlation(dataset, curve):
    plt.scatter(data['x'], data['y'])
    plt.scatter(dataset['x'], data['y'])
    plt.show()


file_path = 'COVID19_Brasil.csv'
data = pd.read_csv(file_path)
print(data)

deaths = data["deaths"]

train, test = get_datasets(deaths)
oi=[]
mse_list = []
for i in range(90):
    polynomial_coefficients = np.polyfit(train['x'], train['y'], i)
    curve = np.poly1d(polynomial_coefficients)
    result = get_result_dataset(curve, test)
    if i ==19:
        pp.pprint(polynomial_coefficients)
        coef = polynomial_coefficients
    mse = mean_squared_error(train, result)
    mse_list.append((i, mse, result))
    oi.append((i, mse))
mse_list.sort(key=itemgetter(1))
x =[]
y=[]

for p in mse_list:
    print(f"{p[0]} & {p[1]}\\\\")

for mse in oi:
    if mse[0] <= 20:
        x.append(mse[0])
        y.append(mse[1])
        #print(mse)
#pp.pprint(mse_list[0])
#plot_scatter_data(mse_list[0][2])
#plt.plot(x,y, marker = 'o', linestyle = ':')
#plt.show()

data=[d for d in deaths]
data.reverse()
plt.scatter([i for i in range(96)], data, marker='o')
plt.plot(mse_list[0][2]['x'], mse_list[0][2]['y'], color='orange')
plt.show()
#plot_scatter_data(train)
#plot_scatter_data(test)
for c in coef:
    print('& ',c, '\\\\')
