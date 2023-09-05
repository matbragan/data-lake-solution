## Necessary processes

### MYSQL

#### Creating a user
- Create the MYSQL user:
    ~~~sql
    create user 'newuser'@'%' identified by 'Newuser4%';
    ~~~
- Grant the required permissions to the user:
    ~~~sql
    grant select, reload, show databases, replication slave, replication client on *.* to 'newuser'@'%';
    ~~~
- Finalize the user's permissions:
    ~~~sql
    flush privileges;
    ~~~

#### Enabling the binlog
- Check whether the `log-bin` options is already on:
    ~~~sql
    select variable_value from performance_schema.global_variables where variable_name='log_bin';
    ~~~
- If it is `OFF`, configure your MySQL server configuration file with the following properties, which are described in the table below:
    ~~~properties
    server-id         = 223344 # Querying variable is called server_id, e.g. select variable_value from information_schema.global_variables where variable_name='server_id';
    log_bin           = mysql-bin
    binlog_format     = ROW
    binlog_row_image  = FULL
    expire_logs_days  = 10
    ~~~
- Confirm your changes by checking the binlog status once more:
    ~~~sql
    select variable_value from performance_schema.global_variables where variable_name='log_bin';
    ~~~

#### Validating binlog row value options
Necessary to `update` events
- Check current variable value
    ~~~sql
    show global variables where variable_name = 'binlog_row_value_options';
    ~~~
- Result:
    ~~~sql
    +--------------------------+-------+
    | Variable_name            | Value |
    +--------------------------+-------+
    | binlog_row_value_options |       |
    +--------------------------+-------+
    ~~~
- In case value is `PARTIAL_JSON`, unset this variable by:
    ~~~sql
    set @@global.binlog_row_value_options = "";
    ~~~

#### Enabling GTIDs (optional)
- Enable `gtid_mode`:
    ~~~sql
    set @@global.gtid_mode = ON;
    ~~~
- Enable `enforce_gtid_consistency`:
    ~~~sql
    set @@global.enforce_gtid_consistency = ON;
    ~~~
- Confirm the changes:
    ~~~sql
    show global variables like '%gtid%';
    ~~~

#### Enabling query log events (optional)
- Enable `binlog_rows_query_log_events`:
    ~~~sql
    set @@global.binlog_rows_query_log_events = ON;
    ~~~
- Confirm the changes:
    ~~~sql
    show global variables like 'binlog_rows_query_log_events';
    ~~~

### Deployment
- Create the containers, with Zookeeper, Kafka and Kafka Connect:
    ~~~sh
    python3 mysql_connector.py
    docker-compose up -d
    ~~~
