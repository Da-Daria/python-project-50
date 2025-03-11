import argparse
from gendiff.scripts.file_reader import read_json_file

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', default='plain', help='set format of output')

    args = parser.parse_args()

    file1_data = read_json_file(args.first_file)
    file2_data = read_json_file(args.second_file)

    print(file1_data)
    print(file2_data)

if __name__ == '__main__':
    main()

