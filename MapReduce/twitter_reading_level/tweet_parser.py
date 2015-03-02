import json
import sys

#nbviewer.ipython.org/github/raynach/hse-twitter/blob/master/docs/Collecting Twitter data from the API with Python.ipynb

class tweet_parser:
	def load_tweet(self, newTweet):
		self.tweet = json.loads(newTweet)

	def get_text(self):
		return self.tweet['text']

	def get_user(self):
		return self.tweet['user']['screen_name']

	
	def get_hashtags(self):
		return self.tweet['entities']['hashtags']

	def get_location(self):
		if self.tweet['coordinates'] == None:
			return None
		else:
			return self.tweet['coordinates']['coordinates']

	def get_time(self):
		return self.tweet['created_at'].split()[3]

	def get_day(self):
		return self.tweet['created_at'].split()[0]
#added for date, month and year
	def get_date(self):
		return self.tweet['created_at'].split()[2]
	
	def get_month(self):
		return self.tweet['created_at'].split()[1]
	
	def get_year(self):
		return self.tweet['created_at'].split()[5]
	
	def get_fulldate(self):
		return self.tweet['created_at']
	
	def get_JulainDay(self):
	    julianday = 0
	    month = self.tweet['created_at'].split()[1]
	    date = int(self.tweet['created_at'].split()[2])
	    
	    if (month.lower() == 'jan'):
	         julianday = date + 1
	    elif(month.lower() == 'feb'):
	        julianday = date + 31
	    elif(month.lower() == 'mar'):
	        julianday = date + 60
	    elif(month.lower() == 'apr'):
	        julianday = date + 91
	    elif(month.lower() == 'may'):
	        julianday = date + 121
	    elif(month.lower() == 'jun'):
	        julianday = date + 152
	    elif(month.lower() == 'jul'):
	        julianday = date + 182
	    elif(month.lower() == 'aug'):
	        julianday = date + 213
	    elif(month.lower() == 'sep'):
	        julianday = date + 244
	    elif(month.lower() == 'oct'):
	        julianday = date + 274
	    elif(month.lower() == 'nov'):
	        julianday = date + 305
	    elif(month.lower() == 'dec'):
	        julianday = date + 335
	    else:
	        julianday = date + 0
	        
	    return julianday
   
def main(argv):
	f = open("twittermini.txt")
	json_str = f.readline()
	f.close()
        parser = tweet_parser()
	parser.load_tweet(json_str)
	print parser.get_user()
	print parser.get_text()
	print parser.get_time()
	print parser.get_day()
	print parser.get_location()
	print parser.get_hashtag()
	#added date year and time 
	print parser.get_date()
	print parser.get_month()
	print parser.get_year()
	print parser.get_fulldate()
	#print parser.get_JulainDay(month,date)

if __name__ == '__main__':
        main(sys.argv)

