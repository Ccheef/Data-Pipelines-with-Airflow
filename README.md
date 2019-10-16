# Data-Pipelines-with-Airflow
<h2>Introduction</h2>
A music streaming company, Sparkify, has decided to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow. <strong>This project applies Airflow to schedule and monitor ETL pipelines that extract data from S3, stage data in Redshift, and transform data into a fact table and a set of dimensional tables for the use of the analytics team. </strong> The high grade data pipelines are dynamic and built from reusable tasks, can be monitored, allow easy backfills, and enable data quality check.

-----------------------------------------------------------------------------------------------------

<h2>Datasets and Star Schema Designed Tables</h2>
Source datasets on S3: The log data is located at s3://udacity-dend/log_data and the song data is located on s3://udacity-dend/song_data<br>
Output tables on Redshift: There are two staging tables that stage data directly from log_data and song_data. Then, five star schema designed tables (1 fact table and 4 dimention tables) are derived from the staging tables. Please refer to the directory 'Data-Warehouse-AWS' to see the tables details. 

-----------------------------------------------------------------------------------------------------

<h2>Airflow Tasks</h2>
