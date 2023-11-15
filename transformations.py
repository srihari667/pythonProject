from pyspark.sql import functions as F

def group_by_measure(df, measure_col):
    return df.groupBy(measure_col).agg(F.sum("value").alias("sum_value"))

def join_datasets(df1, df2, join_col):
    return df1.join(df2, on=join_col)
