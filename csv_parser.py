import sys

def parse(file_path):
    with open(file_path) as data_file:
        lines = data_file.read().strip().split()
        return [list(map(float, line.strip().split(',')))[1:] for line in lines]

def main():
    matrix = parse(sys.argv[1])
    for index, rating_list in enumerate(matrix):
        if len(rating_list) != 101:
            print(index, len(rating_list))
    print(matrix[0])
    print(len(matrix))

if __name__ == '__main__':
    main()