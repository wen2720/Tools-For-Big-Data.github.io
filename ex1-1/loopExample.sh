#!/bin/sh
#rm wordFreq.output
#touch wordFreq.output
while read line; do
	for word in $line; do
		#if ! grep $word wordFreq.output;
		#then
		#	echo $word 1 >> wordFreq.output
		#else
		#	awk '{ if($1 = $word) 
		#		print $1, $2 + 1 > "wordFreqnew.output" }' wordFreqnew.output
		#fi
		echo $word
	done
done < ex1-1.data
