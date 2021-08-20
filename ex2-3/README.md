* python Regex, string operation and built-in function performance comparison

* Exercise 2.3:
    Write a script that takes this file (from this Kaggle competition), extracts the request_text field from each dictionary in the list, and construct a bag of words representation of the string (string to count-list).

    There should be one row pr. text. The matrix should be N x M where N is the number of texts and M is the number of distinct words in all the texts.
i
    The result should be a list of lists ([[0,1,0],[1,0,0]] is a matrix with two rows and three columns).

* The exercise is done implementing some functions which generally have better performance than other method. For instance, manuplating strings with for loop instead of using Regex is way faster. There are more some experimental tricks for performance sensitive implementations.
