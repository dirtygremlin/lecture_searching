import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as data:
        content = json.load(data)
    if field in content.keys():
        return content[field]
    else:
        return None


def linear_search(sequence, num):
    list = []
    for idx, i in enumerate(sequence):
        if i == num:
            list.append(idx)
    result = dict()
    result["positions"] = list
    result["count"] = len(list)
    return result


def main():

    return


if __name__ == '__main__':
    main()