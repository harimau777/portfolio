#! /usr/bin/python

import sys
import rpyc
import thread
import os
import os.path #NOTE: Is this needed since I'm importing os?
from rpyc.utils.server import ThreadedServer

#********** Server **********
class myServer(rpyc.Service):
	userDict = {}	#Dictionary of the users connected to the server.
	def on_connect(self):
		pass

	def exposed_register_user(self, username, file_list_callback, file_transfer_callback):
		try:
			self.userDict[username] = [file_list_callback, file_transfer_callback]	#Add the user to the user dictionary.
		except:
			pass

	def exposed_unregister_user(self, username):
		try:
			del self.userDict[username]				#Delete the user from the user dictionary.
		except:
			pass

	def exposed_list_files(self):
		try:
			fileDict = {}						#Dictionary.  Enties are: Username : List of shared files
			for username in self.userDict:				#Loop through each user.
				packet = self.userDict[username][0]()		#Call the user's file_list callback.
				fileDict[username] = packet[1]			#Store the list of files in the dictionary.
			return fileDict						#Return the list of shared files to the calling user.
		except:
			pass

	def exposed_get_file(self, username, filename):
		try:
			user_file = self.userDict[username][1](filename)	#Call the user's file_transfer_callback.
			return user_file					#Return the file to the calling user.
		except:
			pass

#********** Main **********
#Usage: ./server.py <ip address> <port>
if __name__ == "__main__":
	t = ThreadedServer(myServer, port = int(sys.argv[2]))
	print "Server started, listening to port " + sys.argv[2] + "."
	t.start()

