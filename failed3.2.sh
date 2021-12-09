#!/bin/bash
tf="/tmp/aoc_tmp"

log() {
    echo $1 >&2
}

# args: $1=column (starting at 1)
most_frequent_bit() {
    tee > "/tmp/aoc_tmp2"
    length=`cat /tmp/aoc_tmp2 | wc -l`
    # log /tmp/aoc_tmp2
    log $length
    # how many ones in column ?
    count=`cat /tmp/aoc_tmp2 | cut -c $1 | grep 1 | wc -l`
    log $count
    bit=`echo "$count / ( $length / 2 )" | bc`
    log $bit
    echo $bit 
}

less_frequent_bit() {
    res=`most_frequent_bit $1`
    echo $(( 1 - res )) 
}

# args: $1=column (starting at 0)
recurse() {
    step=$1
    bit=`cat $tf | less_frequent_bit $(( step+1 ))`
    log "^.{$step}$bit.*"
    cat $tf | grep -E "^.{$step}$bit.*" > `echo $tf`
    results=`cat $tf | wc -l` 
    log "$step: $results lines with bit$bit"
    if [[ $results -gt 1 ]]
        then log "next ! $(( step+1 ))"
        log ""
        recurse $(( step+1 ))
    else
        cat $tf
    fi
}

cat input3 > `echo $tf`
recurse 0 


# for i in $(seq 1 `echo -n $gamma | wc -m`)
# 	do matching=$(cat input3 | grep `echo $gamma | cut -c 1-$i`)
# 	if [[ `echo $matching | wc -w` -eq 1 ]]
# 		then echo $matching
# 		break
# 	fi
# done
# epsi2=""
# for i in `seq 1 $width`
#         do epsi2+="$(( 1 - `cut -c $i<input3 | grep 1 | wc -l` / (total/2) ))"
# done
# echo "epsi2=$epsi2"
# for i in $(seq 1 `echo -n $epsi2 | wc -m`)
# 	do matching=$(cat input3 | grep `echo $epsi2 | cut -c 1-$i`)
# 	echo $epsi2 | cut -c 1-$i
# 	echo $matching | wc -w
# 	if [[ `echo $matching | wc -w` -eq 1 ]]
# 		then echo $matching
# 		break
# 	fi
# done
