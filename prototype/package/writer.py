import os.path
from . import table_template

def save_html(html):
    print('저장하고자 하는 파일 이름을 입력하세요. (확장자 없이)')
    file_name = "results/" + input() + '.html'

    if os.path.exists(file_name):
        raise FileExistsError("파일이 이미 존재합니다.")

    with open(file_name, 'w') as file:
        file.write(html)

def to_html(role_dict):
    rows = ""
    for role, person in role_dict.items():
        rows += put_in_table_row(role, person)
    return table_template.TABLE.format(rows=rows)
        
def put_in_table_row(role, person):
    return table_template.ROW.format(role=role, person=person)
