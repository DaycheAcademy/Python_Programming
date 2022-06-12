import os
import sys


def list_all_content(path):

    def list_directory(d):
        nonlocal inserted_tabs
        # d = 'c:\myfiles\GitHub\Week 6\'
        all_content = os.listdir(d)
        for item in all_content:

            # 'c:\myfiles\GitHub\Week 6\fibonacci_alternative.py'
            current_path = os.path.join(d, item)
            if os.path.isdir(current_path):
                inserted_tabs += 1
                print('\t' * inserted_tabs, '[DIRECTORY]: ', item)
                list_directory(current_path)
                inserted_tabs -= 1
            else:
                print('\t' * inserted_tabs, '[FILE]: ', item)

    inserted_tabs = 0

    if os.path.exists(path):
        print('\t' * inserted_tabs, '[DIRECTORY]: ', path)
        list_directory(path)
    else:
        print('Path does not exist')
        sys.exit(-1)


if __name__ == '__main__':

    list_all_content('..')

# LEGB
# Local, Enclosing, Global, Builtins


