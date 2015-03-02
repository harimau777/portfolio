#! /bin/bash

#Usage: ./test_script <role>

if [ $1 == "server" ]; then
	./server.py localhost 18888
elif [ $1 == "client1" ]; then
	./client.py user1 data localhost 18888
elif [ $1 == "client2" ]; then
	./client.py user2 data2 localhost 18888
fi

