#!/bin/bash

echo "File name :$0 "
echo "Parameter Counter : $# "
echo "All parameter : $@ "

if [ $1 = ok ]; then
	echo "good~!"
else
	echo "bad~!"
fi
