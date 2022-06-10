import pandas as pd
import numpy as np
import dask.array as da
import dask.dataframe as dd

ddf = dd.read_csv('./data/UserAnimeList.csv')



ddf['anime_id'] = ddf['anime_id'].astype('category')
ddf['anime_id'] = ddf['anime_id'].cat.as_known()

df = ddf.pivot_table(columns='anime_id', values='my_score', index='username')

matrix = df.to_dask_array()
print(matrix)
matrix.compute().to_csv('./out.*.csv')
u, s, v = da.linalg.svd_compressed(matrix, k=10)
v.compute()