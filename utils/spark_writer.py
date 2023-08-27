from pyspark.sql import DataFrame


def spark_writer(
    dataframe: DataFrame,
    layer: str,
    table: str,
    repartition: int = 1,
    mode: str = 'overwrite',
    partitionBy: list = None
) -> None:
    writer = (
        dataframe
        .repartition(repartition)
        .write.mode(mode)
    )

    if partitionBy:
        writer = writer.partitionBy(partitionBy)
    
    writer.save(f's3a://lake-solution/{layer}/{table}/')
