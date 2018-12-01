import evaluation, sys, os, csv

usage_string = f'usage: python3 {os.path.basename(__file__)} <method_num> <size> <repeats> [optional n]'

def print_help_message():
    print(usage_string)
    print('Implemented collaborative filtering methods (use for <method_num> argument):')
    print('\t1: N Nearest Neighbors using cosine similarity')
    print('\t2: N Nearest Neighbors using Pearson correlation coefficient')

def handle_arguments(args):
    if len(args) == 1:
        print_help_message()
        sys.exit()
    elif len(args) != 4 and len(args) != 5:
        print(usage_string)
        raise ValueError('You must provide 3 or 4 arguments')

def main(*args):
    handle_arguments(args)
    evaluation.random_sampling(csv.parse('dataset.csv'), *map(int, sys.argv[1:]))

if __name__ == '__main__':
    main(*sys.argv)