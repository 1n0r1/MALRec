import pandas as pd
import numpy as np
import heapq
import sys

anime_ratings = pd.read_csv('./data/rating.csv')
anime_ratings.drop(anime_ratings[anime_ratings['rating'] == -1].index, inplace=True)
reviewmatrix = anime_ratings.pivot_table(index="user_id", columns="anime_id", values="rating").fillna(0)
matrix = reviewmatrix.values
u = np.load('./python/u.npy')
s = np.load('./python/s.npy')
vh = np.load('./python/vh.npy')

# Find the highest similarity
def cosine_similarity(v,u):
    return (v @ u)/ (np.linalg.norm(v) * np.linalg.norm(u))

def getRec(anime_id, numAnimes):
    arr = []
    index_no = reviewmatrix.columns.get_loc(anime_id)
    for col in range(0,vh.shape[1]):
        if col == index_no:
            continue
        similarity = cosine_similarity(vh[:,index_no], vh[:,col])
        heapq.heappush(arr,[similarity, reviewmatrix.columns[col]])
        if len(arr) > numAnimes:
            heapq.heappop(arr)
    return arr
print(getRec(int(sys.argv[1]), int(sys.argv[2])))
