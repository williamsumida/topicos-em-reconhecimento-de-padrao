import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import pprint as pp
import math
from operator import itemgetter

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
    msa = 0
    for i in range(len(test['y'])):
        msa += abs(test['y'][i] - result['y'][i])**2
    msa = msa/len(test['y'])
    msa = math.sqrt(msa) 
    return msa 

def plot_scatter_data(data):
    plt.scatter(data['x'], data['y'])
    plt.show()


file_path = 'COVID19_Brasil.csv'
data = pd.read_csv(file_path)
print(data)

deaths = data["deaths"]
train, test = get_datasets(deaths)

mse_list = []

for i in range(90):
    polynomial_coefficients = np.polyfit(train['x'], train['y'], i)
    curve = np.poly1d(polynomial_coefficients)
    result = get_result_dataset(curve, test)
    mse = mean_squared_error(test, result)
    print(f'M={i} MSE = {mse}')
    mse_list.append((i, mse, result))
    #plot_scatter_data(result)
mse_list.sort(key=itemgetter(1))
for mse in mse_list:
    print(mse[0], mse[1])
#print(mse_list)
#pp.pprint(mse_list[0])
plot_scatter_data(mse_list[0][2])

