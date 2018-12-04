#!/bin/bash

hadoop_dir=$HADOOP_HOME
if ! [ -d input ]
then
echo "Make input directory with files"
fi
if ! [ -d output ]
then
mkdir output
else
rm -r output
fi
if ! [ -d $hadoop_dir ]
then
echo "Set valid env variable HADOOP_HOME"
fi
   $hadoop_dir/bin/hdfs namenode -format
   #starting hadoop in pseudo-distributed mode
   $hadoop_dir/sbin/start-dfs.sh
   $hadoop_dir/bin/hdfs dfs -mkdir /user
   $hadoop_dir/bin/hdfs dfs -mkdir /user/smby
   $hadoop_dir/bin/hdfs dfs -put input /user/smby/input
   $hadoop_dir/bin/hdfs dfs -ls /user/smby/input
   #$hadoop_dir/bin/hdfs dfs -rm -r /user/smby/output
   $hadoop_dir/bin/yarn jar $hadoop_dir/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files mapper.py,reducer.py -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec -D mapred.output.compression.type=BLOCK -input '/user/smby/input' -output '/user/smby/output' -mapper mapper.py -reducer reducer.py -numReduceTasks 1 -outputformat org.apache.hadoop.mapred.SequenceFileOutputFormat
   $hadoop_dir/bin/hdfs dfs -get /user/smby/output 
   $hadoop_dir/bin/hdfs dfs -ls /user/smby/output
   $hadoop_dir/sbin/stop-dfs.sh

