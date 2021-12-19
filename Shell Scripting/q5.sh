#!/bin/bash
mkdir temp_activity
cd temp_activity
touch temp{1..50}.txt
for f in temp{1..25}.txt;
do
	mv -- "$f" "${f%.txt}.md"
done

for x in *;
do
	mv "$x" "${x%.*}_modified.${x##*.}"
done

zip txt_compressed.zip *txt

