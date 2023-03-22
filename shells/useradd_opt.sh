#!/bin/bash
#
set -- $(getopt -q ug:c:de "$@")
#
echo
while [ -n "$1" ]
do
	case "$1" in
	-u) echo "(uid) option, parameter value : "$1" ;;
		shift;;	
	-g) param="$2"
	    echo "(gid) option,parameter value :"$2" ;;
	    shift;;
	-c) param="$2"
	    echo "(comment) option, parameter value: "#2" ;;
	    shift ;;
	-d) param="$2"
	    echo "(home direction) option, parameter value: "/home/$2" ;;
	-s) param="$2"
	    echo "(shell) option, parameter value : "/bin/bash" ;;
	    shift ;;
	--) shift
	    break ;;
	-k) (initial scripts directory) parameter value : "/home/$2" ;;
	-m) (make home directory) option
	    
	*) echo "parameter $1 : $1 " ;;
	esac
	shift
done
#
count=1
for param in "$@"
do
	echo "Parameter #$count: $param"
	count=$[ $count +1 ]
done
#

