import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get("https://www.boursorama.com/cours/historique/1rPOVH")
print(response.text)
print()

print("Start parsing")
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table');

print(table)

values = []
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        date = columns[0].text.strip()
        dernier = float(columns[1].text.strip())
        var = columns[2].text.strip()
        haut = float(columns[3].text.strip())
        bas = float(columns[4].text.strip())
        ouverture = float(columns[5].text.strip())

        values.append([date, dernier, var, haut, bas, ouverture])
        
values.reverse()
df = pd.DataFrame(values,columns=['date','dernier','var','haut','bas','ouverture'])
df['mean2'] = df['ouverture'].rolling(2).mean()
print(df)

plt.plot(df['date'], df['dernier'], label='Ligne 1', color='blue', linestyle='solid')  # Ligne bleue pleine
plt.plot(df['date'], df['mean2'], label='Ligne 1', color='yellow', linestyle='solid')  # Ligne bleue pleine
plt.show()