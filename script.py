
a.to_csv('aDataset.csv')

df2 = a.groupby('diseaseNID').apply(lambda x: x['associationType'].unique())
df2

a2 = a.groupby(by = ['diseaseNID'])['associationType'].apply(lambda x: set(x))
a2.head(15)

a2 = a2.to_frame().reset_index()
a2

from itertools import combinations
a2['combinations'] = a2['associationType'].apply(lambda r: list(combinations(r,2)))
a2.head()

a3 = a2[a2['combinations'].map(lambda d: len(d)) > 0]
a3

result = pd.DataFrame([(c, tup.diseaseNID) for tup in a3.itertuples() for c in tup.combinations])
result

result = result.rename(columns={0: 'Combos', 1: 'diseaseNID'})
result

result[['associationType1','associationType2']] = pd.DataFrame(result.Combos.tolist(), index= result.index)
result

result.to_csv('ResultingDataset.csv')

result['geneNID1'] = ""
result

result['geneNID2'] = ""
result

for row in result.iterrows():
     #Can access data using column names with iterrows
     for row2 in a.iterrows():
        if [(row['diseaseNID'] == row2['diseaseNID']) and (row['associationType1'] == row2['associationType'])]:
            row['geneNID1'] = row2['geneNID']
        elif [(row['diseaseNID'] == row2['diseaseNID']) and row['associationType2'] == row2['associationType']]:
            row['geneNID2'] = row2['geneNID']
        break
     break
result


arowList = []
arow2List = []


for index, row in result.iterrows():
#    if [a.loc[(a['diseaseNID'] == row['diseaseNID']) & (a['associationType'] == row['associationType1'])]:
#        row['geneNID1'] = 
    arow = a.loc[(a['diseaseNID'] == row['diseaseNID']) & (a['associationType'] == row['associationType1'])]
    arowList.append(arow['geneNID'])
    #row['geneNID1'] = arow['geneNID']
    #print(row['geneNID1'])
    
    arow2 = a.loc[(a['diseaseNID'] == row['diseaseNID']) & (a['associationType'] == row['associationType2'])]
    #row['geneNID2'] = arow2['geneNID']
    arow2List.append(arow2['geneNID'])
    #print(row['geneNID2'])
    
    #break
result

numpp = result['geneNID1'].to_numpy() 
numpp


from itertools import combinations

a2['combinations'] = a2['associationType'].apply(lambda r: list(combinations(r,2)))
a2.head()
