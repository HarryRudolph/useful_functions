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

# Remove all whitespace from all columns
df.select(pl.col(pl.Utf8).str.strip_chars())

# DataFrame containing only the rows where at least one column is null.
df_missing = (
    df
    .filter(
        pl.any_horizontal(pl.all().is_null())
    )
)

# pl.all() is just syntactic sugar for pl.col("*").

# Change number of rows printed
with pl.Config(tbl_rows=2):
    print(df)
