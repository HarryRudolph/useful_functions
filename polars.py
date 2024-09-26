import polars as pl

def get_duplicates(df):
    return df.filter(pl.struct(["A", "B"]).is_duplicated())


# Keep only groups with more than one row
df = df.filter(
              (pl.len() > 1).over("group")
)

# Add unique id to rows
df = df.with_row_index()

# Compare datetime col with datetime object
ldf = ldf.filter(
              pl.col("dtg") > pl.lit(datetime.datetime.now()).cast(pl.Datetime("us", "UTC"))
)
