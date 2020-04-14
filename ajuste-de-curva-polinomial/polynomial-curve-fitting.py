import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

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

file_path = 'COVID19_Brasil.csv'
data = pd.read_csv(file_path)
print(data)

deaths = data["deaths"]
train, test = get_datasets(deaths)

plt.scatter(train['x'], train['y'])
plt.show()

plt.scatter(test['x'], test['y'])
plt.show()


#curve = np.polyfit(x, deaths, 90)
#print('curve: ', curve)

#poly = np.poly1d(curve)
#final_y = []
#for i in range(96):
#    final_y.append(poly(i))




