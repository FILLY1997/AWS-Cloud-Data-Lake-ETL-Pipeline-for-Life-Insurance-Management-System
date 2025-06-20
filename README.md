# 🏥 Life Insurance Data Engineering Pipeline on AWS

This project demonstrates a modern AWS-based data pipeline for processing and analyzing **life insurance policy data**. It leverages an **Oracle Database** as the source system and integrates **AWS Lambda**, **AWS Glue**, **S3**, and **Athena** to build an automated, serverless, and scalable architecture for analytics.

---

## 🚀 Architecture Overview

**Flow:**

1. Oracle DB stores raw policy data.
2. AWS Lambda triggers AWS Glue job.
3. AWS Glue extracts and transforms data using Spark.
4. Transformed data is written to Amazon S3 in Parquet format.
5. Data is queried using Athena or visualized in QuickSight.

---

## 🧱 Tech Stack

| Component         | Description                               |
|------------------|-------------------------------------------|
| Oracle DB         | Source system with policy records         |
| AWS Lambda        | Triggers Glue job                         |
| AWS Glue          | ETL engine to extract/transform data      |
| Amazon S3         | Data lake for raw and transformed data    |
| Apache Parquet    | Columnar format used for storage          |
| Amazon Athena     | Query engine for analyzing data           |
| Amazon QuickSight | (Optional) Dashboard & visual analytics   |

---

## 📁 Folder Structure

```bash
├── glue_jobs/
│   └── transform_life_insurance_data.py
├── lambda/
│   └── trigger_glue_job.py
├── sql/
│   └── oracle_extract_query.sql
├── README.md
