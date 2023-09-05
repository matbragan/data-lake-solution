from delta.tables import DeltaTable
from pyspark.sql import DataFrame


class SparkWriter():

    def __init__(self, **kwargs):
        self.spark = kwargs.get('spark', None)
        self.bucket = 'lake-solution'
        self.path = f's3a://{self.bucket}/'
        
        if 'path' in kwargs:
            self.path += kwargs['path']
        elif 'table' in kwargs:
            self.path += kwargs['table']
        else:
            raise ValueError('Necessary path or table keyword in SparkWriter class')

    def s3_writer(
        self,
        dataframe: DataFrame,
        mode: str = 'overwrite',
        format: str = 'delta',
        repartition: int = 1,
        partitionBy: list = None
    ) -> None:
        
        writer = (
            dataframe
            .repartition(repartition)
            .write.mode(mode)
        )

        if mode == 'overwrite' and format == 'delta':
            writer = writer.option('overwriteSchema', True)

        if partitionBy:
            writer = writer.partitionBy(partitionBy)
        
        writer.format(format).save(self.path)

    def vacuum_and_optimize(self, retention_hours: int = 72) -> None:
        
        deltaTable = DeltaTable.forPath(self.spark, self.path)
        deltaTable.vacuum(retention_hours)
        deltaTable.optimize().executeCompaction()
