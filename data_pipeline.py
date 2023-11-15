from pyspark.sql import SparkSession
from transformations import group_by_measure, join_datasets

def create_spark_session():
    return SparkSession.builder.appName("DataPipeline").getOrCreate()

def read_data(spark, input_path, format):
    return spark.read.format(format).load(input_path)

def write_data(df, output_path, format, compression):
    df.write.format(format).mode("overwrite").option("compression", compression).save(output_path)

def main():
    spark = create_spark_session()


    input_df = read_data(spark, "path/to/input/data", "parquet")


    grouped_df = group_by_measure(input_df, "measure_column")
    static_df = read_data(spark, "path/to/static/data", "json")
    joined_df = join_datasets(grouped_df, static_df, "join_column")

    write_data(joined_df, "path/to/output/data", "json", "gzip")

if __name__ == "__main__":
    main()
