# data-lake-solution

### Architecture

<img width="600em" src="docs/architecture.png">

### Infra
All the resources needed to create a Kubernetes cluster as well the Platform for the data environment.

For environment deployment:
1. [Kubernetes](https://github.com/matbragan/data-lake-solution/tree/main/infra/kubernetes)
3. [Platform](https://github.com/matbragan/data-lake-solution/tree/main/infra/platform)

### App
Development of an application that creates json or parquet files to place in the landing zone folder of a Data Lake, in this case using MinIO (s3).

1. [Data Gen DataStores](https://github.com/matbragan/data-lake-solution/tree/main/app/data-gen-datastores)

### Data
Creating a data pipeline using Trino, dbt-Core & Apache Airflow to create a complete end-to-end data environment.

To build the data environment:
1. [Trino](https://github.com/matbragan/data-lake-solution/tree/main/data/sql)
2. [dbt-Core](https://github.com/matbragan/data-lake-solution/tree/main/data/dags/dbt/lake)
3. [Airflow](https://github.com/matbragan/data-lake-solution/tree/main/infra/orchestration)
4. [DAG](https://github.com/matbragan/data-lake-solution/tree/main/data/dags/dbt_sql_transform.py)
