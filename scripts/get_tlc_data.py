from pyspark.sql import SparkSession, functions as F
import pandas as pd

# Create a spark session (which will run spark jobs)
spark = (
    SparkSession.builder.appName("MAST30034 Tutorial 2")
    .config("spark.sql.repl.eagerEval.enabled", True)
    .config("spark.sql.parquet.cacheMetadata", "true")
    .config("spark.sql.session.timeZone", "Etc/UTC")
    .config('spark.driver.memory', '4g')
    .config('spark.executor.memory', '2g')
    .getOrCreate()
)

sdf_jul = spark.read.parquet('../data/tlc_data/2023-07.parquet')
sdf_aug = spark.read.parquet('../data/tlc_data/2023-08.parquet')
sdf_sep = spark.read.parquet('../data/tlc_data/2023-09.parquet')
sdf_oct = spark.read.parquet('../data/tlc_data/2023-10.parquet')
sdf_nov = spark.read.parquet('../data/tlc_data/2023-11.parquet')
sdf_dec = spark.read.parquet('../data/tlc_data/2023-12.parquet')