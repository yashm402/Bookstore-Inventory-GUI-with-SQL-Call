import mysql.connector

class HenrySBA():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            user='root',
            passwd='Atlanta91',
            database='henry',
            host='127.0.0.1')

        self.mycur = self.mydb.cursor()

    def searchAuthor(self):

        #perform this query
        sql = "SELECT * FROM henry_author"
        self.mycur.execute(sql)

        self.author_list = []
        for row in self.mycur:
            # self.author_id = row[0]
            # self.last_name = row[1]
            # self.first_name = row[2]
            self.author_list.append([row[1]])
            # print("AuthorID: " + str(self.author_id) + ", name " + self.first_name +" " + self.last_name)
        return (self.author_list)

    def searchBook(self, author):
        self.author_b = author
        sql = "SELECT book.TITLE " \
              "FROM henry_author as author " \
              "JOIN henry_wrote as wrote " \
              "ON author.AUTHOR_NUM = wrote.AUTHOR_NUM " \
              "JOIN henry_book as book " \
              "ON wrote.BOOK_CODE = book.BOOK_CODE " \
              "WHERE author.AUTHOR_LAST = '" + self.author_b[0] + "'"

        #"WHERE author.AUTHOR_LAST = 'Morrison';"
        self.mycur.execute(sql)

        self.book_list = []

        for row in self.mycur:
            self.book_list.append(row)

        return (self.book_list)

    def book_info(self, specs):
        self.book_specs = specs
        "SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE " \
        "FROM henry_book as book " \
        "JOIN henry_inventory as inventory " \
        "ON book.BOOK_CODE = inventory.BOOK_CODE " \
        "JOIN henry_branch as branch " \
        "ON inventory.BRANCH_NUM = branch.BRANCH_NUM " \
        "WHERE book.TITLE = '" + self.specs[0] + "'"

        self.inventory = []

        for row in self.mycur:
            self.inventory.append([row[0]. row[1], row[2]])

        print (self.inventory)
        return (self.inventory)
#class HenrySBP():

#class HenrySPC():
