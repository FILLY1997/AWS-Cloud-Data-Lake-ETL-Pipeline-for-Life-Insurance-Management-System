python
import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, to_date, upper, year, when

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Oracle using Glue Connection (Assuming connection already created)
oracle_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:oracle:thin:@//oracle-host:1521/ORCL") \
    .option("dbtable", "LIFE_POLICY") \
    .option("user", "your_user") \
    .option("password", "your_password") \
    .option("driver", "oracle.jdbc.driver.OracleDriver") \
    .load()

# Transformations
transformed_df = oracle_df \
    .withColumn("policy_start_date", to_date(col("policy_start_date"), "yyyy-MM-dd")) \
    .withColumn("premium_amount", col("premium_amount").cast("double")) \
    .withColumn("policy_type", upper(col("policy_type"))) \
    .withColumn("policy_start_year", year(col("policy_start_date"))) \
    .withColumn("status_flag", when(col("status") == "ACTIVE", 1).otherwise(0))

# Write as Parquet to S3
target_path = "s3://life-insurance-data/transformed/life_policy/"
transformed_df.write.mode("overwrite").parquet(target_path)

job.commit()