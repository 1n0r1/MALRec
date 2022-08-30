import pandas as pd
import numpy as np

anime_ratings = pd.read_csv('../data/rating.csv')

# Print a few sample of what we collected
anime_ratings = pd.DataFrame(anime_ratings, columns=["user_id", "anime_id", "rating"])
anime_ratings.drop(anime_ratings[anime_ratings['rating'] == -1].index, inplace=True)
print(anime_ratings.head())

 
# Look for the users who reviewed more than 50 animes
usercount = anime_ratings[["anime_id","user_id"]].groupby("user_id").count()
usercount = usercount[usercount["anime_id"] >= 50]
 
# Look for the animes who reviewed by more than 50 users
workcount = anime_ratings[["anime_id","user_id"]].groupby("anime_id").count()
workcount = workcount[workcount["user_id"] >= 50]
 
# Keep only the popular animes and active users
anime_ratings = anime_ratings[anime_ratings["user_id"].isin(usercount.index) & anime_ratings["anime_id"].isin(workcount.index)]
print("\nSubset of data:")
print(anime_ratings)
 
# Convert records into user-anime review score matrix
reviewmatrix = anime_ratings.pivot_table(index="user_id", columns="anime_id", values="rating").fillna(0)
matrix = reviewmatrix.values

reviewmatrix.to_csv('reviewmatrix.csv', index=True)
 
# Singular value decomposition
u, s, vh = np.linalg.svd(matrix, full_matrices=False)
np.save('u.npy', u)    # .npy extension is added if not given
np.save('s.npy', s)    # .npy extension is added if not given
np.save('vh.npy', vh)    # .npy extension is added if not given
