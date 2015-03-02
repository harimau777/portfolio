#!/bin/bash

input='/data/books'
output='/user/moneysdr/output'
mapper='search_map.py'
reducer='search_reduce.py'

hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input $input -output $output -file $mapper $reducer -mapper $mapper -reducer $reducer


#hadoop fs -cat /user/moneysdr/output/part-00000 | ./search_compare.py
hadoop fs -get /user/moneysdr/output/part-00000 .
python search_compare.py

