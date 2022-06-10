import pandas as pd
chunksize = 10**6

fileReader = pd.read_csv('./data/UserAnimeList.csv', chunksize=chunksize)

df = pd.DataFrame(dtype = 'int8')

count = 0

for chunk in fileReader:
    count +=1
    if count > 10:
        break
    newdf = chunk.pivot(index='username', columns='anime_id', values='my_score').fillna(0).astype('int8')
    df = pd.concat((df,newdf)).groupby(['username']).first().fillna(0).astype('int8')
    # df.loc[row.iloc[0], row.iloc[1]] = row.iloc[5]=
print(df)