import pandas as pd
import os
pd.options.mode.chained_assignment = None  # default="warn"

if os.getcwd().endswith("solutions"):
    users = pd.read_csv("../../data/05/user_features.csv", sep=";")
    movies = pd.read_csv("../../data/05/movie_features.csv", sep=";")
else:
    users = pd.read_csv("../data/05/user_features.csv", sep=";")
    movies = pd.read_csv("../data/05/movie_features.csv", sep=";")

ignored_columns = ["year_bucket", "movieId", "userId", "title"]
ignored_columns_wide = ["movieId", "userId", "title", "year"]


def get_user_data(user_id, type=None):
    user = users[users.userId == user_id]

    user["_tmpkey"] = 1
    movies["_tmpkey"] = 1
    input = pd.merge(movies, user, on="_tmpkey").drop("_tmpkey", axis=1)

    if type == "wide_n_deep":
        return get_input_data(input, "wide"), get_input_data(input)
    return get_input_data(input)


def get_input_data(input, type=None):
    if type == "wide":
        return input.drop(ignored_columns_wide, axis=1)
    return input.drop([col for col in input.columns if col.startswith(tuple(ignored_columns))], axis=1)
