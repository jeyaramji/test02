import requests
import json

metadata_url = 'http://169.254.169.254/latest/'
metadata_path = ["meta-data/"]


def crawl_tree(url, paths):
    """
    Iterates through the metadata and fetch all the results in dictionary
    :param url: url to fetch
    :param paths: path to hit
    :return: complete json result as dict
    """
    result = {}
    for path in paths:
        new_url = url + path
        r = requests.get(new_url)
        text = r.text
        if path[-1] == "/":
            list_of_values = r.text.splitlines()
            result[path[:-1]] = crawl_tree(new_url, list_of_values)
        elif is_valid_json(text):
            result[path] = json.loads(text)
        else:
            result[path] = text
    return result


def metadata():
    md = crawl_tree(metadata_url, metadata_path)
    return metadata


def is_valid_json(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(metadata())
