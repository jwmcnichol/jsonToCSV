import pandas

import pandas as pd
file='d:/page3.json'

with open(file, encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)
newFile = 'd:/csvfile3.csv'
df.to_csv(newfile, encoding='utf-8', index=False)