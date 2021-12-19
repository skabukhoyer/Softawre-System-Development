#!/bin/bash

 
#num=( 1 4 5 9 10 40 50 90 100 400 500 900 1000 )
#sym=( I IV V IX X XL L XC C CD D CM M )

function toINT(){
s=$1
i=${#s}
ans=0
num=0
i=`expr $i - 1`
while [ $i -ge 0 ]
do
        case ${s:i:1} in
                I)
                        num=1
                        ;;
                V)
                        num=5
                        ;;
                X)
                        num=10
                        ;;
                L)
                        num=50
                        ;;
                C)
                        num=100
                        ;;
                D)
                        num=500
                        ;;
                M)
                        num=1000
                        ;;
        esac
        x=`expr $num \* 4`
        if [[ $x -lt $ans ]];
        then
                ans=`expr $ans - $num`
        else
                ans=`expr $ans + $num`
        fi
        (( i-- ))
done

echo $ans
}


toRoman(){
	local num=( 1 4 5 9 10 40 50 90 100 400 500 900 1000 )
	local sym=( I IV V IX X XL L XC C CD D CM M )

	number=$1
        i=12
        while [ $number -gt 0 ]
        do
                div=`expr $number / ${num[i]}`
                number=`expr $number % ${num[i]}`
                while [ $div -gt 0 ]
                do
                        printf "%s" "${sym[i]}"
                        (( div-- ))
                done
                (( i-- ))
        done

}

if [[ $# -eq 1 ]];
then
	toRoman $1
else 
#	number1=$1
#	number2=$2
	if [[ $1 =~ ^[+-]?[0-9]+$ ]];
	then
		number3=`expr $1 + $2`
		toRoman $number3

	else
		x=$(toINT $1)
		y=$(toINT $2)
		echo `expr $x + $y`
	fi
fi



