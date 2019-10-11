## Random hive-related tips:

- Kill hadoop job:
```
yarn application -kill application_1554118004619_317963
```

- When massive queries bounce try:

```
set mapred.tasktracker.expiry.interval=3600000;
set mapred.task.timeout= 3600000;
SET mapreduce.map.memory.mb=8192;
SET mapreduce.map.java.opts=-Xmx7373m;
SET mapreduce.reduce.memory.mb=8192;
SET mapreduce.reduce.java.opts=-Xmx7373m;
SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.optimize.sort.dynamic.partition=true;
SET hive.vectorized.execution.enabled=true;
SET hive.auto.convert.join.noconditionaltask.size=10000000;
SET hive.exec.parallel=true;
SET hive.exec.parallel.thread.number=8;
SET hive.stats.fetch.partition.stats=true;
SET hive.stats.fetch.column.stats=true;
SET hive.stats.fetch.partition.stats=true;
SET hive.compute.query.using.stats=true;
```
