#!/bin/sh

#The idea to fiter out the lines which the price fields are less than 10000 by using awk 'PATTERN {ACTION}'
awk '$5 <= 10000 ' $1
