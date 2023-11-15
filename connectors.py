from pyspark.sql import SparkSession

class HadoopConnector:
    def __init__(self, spark):
        self.spark = spark

    def read_data(self, path, format):
        return self.spark.read.format(format).load(path)

    def write_data(self, df, path, format, compression):
        df.write.format(format).mode("overwrite").option("compression", compression).save(path)
