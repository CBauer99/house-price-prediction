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
combine = []

# PARSE DATA AS PAIRS RATHER THAN TRYING TO PARSE EACH "PART" BASED ON CHAR LEN
for i in range(0, len(data_lines) - 1, 2): 
     p1 = data_lines[i].strip().split()
     p2 = data_lines[i + 1].strip().split()
     combine.append(p1 + p2)

## Place data in DataFrame
df = pd.DataFrame(combine, columns=columns)

## Export to csv
df.to_csv(path, index=False)
print(f"Data saved to {path}")