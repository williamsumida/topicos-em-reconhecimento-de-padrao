import numpy as np
import pandas as pd

file_path = 'COVID19_Brasil.csv'
data = pd.read_csv(file_path)

print(data)
deaths = data["deaths"]
print(deaths)
