#!/bin/bash
position=0
depth=0
aim=0
while read line
	value=`echo $line | cut -d " " -f 2`
	do case `echo $line | cut -d " " -f 1` in
		up)
			aim=$(( aim - value ))
			;;
		down)
			aim=$(( aim + value ))
			;;
		forward)
			position=$(( position + value ))
			depth=$((depth + aim * value ))
			;;
		*)
			break
			;;
	esac
done <input2
echo "$position * $depth" | bc
