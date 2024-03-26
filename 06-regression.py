import pandas as pd
from sklearn.linear_model import LogisticRegression


data = pd.DataFrame({
    'age':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
    'majeur':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
})

logreg = LogisticRegression()

learnData = data.loc[:,['age']]
target = data.loc[:,'majeur']
print(learnData)

logreg.fit(learnData,target)

result = logreg.predict([[1],[5],[2],[84],[12],[1]])
print(result)