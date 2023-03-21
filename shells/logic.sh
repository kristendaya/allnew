#!/bin/bash

opt=$1
opt=$2

if [ $# -eq 2 ]; then
	if [ $opt == 'test' -a $opt == 'aaa' ]; then
		echo good
	elif [ $opt1 == 'aaa' -a $opt2 == 'test' ]; then
		echo good
	else
		echo bad
	fi
	else 
		echo "Input two parameters!"
fi	

