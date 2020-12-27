import csv
import sys
from collections import defaultdict
from typing import IO, TextIO, Tuple


# Read CSV file
def read_csv(file: TextIO) -> Tuple[list, list]:
    reader = csv.reader(file)

    data = list()
    for line in reader:
        data.append(line)

    header = data.pop(0)
    return header, data


# Filter the top-N files with the highest number of ratings
def filter_by_content(data: list, content_size: int, remove_size: int) -> list:
    content_dict = defaultdict(int)

    for row in data:
        content_dict[row[2]] = int(content_dict[row[2]]) + 1

    sorted_content = sorted(content_dict.items(), key=lambda x: x[1], reverse=True)

    content_list = list()
    for count, user_data in enumerate(sorted_content):
        if remove_size <= count < content_size + remove_size:
            content_list.append(user_data[0])
    content_list.sort(key=lambda x: int(x))

    return content_list


# Filter the top-N users with the most ratings
def filter_by_user(content_list: list, data: list, user_size: int, remove_size: int) -> list:
    user_dict = defaultdict(int)

    for row in data:
        if row[2] in content_list:
            user_dict[row[1]] = int(user_dict[row[1]]) + 1

    sorted_user = sorted(user_dict.items(), key=lambda x: x[1], reverse=True)

    user_list = list()
    for count, user_data in enumerate(sorted_user):
        if remove_size <= count < user_size + remove_size:
            user_list.append(user_data[0])
    user_list.sort(key=lambda x: int(x))

    result_data = list()
    for value in data:
        if value[1] in user_list and value[2] in content_list:
            result_data.append(value)

    return result_data


def write_to_csv(header: str, result_data: list, output_file: IO):
    output_file.write(header + '\n')
    for data in result_data:
        line = f'{data[0]},{data[1]},{data[2]},{data[3]}\n'
        output_file.write(line)


def main():
    base_file: TextIO = open(sys.argv[1], "r")
    output_file: TextIO = open(sys.argv[2], "w")
    user_size: int = int(sys.argv[3])
    content_size: int = int(sys.argv[4])
    remove_size: int = int(sys.argv[5])

    header, data = read_csv(base_file)

    content_list: list = filter_by_content(data, content_size, remove_size)
    result_data: list = filter_by_user(content_list, data, user_size, remove_size)

    write_to_csv(','.join(header), result_data, output_file)

    base_file.close()
    output_file.close()


if __name__ == "__main__":
    main()
