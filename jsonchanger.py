import json


def loud_from_json(filename):
    with open(filename, 'r') as openfile:
        # Reading from json file
        return json.load(openfile)

def save_to_json(filename, l):
    with open(filename, 'w') as outfile:
        json.dump(l, outfile)

def change_numbers(dict):
    l=[]
    for n in dict:
        if n ==0:
            l.append(1)
        elif n ==1:
            l.append(0)
        else:
            l.append(n)
    return l

def run(filename):
    save_to_json(filename, change_numbers(loud_from_json(filename)))

def run_to_other_file(src, dest):
    save_to_json(dest, change_numbers(loud_from_json(src)))

if __name__ == '__main__':
    filename = 'y_test.json'
    run(filename)
    with open(filename, 'r') as f:
        aa = json.load(f)
    print(aa)

