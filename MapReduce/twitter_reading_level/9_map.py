#!/usr/bin/env python

import sys
from reading_level import reading_level
from tweet_parser import tweet_parser

parser = tweet_parser()
reading_level = reading_level()

#Variables for reading level:
highest_rl = None	#Highest reading level found.
highest_usr = None	#Name of the user with the highest reading level.
lowest_rl = None	#Lowest reading level found.
lowest_usr = None	#Name of the user with the lowest reading level.
rl_sum = 0.0		#Sum of the reading level for all tweets.
rl_count = 0		#Count of the number of tweets.
rl_loc_sum = 0.0	#Sum of the reading level for tweets with location information.
rl_loc_count = 0	#Count of the number of tweets with location information.
rl_noLoc_sum = 0.0	#Sum of the reading level for tweets without location information.
rl_noLoc_count = 0	#Count of the number of tweets without location information.

for line in sys.stdin: #Get a tweet from stdin
	try:
		#Load the tweet into the parser:
		parser.load_tweet(line)

		#Parse the tweet:
		text = parser.get_text()
		user = parser.get_user()
		location = parser.get_location()	#Format is [longitude][latitude].
	except:
		continue

	#Calculate the reading level:
	#	Format: reading_level\t<user> <Is location present?> <reading_level>
	#Find the user with the highest reading level:
	rl = reading_level.get_level(text)
	if (highest_rl == None) or (rl > highest_rl):
		highest_rl = rl
		highest_usr = user

	#Find the user with the lowest reading level:
	if (lowest_rl == None) or (rl < lowest_rl):
		lowest_rl = rl
		lowest_usr = user

	#Calculate reading level sums and tweet counts:
	rl_sum += rl
	rl_count += 1
	if location == None:
		rl_noLoc_sum += rl
		rl_noLoc_count += 1
	else:
		rl_loc_sum += rl
		rl_loc_count += 1

#Output the keys:
#Output the reading level keys:
reading_level_usr_str = highest_usr + " " + str(highest_rl) + " " + lowest_usr + " " + str(lowest_rl)
reading_level_avg_str = str(rl_sum) + " " + str(rl_count) + " " + str(rl_loc_sum) + " " + str(rl_loc_count) + " " + str(rl_noLoc_sum) + " " + str(rl_noLoc_count)
print '%s\t%s' % ('reading_level_usr', reading_level_usr_str)
print '%s\t%s' % ('reading_level_avg', reading_level_avg_str)

