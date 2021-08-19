#!/bin/sh
## To compare two files by using comm command, the stdout would be three columns of data.
#e.g	comm FILE1 FILE2
## First column shows the data that only appears in the FILE1. Second column of data shows the data that only appears in the FILE2. And the third column of data shows the data appears in both of FILE1 and FILE 2/
## To supress column,for showing data which only appears in FILE1, we can use following instance.
comm -23 $1 $2
