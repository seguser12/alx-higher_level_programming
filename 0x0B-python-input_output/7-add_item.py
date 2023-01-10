#!/usr/bin/python3
'''working with python input/output'''

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    try:
        args = load_from_json_file('add_item.json')
    except FileNotFoundError:
        args = []
    args.extend(sys.argv[1:])
    save_to_json_file(args, 'add_item.json')
