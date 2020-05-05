import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import pprint as pp
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
    return msa


def plot_scatter_data(data):
    plt.scatter(data['x'], data['y'])
    plt.show()


file_path = 'COVID19_Brasil.csv'
data = pd.read_csv(file_path)
print(data)

deaths = data["deaths"]
train, test = get_datasets(deaths)

pp.pprint(test)
