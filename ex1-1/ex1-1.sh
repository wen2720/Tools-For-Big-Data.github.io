#!/bin/sh

#Idea:
#The idea is to translate each alphabetic characters which forms the words with -c option and compress identical newline character with second argument with -s option.   


(tr -cs "[:alpha:]" '\n' | sort | uniq -c | sort -hr | head -n 10) < $1
#The first sort command sorts the words alphabetically for counting words occurrencies of the same words and the second sort command sorts the occurrencies numerically with revesed order. Finally the head command list top 10 lines of words with occurencies by side. The line of commands are piped whci requies a file argument when bashing it.
