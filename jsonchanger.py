import json
from random import random


def loud_from_json(filename):
    with open(filename, 'r') as openfile:
        # Reading from json file
        return json.load(openfile)


def save_to_json(filename, l):
    with open(filename, 'w') as outfile:
        json.dump(l, outfile)


def replace_numbers(dict):
    l = []
    for n in dict:
        if n == 0:
            l.append(1)
        elif n == 1:
            l.append(0)
        else:
            l.append(n)
    return l


def random_numbers(dict):
    l = []
    for n in dict:
        l.append(int(random() * 2))
    return l


def run_replace(filename):
    save_to_json(filename, replace_numbers(loud_from_json(filename)))


def get_list_replace(filename):
    return replace_numbers(loud_from_json(filename))


def run_replace_to_other_file(src, dest):
    save_to_json(dest, replace_numbers(loud_from_json(src)))


def run_random(filename):
    save_to_json(filename, random_numbers(loud_from_json(filename)))


def get_list_random(filename):
    return random_numbers(loud_from_json(filename))


def run_random_to_other_file(src, dest):
    save_to_json(dest, random_numbers(loud_from_json(src)))


if __name__ == '__main__':
    filename = 'y_test.json'
    print(get_list_random(filename))
    print(get_list_replace(filename))
