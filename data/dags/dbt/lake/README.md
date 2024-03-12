# dbt-Core

### Install
- [dbt](https://docs.getdbt.com/docs/core/installation-overview)

### Test
~~~sh
# connection
dbt debug

# models
dbt test
~~~

### Build
~~~sh
dbt build

# specific model
dbt run --model=<model_name>
~~~