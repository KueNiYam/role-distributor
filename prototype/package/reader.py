def file_to_list(file_name):
    with open(file_name) as file:
        return list(map(lambda str: str.rstrip('\n'), file.readlines()))
