import csv_parser, sys, math, random, time, bisect, heapq, numpy as np
from operator import itemgetter

def filter_unrated_jokes(x1, x2):
    v1 = []
    v2 = []
    for i in range(len(x1)):
        if x1[i] == 99.0 or x2[i] == 99.0:
            continue
        v1.append(x1[i])
        v2.append(x2[i])
    return v1, v2

def cosine_similarity(x1, x2):
    v1, v2 = filter_unrated_jokes(x1, x2)

    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    denom = math.sqrt(sumxx * sumyy)
    return sumxy / denom if denom != 0 else -1

def pearson_correlation(x1, x2):
    v1, v2 = filter_unrated_jokes(x1, x2)

    N = len(v1)
    numerator = N * sum(x * y for x, y in zip(v1, v2)) - sum(v1) * sum(v2)
    denom1 = N * sum(x ** 2 for x in v1) - sum(v1) ** 2
    denom2 = N * sum(y ** 2 for y in v2) - sum(v2) ** 2
    denom = math.sqrt(denom1 * denom2)
    return numerator / denom if denom != 0 else -2

def ordered_neighbors(rating_matrix, user_id, item_id, similarity_func, n):
    rating_vector1 = rating_matrix[user_id]
    neighbors = []
    for index, rating_vector2 in enumerate(rating_matrix):
        if index == user_id or rating_vector2[item_id] == 99.0:
            continue
        similarity = similarity_func(rating_vector1, rating_vector2)
        neighbors.append((similarity, rating_vector2[item_id]))
    return list(map(itemgetter(1), heapq.nlargest(n, neighbors, key=itemgetter(0))))

def ordered_neighbors_optimized(rating_matrix, user_id, item_id, similarity_func, n):
    rating_vector1 = rating_matrix[user_id]
    neighbors = []
    for index, rating_vector2 in enumerate(rating_matrix):
        if index == user_id or rating_vector2[item_id] == 99.0:
            continue
        similarity = similarity_func(rating_vector1, rating_vector2)
        neighbors.append((similarity, rating_vector2[item_id]))
    np_array = np.array(neighbors, dtype=[('similarity', 'f4'), ('rating', 'f4')])
    x = np.partition(np_array, np_array.size - n + 1, order='similarity')
    return x[-n:]

def ordered_neighbors_with_similarities(rating_matrix, user_id, item_id, similarity_func, n):
    rating_vector1 = rating_matrix[user_id]
    neighbors = []
    for index, rating_vector2 in enumerate(rating_matrix):
        if index == user_id or rating_vector2[item_id] == 99.0:
            continue
        similarity = similarity_func(rating_vector1, rating_vector2)
        neighbors.append((similarity, rating_vector2[item_id]))
    k_nearest = heapq.nlargest(n, neighbors, key=itemgetter(0))
    return k_nearest

def predict_rating_average(rating_matrix, user_id, item_id, n, similarity = cosine_similarity):
    rating = rating_matrix[user_id][item_id]
    rating_matrix[user_id][item_id] = 99.0
    rating_vector = rating_matrix[user_id]
    neighbor_ratings = ordered_neighbors(rating_matrix, user_id, item_id, similarity, n)
    predicted_rating = sum(neighbor_ratings) / len(neighbor_ratings)
    rating_matrix[user_id][item_id] = rating
    return predicted_rating

def predict_rating_optimized(rating_matrix, user_id, item_id, n, similarity = cosine_similarity):
    rating = rating_matrix[user_id][item_id]
    rating_matrix[user_id][item_id] = 99.0
    rating_vector = rating_matrix[user_id]
    neighbor_ratings = ordered_neighbors_optimized(rating_matrix, user_id, item_id, similarity, n)
    predicted_rating = sum(y for x,y in neighbor_ratings) / len(neighbor_ratings)
    rating_matrix[user_id][item_id] = rating
    return predicted_rating

def compute_average_rating(rating_vector):
    total = 0
    count = 0
    for i in range(len(rating_vector)):
        if rating_vector[i] != 99:
            total += rating_vector[i]
            count += 1

    return total / count

def adjusted_weighted_sum(rating_matrix, user_id, item_id, n, similarity = cosine_similarity):
    rating = rating_matrix[user_id][item_id]
    rating_matrix[user_id][item_id] = 99.0
    rating_vector = rating_matrix[user_id]
    neighbor_ratings = ordered_neighbors_with_similarities(rating_matrix, user_id, item_id, similarity, n)
    average_rating = compute_average_rating(rating_vector)

    k = 1 / sum(abs(x) for x,y in neighbor_ratings)
    summation = sum((x * (y - average_rating)) for x,y in neighbor_ratings)
    predicted_rating =  average_rating + k * summation
    rating_matrix[user_id][item_id] = rating
    return predicted_rating

def random_predict_rating(a, b, c, d):
    return random.random() * 20 - 10

def main(program_name, file_name, n):
    matrix = csv_parser.parse(file_name)
    start_time = time.time()
    rating = adjusted_weighted_sum(matrix, 0, 0, int(n))
    print(f"rating: {rating}, time: {time.time() - start_time} seconds")

if __name__ == '__main__':
    main(*sys.argv)