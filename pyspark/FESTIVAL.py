from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("yarn").appName("Festival").getOrCreate()

# 데이터 가져와서 기본 가공
df = spark.read.option("multiline", "true").json("festival.json")
df_temp = df.select(explode(col('culture')).alias('temp'))


# 가공 - EVENT_PLACE table
place = df_temp.withColumn('place', explode(col('temp.place'))).select('place').distinct().withColumn('id', monotonically_increasing_id())
# place_id 부여
window = Window.orderBy(col('id'))
event_place = place.withColumn('place_id', row_number().over(window)).select('place_id', col('place').alias('place_nm'))


# 가공 - EVENT_INFO table
festival = df_temp.withColumn('tmp', explode(arrays_zip(col('temp.place'), col('temp.coord')))).withColumn('row_id', monotonically_increasing_id()).select(col('row_id'), col('temp.title').alias('event_nm'), col('tmp.place'), col('tmp.coord'), col('temp.period'), col('temp.time').alias('event_tm'), col('temp.target').alias('target_kb'), col('temp.fee').alias('fare_amt')).withColumn('from_dt', to_date(substring(split('period', '~').getItem(0), 1, 10), 'yyyy-MM-dd')).withColumn('to_dt', to_date(substring(split('period', '~').getItem(1), 2, 10), 'yyyy-MM-dd')).drop('period').withColumn('x_coord', col('coord').getItem(0)).withColumn('y_coord', col('coord').getItem(1)).drop('coord')
event_info = festival.join(event_place, festival.place == event_place.place_nm, 'inner').select(festival.row_id, festival.event_nm, event_place.place_id, festival.from_dt, festival.to_dt, festival.event_tm, festival.target_kb, festival.fare_amt)



# MySQL에 저장
event_place.write.mode("overwrite").format("jdbc")\
     .option("driver", "com.mysql.cj.jdbc.Driver")\
     .option("url", "jdbc:mysql://localhost:3306/mysql")\
     .option("dbtable", "pjt2.EVENT_PLACE")\
     .option("user", "root")\
     .option("password", "1234")\
     .save()


event_info.write.mode("overwrite").format("jdbc")\
     .option("driver", "com.mysql.cj.jdbc.Driver")\
     .option("url", "jdbc:mysql://localhost:3306/mysql")\
     .option("dbtable", "pjt2.EVENT_INFO")\
     .option("user", "root")\
     .option("password", "1234")\
     .save()