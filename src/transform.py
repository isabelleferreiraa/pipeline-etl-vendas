import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)

    rating_df = pd.json_normalize(df["rating"])
    df = df.drop(columns=["rating"]).join(rating_df)

    return df