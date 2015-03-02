#!/bin/bash

input='/data/numbers'
output='output'
mapper='mathstats_map.py'
reducer='mathstats_reduce.py'

hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input $input -output $output -file $mapper $reducer -mapper $mapper -reducer $reducer

