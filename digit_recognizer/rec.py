import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


train = pd.read_csv('train.csv')
print train.head()

print(train.shape)

# save the labels to a Pandas series target
target = train['label']
# Drop the label feature
train = train.drop("label",axis=1)