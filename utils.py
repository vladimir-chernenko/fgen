import os
from isort import SortImports


def j(*args):
    return os.path.join(*args)


def file_writer(file_name, text_dict):
    """Safely insert text to file, and sorts imports automatically

    Args:
        file_name (TYPE): File name, will be used as ``
        text_dict (TYPE):
            {
                'start': [lines...], # special one
                'end': [lines...], # special one
                'any_pattern': [lines...]
            }
            'any_pattern' is checked with `if 'any_pattern' in line`
    """
    file_name = os.path.abspath(file_name)

    with open(file_name, 'r') as file:
        lines = file.readlines()
        file_text = ''.join(lines)

        for index, line in enumerate(lines):
            for point_line in text_dict.keys():
                insert = False

                if point_line == 'start' and index == 0:
                    insert = True
                elif point_line == 'end' and index == len(lines):
                    insert = True
                elif point_line in line:
                    insert = True

                if insert:
                    insert = False
                    for new_line in text_dict[point_line]:
                        if new_line not in file_text:
                            lines.insert(index + 1, new_line + '\n')

    file_name_bak = '{}.bak'.format(file_name)

    with open(file_name_bak, 'w') as file_backup:
        file_backup.writelines(lines)

    os.remove(file_name)
    os.rename(file_name_bak, file_name)

    SortImports(file_name)
