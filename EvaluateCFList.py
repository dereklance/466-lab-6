import sys, os, evaluation, csv

usage_string = f'usage: python3 {os.path.basename(__file__)} <method_num> <filename>'

def print_help_message():
    print(usage_string)
    print('Implemented collaborative filtering methods (use for <method_num> argument):')
    print('\t1: N Nearest Neighbors using cosine similarity')
    print('\t2: N Nearest Neighbors using Pearson correlation coefficient')

def handle_arguments(args):
    if len(args) == 1:
        print_help_message()
        sys.exit()
    elif len(args) != 3:
        print(usage_string)
        raise ValueError('You must provide 2 arguments')

def parse_input(filename):
    with open(filename) as file:
        lines = file.read().strip().split('\n')
        pairs = [tuple(line.replace(',', ' ').strip().split()) for line in lines]
        return list(map(lambda x: (int(x[0]), int(x[1])), pairs))

def main():
    handle_arguments(sys.argv)
    evaluation.user_specified(csv.parse('dataset.csv'), int(sys.argv[1]), parse_input(sys.argv[2]))

if __name__ == '__main__':
    main()