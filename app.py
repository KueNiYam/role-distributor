from package import reader
from package import distributor
from package import writer

if __name__ == '__main__':
    roles = reader.file_to_list('data/roles.txt')
    people = reader.file_to_list('data/people.txt')

    role_dict = distributor.distribute_role(roles, people)

    writer.save_html(writer.to_html(role_dict))