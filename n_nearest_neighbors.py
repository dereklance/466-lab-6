import csv, sys, math, random
from operator import itemgetter

def pearson_correlation(v1, v2):
    N = len(v1)
    numerator = N * sum(x * y for x, y in zip(v1, v2)) - sum(v1) * sum(v2)
    denom1 = N * sum(x ** 2 for x in v1) - sum(v1) ** 2
    denom2 = N * sum(y ** 2 for y in v2) - sum(v2) ** 2
    return numerator / math.sqrt(denom1 * denom2)

def ordered_neighbors(rating_matrix, user_id):
    rating_vector1 = rating_matrix[user_id]
    neighbors = []
    for index, rating_vector2 in enumerate(rating_matrix):
        if index == user_id:
            continue
        similarity = pearson_correlation(rating_vector1, rating_vector2)
        neighbors.append((similarity, rating_vector2))
    neighbors.sort(reverse = True, key = itemgetter(0))
    return neighbors

def predict_rating(rating_matrix, user_id, item_id, n):
    rating = rating_matrix[user_id][item_id]
    rating_matrix[user_id][item_id] = 99.0
    rating_vector = rating_matrix[user_id]
    neighbors = ordered_neighbors(rating_matrix, user_id)

    # might need to eliminate values of 99 from consideration
    neighbor_ratings = list(filter(lambda rating: rating != 99.0, [vector[item_id] for _, vector in neighbors]))[:n]
    predicted_rating = 1 / len(neighbor_ratings) * sum(neighbor_ratings)
    ################

    rating_matrix[user_id][item_id] = rating
    return predicted_rating

def random_predict_rating(a, b, c, d):
    return random.random() * 20 - 10

def main():
    matrix = csv.parse(sys.argv[1])
    n = int(sys.argv[2])
    predicted_ratings = [predict_rating(matrix, 0, i, n) for i in range(100)]
    actual_ratings = matrix[0]
    differences = [None if act == 99.0 else pred - act for pred, act in zip(predicted_ratings, actual_ratings)]
    print(differences)

if __name__ == '__main__':
    main()