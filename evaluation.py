# Ian Battin :ianbattin0@gmail.com
# Derek Lance: dwlance@gmail.com

import sys, csv_parser, n_nearest_neighbors
import basic_predictors
from random import randint
from statistics import mean, stdev

methods = {
    1: lambda matrix, user_id, item_id, n:
        n_nearest_neighbors.predict_rating_average(
            matrix, user_id, item_id, n, similarity = n_nearest_neighbors.cosine_similarity
        ),
    2: lambda matrix, user_id, item_id, n:
        n_nearest_neighbors.predict_rating_average(
            matrix, user_id, item_id, n, similarity = n_nearest_neighbors.pearson_correlation
        ),
    3: lambda matrix, user_id, item_id, n:
        basic_predictors.mean_utility(
            matrix, user_id, item_id
        ),
    4: lambda matrix, user_id, item_id, n:
        n_nearest_neighbors.adjusted_weighted_sum(
            matrix, user_id, item_id, n, similarity = n_nearest_neighbors.cosine_similarity
        )
}

def random_sample(matrix, size):
    num_users = len(matrix)
    num_items = 100
    test_pairs = []
    for i in range(size):
        rating = (randint(0, num_users - 1), randint(0, num_items - 1))
        while matrix[rating[0]][rating[1]] == 99.0:
            rating = randint(0, num_users - 1), randint(0, num_items - 1)
        test_pairs.append(rating)
    return test_pairs

def recommend_joke(rating, threshold = 5):
    return rating >= threshold

def user_specified(matrix, method_num, test_pairs):
    true_recommend, false_recommend, true_not_recommend, false_not_recommend = 0, 0, 0, 0
    accuracy = None
    absolute_errors = []
    for user_id, item_id in test_pairs:
        if matrix[user_id][item_id] == 99.0:
            continue
        predicted_rating = methods.get(method_num)(matrix, user_id, item_id, n)
        actual_rating = matrix[user_id][item_id]
        if recommend_joke(predicted_rating) and recommend_joke(actual_rating):
                true_recommend += 1
        elif recommend_joke(predicted_rating) and not recommend_joke(actual_rating):
            false_recommend += 1
        elif not recommend_joke(predicted_rating) and not recommend_joke(actual_rating):
            true_not_recommend += 1
        else:
            false_not_recommend += 1
        abs_err = abs(predicted_rating - actual_rating)
        absolute_errors.append(abs_err)
        output = [user_id, item_id, actual_rating, predicted_rating, abs_err]
        output = map(lambda x: str(round(x, 2)), output)
        print(','.join(output))
    N = len(list(filter(lambda x:  matrix[x[0]][x[1]] != 99.0, test_pairs)))
    accuracy = print_accuracy_measures(true_recommend, false_recommend, true_not_recommend, false_not_recommend, N)
    print('MAE:', round(sum(absolute_errors) / len(absolute_errors), 2))
    

def print_accuracy_measures(true_recommend, false_recommend, true_not_recommend, false_not_recommend, N):
    print()
    print('%-25s%-25s%-25s' % (f'N = {N}', 'Did Recommend', 'Did not Recommend'))
    print('%-25s%-25i%-25i' % ('Should Recommend', true_recommend, false_not_recommend))
    print('%-25s%-25i%-25i' % ('Should not Recommend', false_recommend, true_not_recommend))
    print()

    precision = round(true_recommend + 1 / (true_recommend + false_recommend + 1), 3)
    recall = round(true_recommend + 1 / (true_recommend + false_not_recommend + 1), 3)
    print('Precision:', precision)
    print('Recall:', recall)
    print('F-1 Measure:', round(2 * precision * recall / (precision + recall), 3))
    accuracy = round((true_recommend + true_not_recommend) / N, 3)
    print('Overall Accuracy:', accuracy)
    return accuracy


def random_sampling(matrix, method_num, size, repeats, n=20):
    mean_absolute_errors = []
    accuracies = []
    for i in range(repeats):
        true_recommend, false_recommend, true_not_recommend, false_not_recommend = 0, 0, 0, 0
        sample = random_sample(matrix, size)
        absolute_errors = []
        for user_id, item_id in sample:
            predicted_rating = methods.get(method_num)(matrix, user_id, item_id, n)
            actual_rating = matrix[user_id][item_id]
            if recommend_joke(predicted_rating) and recommend_joke(actual_rating):
                true_recommend += 1
            elif recommend_joke(predicted_rating) and not recommend_joke(actual_rating):
                false_recommend += 1
            elif not recommend_joke(predicted_rating) and not recommend_joke(actual_rating):
                true_not_recommend += 1
            else:
                false_not_recommend += 1
            abs_err = abs(predicted_rating - actual_rating)
            absolute_errors.append(abs_err)
            output = [user_id, item_id, actual_rating, predicted_rating, abs_err]
            output = map(lambda x: str(round(x, 2)), output)
            print(','.join(output))
        accuracy = print_accuracy_measures(true_recommend, false_recommend, true_not_recommend, false_not_recommend, len(sample))
        accuracies.append(accuracy)
        mae = mean(absolute_errors)
        print('MAE:', round(mae, 2))
        print('-----------------------------------')
        mean_absolute_errors.append(mae)

    print('Mean MAE:', round(mean(mean_absolute_errors), 2))
    print('Standard Deviation MAE:', 0 if len(mean_absolute_errors) == 1 else round(stdev(mean_absolute_errors), 2))
    mean_accuracy = mean(accuracies)
    print('Mean Accuracy:', round(mean_accuracy, 3))
    return mean_accuracy

def main():
    matrix = csv_parser.parse(sys.argv[1])
    # random_sampling(matrix, *map(int, sys.argv[2:]))
    user_specified(matrix, 1, [(0, 8), (15, 78), (22000, 43)])

if __name__ == '__main__':
    print_confusion_matrix(1, 2, 3, 4, 10)