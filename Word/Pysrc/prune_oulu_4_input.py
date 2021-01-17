import os
import sys


def input_generator(input_filename):
    with open(input_filename, 'r') as f:
        for line in f:
            yield line


def line_is_legal(line):
    if len(line) == 0:
        return False
    if line.count('\t') < 2:
        return False
    return True


def pruned_line(line):
    if line_is_legal(line):
        return ''.join((line.split('\t')[1], '\n'))
    else:
        return ''


def write2output(output_filename, lines):
    with open(output_filename, 'w') as f:
        for line in lines:
            f.write(pruned_line(line))


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = '_pruned'.join(os.path.splitext(input_file))
    input_lines = input_generator(input_file)
    write2output(output_file, input_lines)
