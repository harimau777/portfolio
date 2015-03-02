#!/usr/bin/env python

import sys
import operator

#Variables for hashtag frequency:
day_hashtag_dict = {}		#Nested dictionary, day_hashtag_dict[day][hashtag] = count of times the hashtag occured
hour_hashtag_dict = {}		#Nested dictionary, hour_hashtag_dict[hour][hashtag] = count of the times the hashtag occured

for line in sys.stdin:  #Get the key values from stdin.
	try:
		#Split into key and value:
		(key, val) = line.strip().split('\t', 1)	#Split at the first tab.

		#Reduce hashtag frequency per day:
		if key == 'hashtag_count_day':
			(day, hashtag, hashtag_count) = val.strip().split()
			#Calculate the hashtag frequency per day:
			if day not in day_hashtag_dict:
				day_hashtag_dict[day] = {}
			if hashtag not in day_hashtag_dict[day]:
				day_hashtag_dict[day][hashtag] = int(hashtag_count)
			else:
				day_hashtag_dict[day][hashtag] += int(hashtag_count)

		#Reduce hashtag frequency per hour:
		if key == 'hashtag_count_hour':
			(hour, hashtag, hashtag_count) = val.strip().split()
			#Calculate the hashtag frequency per day:
			if hour not in hour_hashtag_dict:
				hour_hashtag_dict[hour] = {}
			if hashtag not in hour_hashtag_dict[hour]:
				hour_hashtag_dict[hour][hashtag] = int(hashtag_count)
			else:
				hour_hashtag_dict[hour][hashtag] += int(hashtag_count)
	except:
		pass

#Print the results:
#Output the hashtag frequency:
for day in day_hashtag_dict:
	#http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
	max_hash = max(day_hashtag_dict[day].iteritems(), key=operator.itemgetter(1))[0]
	print "The most frequent hashtag for " + day + " was #" + max_hash + "."
for hour in hour_hashtag_dict:
	max_hash = max(hour_hashtag_dict[hour].iteritems(), key=operator.itemgetter(1))[0]
	print "The most frequent hashtag for " + hour + ":00 was #" + max_hash + "."

