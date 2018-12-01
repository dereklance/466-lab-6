# Ian Battin :ianbattin0@gmail.com
# Derek Lance: dwlance@gmail.com

def mean_utility(matrix, user, item):
  total_rating, count = 0, 0
  for i in range(len(matrix)):
    if i != user:
      rating = matrix[i][item]
      if rating != 99:
        total_rating += rating
        count += 1

  return total_rating / count

def main():
  matrix = csv_parser.parse(file_name)
  average_user_ratings - calculate_average_user_ratings(matrix)
  start_time = time.time()
  rating = predict_rating_average(matrix, 0, 0, 500)
  print(f'rating: {rating}, time: {time.time() - start_time} seconds')

if __name__ == "__main__":
    main()