#!/bin/bash
incr=0
prev=99999
for line in `cat input1`;
	do
        if [ $line -gt $prev ]
		then incr=$((incr+1))
	fi
        prev=$line
done
echo $incr
