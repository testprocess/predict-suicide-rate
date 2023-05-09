import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import csv

suicide = pd.read_csv(os.path.join('./input', 'sc.csv'))
gdp = pd.read_csv(os.path.join('./input', 'gdp.csv'))

suicide.info()
suicideData = pd.DataFrame(suicide)
gdpData = pd.DataFrame(gdp)
initYear = 1983

result = []

with open('cb.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["year", "suicide", "gdp"]
    
    writer.writerow(field)
    for i in range(39):
        nowYear = initYear + i
        multiply = 10
        suicideInsert = int(float(suicideData[str(nowYear)][0]) * multiply)
        gdpInsert = int(float(gdpData[str(nowYear)][1]) * multiply)
        data = [nowYear, suicideInsert, gdpInsert]
        result.append(data)
        writer.writerow(data)

print(result)