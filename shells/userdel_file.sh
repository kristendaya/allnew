#!/bin/bash

input= "user.dat"

while IFS=',' read -r username uid gid comment
do
	userdel -r "$username" 
	echo "Deleted $username"
done < $input

