from index import *
from database import *

document1 = {
    'id': '1',
    'text': 'The big sharks of Belgium drink beer.'
}

document2 = {
    'id': '2',
    'text': 'Belgium has great beer. They drink beer all the time.'
}

document3 = {
    'id': '3',
    'text': 'Belgium has great . They drink  all the time.'
}
db = Database()
index = Index(db)
index.index_document(document1)
index.index_document(document2)
index.index_document(document3)

query = 'beer'

ranked_list = index.search(query)
recall_list = []
for i in ranked_list:
    recall_list.append(db.get(i[0]))
recall_list


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
