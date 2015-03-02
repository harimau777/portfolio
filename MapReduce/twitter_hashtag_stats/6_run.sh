#!/bin/bash

input='/data/twitter'
output='/user/moneysdr/output'
mapper='6_map.py'
reducer='6_reduce.py'
other='tweet_parser.py reading_level.py syl_dict.p'

hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input $input -output $output -file $mapper $reducer $other -mapper $mapper -reducer $reducer

