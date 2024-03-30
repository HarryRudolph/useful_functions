import polars as pl

def get_duplicates(df):
    return df.filter(pl.struct(["A", "B"]).is_duplicated())

