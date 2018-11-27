import sys, csv, n_nearest_neighbors
from random import randint
from statistics import mean, stdev

methods = {
    1: lambda matrix, user_id, item_id, n:
        n_nearest_neighbors.predict_rating(
            matrix, user_id, item_id, n, similarity = n_nearest_neighbors.cosine_similarity
        ),
    2: lambda matrix, user_id, item_id, n:
    n_nearest_neighbors.predict_rating(
        matrix, user_id, item_id, n, similarity = n_nearest_neighbors.pearson_correlation
    )
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

def user_specified(matrix, method_num, test_pairs):
    absolute_errors = []
    for user_id, item_id in test_pairs:
        if matrix[user_id][item_id] == 99.0:
            continue
        predicted_rating = methods.get(method_num)(matrix, user_id, item_id, n)
        actual_rating = matrix[user_id][item_id]
        abs_err = abs(predicted_rating - actual_rating)
        absolute_errors.append(abs_err)
        output = [user_id, item_id, actual_rating, predicted_rating, abs_err]
        output = map(lambda x: str(round(x, 2)), output)
        print(','.join(output))
    print('MAE:', round(sum(absolute_errors) / len(absolute_errors), 2))

def random_sampling(matrix, method_num, size, repeats):
    mean_absolute_errors = []
    for i in range(repeats):
        sample = random_sample(matrix, size)
        absolute_errors = []
        for user_id, item_id in sample:
            predicted_rating = methods.get(method_num)(matrix, user_id, item_id, n)
            actual_rating = matrix[user_id][item_id]
            abs_err = abs(predicted_rating - actual_rating)
            absolute_errors.append(abs_err)
            output = [user_id, item_id, actual_rating, predicted_rating, abs_err]
            output = map(lambda x: str(round(x, 2)), output)
            print(','.join(output))
        mae = mean(absolute_errors)
        print('MAE:', round(mae, 2))
        print('-----------------------------------')
        mean_absolute_errors.append(mae)
    print('Mean MAE:', round(mean(mean_absolute_errors), 2))
    print('Standard Deviation MAE:', 0 if len(mean_absolute_errors) == 1 else round(stdev(mean_absolute_errors), 2))

def main():
    matrix = csv.parse(sys.argv[1])
    # random_sampling(matrix, *map(int, sys.argv[2:]))
    user_specified(matrix, 1, [(0, 8), (15, 78), (22000, 43)])

if __name__ == '__main__':
    main()