import sys, csv, n_nearest_neighbors
from random import randint
from statistics import mean, stdev

methods = {
    1: n_nearest_neighbors
}

n = 200

def random_sample(matrix, size):
    num_users = len(matrix)
    num_items = 100
    test_pairs = []
    for i in range(size):
        rating = randint(0, num_users - 1), randint(0, num_items - 1)
        while matrix[rating[0]][rating[1]] == 99.0:
            rating = randint(0, num_users - 1), randint(0, num_items - 1)
        test_pairs.append(rating)
    return test_pairs

def random_sampling(matrix, method_num, size, repeats):
    mean_absolute_errors = []
    for i in range(repeats):
        sample = random_sample(matrix, size)
        absolute_errors = []
        for user_id, item_id in sample:
            predicted_rating = methods.get(method_num).predict_rating(matrix, user_id, item_id, n)
            actual_rating = matrix[user_id][item_id]
            abs_err = abs(predicted_rating - actual_rating)
            absolute_errors.append(abs_err)
            print(user_id, item_id, actual_rating, predicted_rating, abs_err, sep = ',')
        mae = mean(absolute_errors)
        print('MAE:', mae)
        print('-----------------------------------')
        mean_absolute_errors.append(mae)
    print('Mean MAE:', mean(mean_absolute_errors))
    print('Standard Deviation MAE:', 0 if len(mean_absolute_errors) == 1 else stdev(mean_absolute_errors))


def main():
    matrix = csv.parse(sys.argv[1])
    random_sampling(matrix, *map(int, sys.argv[2:]))

if __name__ == '__main__':
    main()