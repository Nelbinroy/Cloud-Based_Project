from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

def main():
    spark = SparkSession.builder.appName("Reviews Analysis").getOrCreate()
    # Load data, assuming you have a CSV file
    df = spark.read.csv("/path/to/your/dataset.csv", header=True, inferSchema=True)
    # Calculate average helpful votes per rating
    result = df.groupBy("reviews.rating").agg(avg("reviews.numHelpful").alias("avg_helpful"))
    result.show()
    # Optionally, save or visualize the results here
    spark.stop()

if __name__ == "__main__":
    main()
