import n_nearest_neighbors
import csv
import csv_parser
import sys

def main():
  matrix = csv_parser.parse(sys.argv[1])
  output_file = sys.argv[2]

  with open(output_file, 'w+') as output:
    csvwriter = csv.writer(output)

    for user in matrix:
      similarity_vector = []
      for other_user in matrix:
        similarity_vector.append(round(n_nearest_neighbors.cosine_similarity(user, other_user), 3))
      csvwriter.writerow(similarity_vector)

if __name__ == "__main__":
    main()