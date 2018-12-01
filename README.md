# 466-lab-6

Required libraries: matplotlib, numpy

Method 1 - N Nearest Neighbors, Cosine similarity, Average Ranking
Method 2 - N Nearest Neighbors, Pearson correlation, Average Ranking
Method 3 -
Method 4 -

EvaluateCFRandom.py
usage: python3 EvaluateCFRandom.py <method_num> <size> <repeats> [optional n]
runs n nearest neighbors. n defaults to 30 if no argument is provided.
size refers to the size of the random sample, and repeats are the number of
times the test case is repeated. prints results to stdout

EvaluateCFList.py
usage: python3 EvaluateCFList.py <method_num> <filename>
filename is the path to the file containing user specified test cases.
prints results to stdout
