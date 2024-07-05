## IMPORTS ##
import os
import requests
import pandas as pd

## Pull Data from site
url = "https://lib.stat.cmu.edu/datasets/boston"
pull = requests.get(url)
data = pull.text

## DATA PREPERATION ##
path = os.path.join('data/boston_housing.csv') ## FILE DL LOCATION

## COLUMNS from Dataset Description
columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
## Split data into lines
lines = data.split('\n')

## Extract the relevant lines with data
data_start = 22 ## LN 22 is where data starts
data_lines = lines[data_start:]

## Dataset in splint in two parts, we have to combine them
p1 = []
p2 = []

for i in range(len(data_lines)):
    if i < 77: ## Second line will never hit this len
        p1.append(data_lines[i].strip().split())
    else:
        p2.append(data_lines[i].strip().split())

## Combine the parts
combine = []
for i in range(len(p1)):
        combine.append(p1[i] + p2[i])

## Place data in DataFrame
df = pd.DataFrame(combine, columns=columns)

## Export to csv
df.to_csv('boston_housing.csv', index=False)