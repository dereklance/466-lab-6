# 466-lab-6
Ian Battin: ianbattin0@gmail.com
Derek Lance: dwalance@gmail.com

Required libraries: matplotlib, numpy

Method 1 - N Nearest Neighbors, Cosine similarity, Mean Utility
Method 2 - N Nearest Neighbors, Pearson correlation, Mean Utility
Method 3 - Mean Utility
Method 4 - N Nearest Neighbors Adjusted Weighted Sum, Cosine Similarity

EvaluateCFRandom.py
usage: python3 EvaluateCFRandom.py <method_num> <size> <repeats> [optional n]
runs n nearest neighbors. n defaults to 30 if no argument is provided.
size refers to the size of the random sample, and repeats are the number of
times the test case is repeated. prints results to stdout

EvaluateCFList.py
usage: python3 EvaluateCFList.py <method_num> <filename>
filename is the path to the file containing user specified test cases.
prints results to stdout
