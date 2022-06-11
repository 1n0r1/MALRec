import pandas as pd
import numpy as np
import dask.array as da

chunksize = 10**6

fileReader = pd.read_csv('./data/UserAnimeList.csv', chunksize=chunksize)

df = pd.DataFrame(dtype = 'int8')

count = 0

for chunk in fileReader:
    count +=1
    if count > 100:
        break
    newdf = chunk.pivot(index='username', columns='anime_id', values='my_score').fillna(0).astype('int8')
    df = pd.concat((df,newdf)).groupby(['username']).first().fillna(0).astype('int8')
    print(df)
    df.to_csv('./value_matrix_' + str(count) + '.csv')
    # df.loc[row.iloc[0], row.iloc[1]] = row.iloc[5]=
print(df)


matrix = df.values

u, s, vh = np.linalg.svd(matrix, full_matrices=False)


 
# Find the highest similarity
# def cosine_similarity(v,u):
#     return (v @ u)/ (np.linalg.norm(v) * np.linalg.norm(u))
 
# highest_similarity = -np.inf
# highest_sim_col = -1
# for col in range(1,vh.shape[1]):
#     similarity = cosine_similarity(vh[:,0], vh[:,col])
#     if similarity > highest_similarity:
#         highest_similarity = similarity
#         highest_sim_col = col
 
# print("Column %d (book id %s) is most similar to column 0 (book id %s)" %
#         (highest_sim_col, df.columns[col], df.columns[0])
# )
