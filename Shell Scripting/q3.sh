#!/bin/bash

string=$(echo $1 | grep -o . | sort | tr -d "\n")
array=($(compgen -c))
count=0
for item in "${array[@]}"
do
	x=$(echo $item | grep -o . | sort | tr -d "\n")
	if [ $x = $string ]
	then
		if [[ $count -eq 0 ]]
		then 
			printf "%s\t" "YES"
		fi
		printf "%s\t" "$item"
		count=1
	fi

done

if [[ $count -eq 0 ]]
then
	echo "NO"
fi
echo 
