#!/bin/sh

### This shell script 
### 1. The exercise is to find wrong engish spells from stdin shakespeare.txt file regarding to a given dictionary stdin dict file. Recall the following command choosing the option -c for translating the each pattern matches the regexes and -s which replace multiple occurrences of '\n' to a single one. Please ignore the example, to bash the script require following syntax:
# bash ex1-3 shakespeare.txt dict

### Example. An if-else control flow -eq, means equal. -lt means less than
#if [ $# -lt 1  ] ; then
#	echo "Some text"
#	exit 1
#fi

### Example. Use following command to delete the puntuation for the stdout.
## tr -d [:CHARACTER CLASS:] < file
#tr -d [:punct:] < $1

### Example. Try capture 's  'are 'll 'd 't, which is a bit over think for doing this exercise which should distinguish the english grammar rule for tense. e.g. he's -> he is or he has.
#tr "[='=][=s=]" "is" < $1 > ex1-3.new
#tr [=char=] option can be combined in "" to perfom string

### Example. Try with sed command to manipulate the regular expression, sed can substitute option to replace the punctuation.sed command applies on the regex which have been read.
## sed 's/'`echo "'"`'/foo/g' `` for command when match the regex, '"'"' for matching regex of quote '
#sed 's/'"'"''/foo/g'

### Example. Solve the exercise with comm command comm file1 file2, for using stdin we have to do comm <(file1) <(file2)
## bash ex1-3 arg1 arg2
## comm file1 file2
# for argument of comm command, we need to bracket them () and use < such as inputing a file 
#(comm <(tr -d [:punct:] < $1 | tr -cs [:alpha:] '\n' | sort | uniq) <(sort $2)) > testComm.data

### Example. But, writing long command is not easy to test if somewhere is not correct. Therefore try make simple functions. The following functions has a lot commentted script which is not a intuitive way for testing. So what I can do for next script is to make smaller functions which with the commands and saparate them. The functions should also be syntatically correct and bash-able even though I don't use it for resolving the current problem. In this way the functions can be documented maybe not useful for the task, but yet can be a good example for solving other task. And the function call of those need to be commented out.
checkSpell() {
	#tr -d [:punct:] < $1
	#variable=, the equal sign needs followed with no space
	#FILE1=$1
	#Refering the place holder $FILE1 need to be type cast to string 
	#tr -d [:punct:] < "$FILE1"
	#unset FILE1
	#FILE1=$1
	#F1_PUNCT=$(tr -d [:punct:] < "$FILE1")
	#tr -cs [:alpha:] '\n' <<< "$F1_PUNCT"
	#tr -d [:punct:] < "$FILE1" | tr -cs [:alpha:] '\n' 
	#F1_LINE_WORD = $(tr -cs [:alpha:] '\n' < $F1_U_PUNCT)
	#F1_SORTED = $(sort $F1_LINE_WORD | uniq)
	#F2_SORTED = $(sort $2)
	#comm $F1_SORTED $F2_SORTED
	
	### <() use stdout produced by a valid command as an input file without generating an actual file
	#unset FILE1
	#unset FILE2
	#FILE1=$1
	#FILE2=$2
	#comm <(tr -d [:punct:] < "$FILE1" | tr -cs [:alpha:] '\n' | sort | uniq) <(sort "$2")
	#comm -23 <( tr -d [:punct:] < "$FILE1" | tr -cs [:alpha:] '\n' | tr [:upper:] [:lower:] | sort | uniq ) <( tr [:upper:] [:lower:] < "$FILE2" | sort | uniq )
	
	###storing stdout to a variable identifier.
	#tr: when not truncating set1, string2 must be non-empty
	tr -cs [:alpha:] '\n' < $1 | tr -d [:punct:] | tr [:upper:] [:lower:] | sed '/^$/d' | sort -u > FILE1
	tr [:upper:] [:lower:] < $2 | sort -u > FILE2
	comm -23 FILE1 FILE2 > FILE3
	wc FILE3

	###bash another shell script
	#tr -cs [:alpha:] '\n' < $1 | tr -d [:punct:] | tr [:upper:] [:lower:] | sed '/^&/d' | sort -u > FILE1
	#tr [:upper:] [:lower:] < $2 | sort -u > FILE2
	#bash ./commExample.sh FILE1 FILE2
}
checkSpell $1 $2

#Example: A function to print out stdout by passing stdin arguments to the function
fresh(){
	# t stores $1 argument passed to fresh()
	t=$1
	echo "fresh(): \$0 is $0"
	echo "fresh(): \$1 is $1"
	echo "fresh(): \$t is $t"
	echo "fresh(): total args passed to me $#"
	echo "fresh(): all args (\$@) passed to me -\"$@\""
	echo "fresh(): all args (\$*) passed to me -\"$*\""
}
#echo "**** calling fresh() 1st time ****"
#fresh Tomat
# invoke the function with total 3 arguments
#echo "**** calling fresh() 2nd time ****"
#fresh Tomato Onion Paneer
