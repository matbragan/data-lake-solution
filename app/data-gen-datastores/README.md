# Data Gen DataStores

### Write data to [interface]
Use `object_storage.sh` to automatic write some data.
~~~sh
python cli.py --help

python cli.py all parquet
python cli.py mssql json
python cli.py postgres json
python cli.py mongodb json
python cli.py redis json
~~~