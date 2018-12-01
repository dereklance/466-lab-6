import evaluation, sys, os, csv_parser

usage_string = f'usage: python3 {os.path.basename(__file__)} <method_num> <size> <repeats>'

def print_help_message():
    print(usage_string)
    print('Implemented collaborative filtering methods (use for <method_num> argument):')
    print('\t1: Average N Nearest Neighbors using cosine similarity')
    print('\t2: Average N Nearest Neighbors using Pearson correlation coefficient')
    print('\t3: Mean Utility')
    print('\t4: N Nearest Neighbors Adjusted Weighted Sum using cosine similarity')

def handle_arguments(args):
    if len(args) == 1:
        print_help_message()
        sys.exit()
    elif len(args) != 4:
        print(usage_string)
        raise ValueError('You must provide 3 arguments')

def main(*args):
    handle_arguments(args)
    evaluation.random_sampling(csv_parser.parse('dataset.csv'), *map(int, sys.argv[1:]))

if __name__ == '__main__':
    main(*sys.argv)