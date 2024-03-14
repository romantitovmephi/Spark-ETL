from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as F
import pyspark.sql.types as t


def extract_data(spark: SparkSession) -> DataFrame:
    path = "data/cars.csv"
    return spark.read.option("header", "true").csv(path)


def transform_data(df: DataFrame) -> DataFrame:
    output = (
        df
        .groupBy("manufacturer_name")
        .agg(
            F.count("manufacturer_name").alias("count"),
            F.round(F.avg("year_produced")).cast(t.IntegerType()).alias("avg_year_produced"),
            F.min(F.col("price_usd").cast(t.FloatType())).alias("min_price"),
            F.max(F.col("price_usd").cast(t.FloatType())).alias("max_price")  
        )
        .orderBy(F.col("count").desc())
    )
    return output


def save_data(df: DataFrame) -> None:
    df.coalesce(1).write.mode("overwrite").format("csv").save("output.csv")


def main():
    spark = SparkSession.builder.appName("ETL").getOrCreate()
    df = extract_data(spark)
    output = transform_data(df)
    save_data(output)
    #spark.stop()

main()