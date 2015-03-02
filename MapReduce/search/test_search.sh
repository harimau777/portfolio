#!/bin/bash

input='/data/books'
output='output'
mapper='search_map.py'
reducer='search_reduce.py'

hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input $input -output $output -file $mapper $reducer -mapper $mapper -reducer $reducer

#python search_compare.py

