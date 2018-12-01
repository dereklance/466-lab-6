import evaluation, sys, csv_parser, bisect, n_nearest_neighbors
import matplotlib.pyplot as plt

def output_graph_to_png(n_vs_accuracy):
    [xs, ys] = zip(*n_vs_accuracy)
    plt.scatter(xs, ys)
    plt.savefig('nnn_tuning.png')

def main(method_num, size, repeats):
    # matrix = csv_parser.parse('dataset.csv_parser')
    # accuracies = [(n, evaluation.random_sampling(matrix, method_num, size, repeats, n)) for n in range(5, 46, 5)]
    # print(accuracies)

    accuracies = [
        (5, 0.744), (10, 0.755), (15, 0.78), (20, 0.741),
        (25, 0.774), (30, 0.782), (35, 0.763), (40, 0.768), (45, 0.772),
        (50, 0.775), (100, 0.762), (150, 0.745), (200, 0.763),
        (250, 0.763), (300, 0.75), (350, 0.774), (400, 0.769),
        (450, 0.764), (500, 0.758)
    ]
    output_graph_to_png(accuracies)

if __name__ == '__main__':
    main(*map(int, sys.argv[1:]))