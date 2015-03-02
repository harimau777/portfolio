#!/usr/bin/env python

import sys
from tweet_parser import tweet_parser
import operator

parser = tweet_parser()

#Variables for hashtag frequency:
day_hashtag_dict = {}		#Nested dictionary, day_hashtag_dict[day][hashtag] = count of times the hashtag occured
hour_hashtag_dict = {}		#Nested dictionary, hour_hashtag_dict[hour][hashtag] = count of the times the hashtag occured

for line in sys.stdin: #Get a tweet from stdin
	try:
		try:
			#Load the tweet into the parser:
			parser.load_tweet(line)

			#Parse the tweet:
			hashtag_list = parser.get_hashtags()
			hour = parser.get_time().split(':')[0]
			day = parser.get_day()
		except:
			continue

		#Calculate the hashtag frequency:
		if len(hashtag_list) > 0:	#If there are no hashtags, then we do not need to calculate anything.
			#Calculate the hashtag frequency per day:
			if day not in day_hashtag_dict:
				day_hashtag_dict[day] = {}
			for hashtag in hashtag_list:
				if hashtag['text'] not in day_hashtag_dict[day]:
					day_hashtag_dict[day][hashtag['text']] = 1
				else:
					day_hashtag_dict[day][hashtag['text']] += 1

			#Calculate the hashtag frequency per hour:
			if hour not in hour_hashtag_dict:
				hour_hashtag_dict[hour] = {}
			for hashtag in hashtag_list:
				if hashtag['text'] not in hour_hashtag_dict[hour]:
					hour_hashtag_dict[hour][hashtag['text']] = 1
				else:
					hour_hashtag_dict[hour][hashtag['text']] += 1
	except:
		pass

#Output the keys:
#Output the hashtag frequency keys:
try:
	if day_hashtag_dict:	#If dictionary is not empty.
		for day in day_hashtag_dict:
			#http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
			max_hash = max(day_hashtag_dict[day].iteritems(), key=operator.itemgetter(1))[0]
			hashtag_count_str = day + " " + max_hash + " " + str(day_hashtag_dict[day][max_hash])
			print '%s\t%s' % ('hashtag_count_day', hashtag_count_str)
except:
	pass

try:
	if hour_hashtag_dict:	#If dictionary is not empty.
		for hour in hour_hashtag_dict:
			max_hash = max(hour_hashtag_dict[hour].iteritems(), key=operator.itemgetter(1))[0]
			hashtag_count_str = hour + " " + max_hash + " " + str(hour_hashtag_dict[hour][max_hash])
			print '%s\t%s' % ('hashtag_count_hour', hashtag_count_str)
except:
	pass

