#!/bin/sh
### to translate stdin regarding to the pattern
##e.g tr OPTION STRING1 STRING2 FILE
tr -cs "[:alpha:]" "\n" < $1 
