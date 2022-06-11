import dask.array as da
import dask.dataframe as dd

x = dd.read_csv('./value_matrix.csv')
print(x.head())
u, s, v = da.linalg.svd_compressed(x, k=10)
v.compute()