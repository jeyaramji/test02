"""
call the metadata program and collect the complete
metadata and then get the result based on the passed
key
"""
from metadata import metadata


# https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-python-dictionaries-and-lists
def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(key):
    md = metadata()
    return list(gen_dict_extract(key, md))


if __name__ == '__main__':
    key = input("Key?\n")
    print(find_key(key))
