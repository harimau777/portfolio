#! /usr/bin/python

import sys
import rpyc
import thread
import os
import os.path #Is this needed since I'm importing os?

#********** Client **********
class myClient():
	#********** User registration methods **********
	conn = None
	username = None					#The client's username.
	bgsrv = None
	def set_username(self, name):
		self.username = name

	def connect(self, ip, port):
        	self.conn = rpyc.connect(ip, port)		#Connect to the chat server
		self.bgsrv = rpyc.BgServingThread(self.conn)	#Creates a bg thread to process incoming events.
		self.conn.root.register_user(self.username, self.exposed_send_file_list, self.exposed_send_file)	#Register the user with the server

	def disconnect(self):
                self.conn.root.unregister_user(self.username)	#Unregister the user with the server
		self.bgsrv.stop()

	#********** Remote file methods **********
	def get_file_list(self):
		file_list = self.conn.root.list_files()
		for user in file_list:
			print "***** " + user + " *****"
			for filename in file_list[user]:
				print filename

	def get_file(self, username, old_filename, new_filename):
		file_packet = self.conn.root.get_file(username, old_filename)
		if file_packet[0] == True:
			f = open(new_filename, "wb")
			f.write(file_packet[1])
			f.close
			print username + "'s file " + old_filename + " saved as " + new_filename
		else:
			print file_packet[1]	#Print the error message.

#		f = open(new_filename, "wb")
#		f.write(self.conn.root.get_file(username, old_filename))
#		f.close()
#		print username + "'s file " + old_filename + "saved as " + new_filename

	#********** Local file methods: **********
	shared_path = None	#Path to shared files NOTE: IS THIS HOW WE DEFINE A LOCAL VARIABLE?
	def set_path(self, path):
		self.shared_path = path

	def exposed_send_file(self, filename):
		if filename.find("..") != -1:	#Return an error if the someone tries to leave the shared folder.
			return (False, "Error: For security reasons filenames cannot contain \"..\".")
		try:
			filepath = self.shared_path + "/" + filename	#NOTE: IS THIS CORRECT AND NECESSARY?
			f = open(filepath, "rb")		#Open the file
			return (True, f.read())			#Read the file and return it to the server.
			f.close()
		except:
			return (False, "Error: Failed to read the file.")	#Return an error message.

	def exposed_send_file_list(self):
		try:
			#Get the list of files:
			file_list = os.listdir(self.shared_path)				#Get all files at the given path.
			file_list = [item for item in file_list if  not os.path.isfile(item)]	#Remove "files" that are not really files (e.g. directories).
			return (True, file_list)						#Return the list of files to the server.
		except:
			return (False, "Error: Failed to retrieve file list.")

#********** Main **********
#Usage: ./client.py <username> <path> <ip address> <port>
if __name__ == "__main__":
	c = myClient()
	c.set_username(sys.argv[1])
	c.set_path(sys.argv[2])
	c.connect(sys.argv[3], sys.argv[4])
	print "Enter \"help\" for a list of commands."
	while True:	#Program loop.
		user_input = raw_input("Please enter a command: ").split()
		if user_input[0] == "list_files":
			c.get_file_list()
		elif user_input[0] == "get_file":
			c.get_file(user_input[1], user_input[2], user_input[3])
		elif user_input[0] == "disconnect":
			c.disconnect()
			break
		elif user_input[0] == "help":
			print "\n\r********************"
			print "list_files : List the files shared by each user"
			print "get_file <username> <filepath> <filename> : Get the file at <filepath> from <username> and save it as <filename>"
			print "disconnect : Disconnect from the server"
			print "help : Display this help information"
			print "********************\n\r"
		else:
			print "Unrecognized command"

