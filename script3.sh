#!/bin/bash
total=`wc -l <input3`
width=`wc -L <input3`
gamma=""
for i in `seq 1 $width`
	do gamma+="$(( `cut -c $i<input3 | grep 1 | wc -l` / (total/2) ))"
done
echo "gamma = $gamma ->" $(( 2#$gamma ))
epsilon=`echo $gamma | sed -e "s/1/2/g" -e "s/0/1/g" -e "s/2/0/g"`
echo "epsilon = $epsilon ->" $(( 2#$epsilon ))
echo result = $(( 2#$gamma * 2#$epsilon ))