from surprise import Reader, Dataset ,SVD
from surprise.model_selection import cross_validate
import pandas as pd

reader = Reader()

anime_ratings = pd.read_csv('./data/rating.csv')
# sample 25000 row

print(anime_ratings[["user_id", "anime_id", "rating"]])
data = Dataset.load_from_df(anime_ratings[["user_id", "anime_id", "rating"]], reader)
svd = SVD()
print(cross_validate(svd, data, measures=["RMSE", "MAE"], cv=10))
trainset = data.build_full_trainset()
svd.fit(trainset)
print(svd)
print(svd.predict(1, 32681))
