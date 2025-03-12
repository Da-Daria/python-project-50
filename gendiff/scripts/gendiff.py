import argparse
import json
from gendiff.scripts.file_reader import read_json_file

def generate_diff(file1_data, file2_data):
    diff = {}
    keys = sorted(set(file1_data.keys()).union(file2_data.keys()))

    for key in keys:
        if key in file1_data and key not in file2_data:
            diff[key] = f"- {file1_data[key]}"
        elif key not in file1_data and key in file2_data:
            diff[key] = f"+ {file2_data[key]}"
        elif file1_data[key] != file2_data[key]:
            diff[key] = f"- {file1_data[key]}"
            diff[key] = f"+ {file2_data[key]}"
    
    return json.dumps(diff, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', default='plain', help='set format of output')

    args = parser.parse_args()

    file1_data = read_json_file(args.first_file)
    file2_data = read_json_file(args.second_file)

    diff = generate_diff(file1_data, file2_data)
    print(diff)

if __name__ == '__main__':
    main()

