import evaluation, sys, csv
import matplotlib.pyplot as plt

def main(method_num, size, repeats):
    matrix = csv.parse('dataset.csv')
    accuracies = [(n, evaluation.random_sampling(matrix, method_num, size, repeats, n)) for n in range(10, 51, 10)]
    print(accuracies)

if __name__ == '__main__':
    main(*map(int, sys.argv[1:]))