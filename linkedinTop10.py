import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

con_data = pd.read_csv('Connections.csv')
orgs_raw = con_data['Company']

orgs = []
totals = []

for i in orgs_raw:
    if i in orgs:
        totals[orgs.index(i)] += 1
    else:
        orgs.append(str(i))
        totals.append(int(1))
        
zipOrgs = list(zip(orgs, totals))
zipOrgs.sort(key=lambda x: x[1], reverse = True)
zipOrgs = zipOrgs[:10]

print(len(orgs))
print(len(zipOrgs))

data = list(zip(*zipOrgs))

plt.bar(data[0], data[1])
plt.xticks(rotation=60)
plt.title("Connections per Organization (Top 10)")
plt.ylabel("No. of Connections")
plt.xlabel("Organizations")
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.show()