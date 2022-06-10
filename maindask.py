import pandas as pd
import numpy as np
import dask.array as da
import dask.dataframe as dd

chunksize = 10**6

ddf = dd.read_csv('./data/UserAnimeList.csv')[['username', 'anime_id', 'my_score']]


ddf['anime_id'] = ddf['anime_id'].astype('category')
ddf['anime_id'] = ddf['anime_id'].cat.as_known()

df = ddf.pivot_table(columns='anime_id', values='my_score', index='username')
print(df.head())
# matrix = df.to_dask_array()

# print(matrix)
# u, s, vh = da.linalg.svd_compressed(matrix, k=10, compute=True)
# print(u)
# print(s)
# print(vh)