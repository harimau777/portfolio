#!/usr/bin/env python

import sys

#Variables for reading level:
highest_rl = None		#Highest reading level found.
highest_usr = None		#Name of the user with the highest reading level.
lowest_rl = None		#Lowest reading level found.
lowest_usr = None		#Name of the user with the lowest reading level.
rl_sum = 0.0			#Sum of the reading level for all tweets.
rl_cnt = 0			#Count of the number of tweets.
rl_loc_sum = 0.0		#Sum of the reading level for tweets with location information.
rl_loc_cnt = 0			#Count of the number of tweets with location information.
rl_noLoc_sum = 0.0		#Sum of the reading level for tweets without location information.
rl_noLoc_cnt = 0		#Count of the number of tweets without location information.

for line in sys.stdin:  #Get the key values from stdin.
	#Split into key and value:
	(key, val) = line.strip().split('\t', 1)	#Split at the first tab.

	#Reduce user reading level:
	if key == 'reading_level_usr':
		(high_usr, high_rl, low_usr, low_rl) = val.strip().split()
		#Find the user with the highest reading level:
		if (highest_rl == None) or (float(high_rl) > highest_rl):
			highest_rl = float(high_rl)
			highest_usr = high_usr

		#Find the user with the lowest reading level:
		if (lowest_rl == None) or (float(low_rl) < lowest_rl):
			lowest_rl = float(low_rl)
			lowest_usr = low_usr

	#Reduce average reading level:
	if key == 'reading_level_avg':
		(cur_rl_sum, cur_rl_cnt, cur_rl_loc_sum, cur_rl_loc_cnt, cur_rl_noLoc_sum, cur_rl_noLoc_cnt) = val.strip().split()
		rl_sum += float(cur_rl_sum)
		rl_cnt += int(cur_rl_cnt)
		rl_loc_sum += float(cur_rl_loc_sum)
		rl_loc_cnt += int(cur_rl_loc_cnt)
		rl_noLoc_sum += float(cur_rl_noLoc_sum)
		rl_noLoc_cnt += int(cur_rl_noLoc_cnt)

#Print the results:
#Output for reading level:
print "Highest reading level was from " + highest_usr + " with " + str(highest_rl)
print "Lowest reading level was from " + lowest_usr + " with " + str(lowest_rl)
try:
	print "Average reading level: " + str(rl_sum / rl_cnt)
	print "Average reading level with location data: " + str(rl_loc_sum / rl_loc_cnt)
	print "Average reading level without location data: " + str(rl_noLoc_sum / rl_noLoc_cnt)
except ZeroDivisionError:
	print "Error: Divide by zero"
