from pyspark.sql.types import *
from pyspark.sql import SQLContext
from pyspark import SparkContext

sqlContext = SQLContext(sc)

#Define the targeted section that is shared across all form types
customSchema = StructType([ \
    StructField("Amt", StringType(), True), \
    StructField("GrantOrContributionPurposeTxt", StringType(), True), \
    StructField("RecipientBusinessName", StringType(), True), \
    StructField("RecipientFoundationStatusTxt", StringType(), True), \
    StructField("RecipientPersonNm", StringType(), True), \
    StructField("RecipientRelationshipTxt", StringType(), True), \
    StructField("RecipientUSAddress", StructType([StructField("AddressLine1Txt", StringType(), True),StructField("CityNm", StringType(), True),StructField("StateAbbreviationCd", StringType(), True),StructField("ZIPCd", StringType(), True)]), True)])

#Create Spark DataFrame with each row being the contents of a single tax form
read_df = spark.read.format('xml').options(rowTag='GrantOrContributionPdDurYrGrp').load('S3_BUCKET_ADDRESS', schema=customSchema)
explode_df = read_df.select("RecipientUSAddress.","")
write_df = explode_df.drop("RecipientUSAddress")

#Write DataFrame to MySQL database
write_df.write.format('jdbc').options(
    url='MYSQL_DATABASE',
    driver='com.mysql.jdbc.Driver',
    dbtable='TABLE_NAME',
    user='USERNAME',
    password='PASSWORD').mode('append').save()
