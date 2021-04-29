import tkinter as tk
from tkinter import ttk
import mysql.connector
from HenryDOA import HenrySBA

myFont = ("Arial", 16, "bold")
class GUIsetup():

#created tkinter window
    def __init__(self):
        self.root = tk.Tk()
        self.create()
        self.root.mainloop()
        #self.comboCall2()



# main window
    def create(self):

        self.root.title('Henry Bookstore')


# create a notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

# create frames
        self.tab1 = ttk.Frame(self.notebook, width=400, height=480)
        self.tab2 = ttk.Frame(self.notebook, width=400, height=480)
        self.tab3 = ttk.Frame(self.notebook, width=400, height=480)

        self.tab1.pack(fill='both', expand=1)
        self.tab2.pack(fill='both', expand=1)
        self.tab3.pack(fill='both', expand=1)

# adds frames to notebook

        self.notebook.add(self.tab1, text='Search by Author')
        self.notebook.add(self.tab2, text='Search by Publisher')
        self.notebook.add(self.tab3, text='Search by Category')

#Creation of Labels

        """Labels in SBA"""
        self.label1 = ttk.Label(self.tab1)
        self.label1.grid(column=3, row=3, padx = 25)
        self.label1['text'] = "Author Selection:"

        self.label2 = ttk.Label(self.tab1)
        self.label2.grid(column=6, row=3, pady =2, padx = 30)
        self.label2['text'] = "Book Selection:"

        # self.label3 = ttk.Label(self.tab1)
        # self.label3.grid(column=9, row=3)
        # self.label3['text'] = "Price in USD:"

# Author Combobox SBA

        self.combobox1 = ttk.Combobox(self.tab1, width=20, state="readonly", font = myFont)
        self.combobox1.grid(column=3, row=30, padx= 25)
        #Values in the dropdown meny obrained from the SQL code in search author function in DOA
        self.combobox1['values'] = HenrySBA().searchAuthor()
        # self.combobox1.current(0)
        self.combobox2 = ttk.Combobox(self.tab1, width=20, state="readonly", font = myFont)
        self.combobox2.grid(column=6, row=30, padx=30)
        self.author_select = self.combobox1.bind("<<ComboboxSelected>>", self.comboCall)



        # self.combobox2['values'] = HenrySBA().searchBook(self.author)
        #
        #self.combobox2.bind("<<ComboboxSelected>>", self.combo2)

# Creating a Tree
        self.tree1 = ttk.Treeview(self.tab1, columns=('Branch', 'Copies', 'Price'), show='headings')
        self.tree1.heading('Branch', text='Branch Name')
        self.tree1.heading('Copies', text='Copies Available')
        self.tree1.heading('Price', text='Price')
        self.tree1.grid(column=1, row=1)

        # for i in self.tree1.get_children():  # Remove any old values in tree list
        #     self.tree1.delete(i)
        #
        # for row in myList:
        #     self.tree1.insert("", "end", values=[row, "Name Unknown"])


    # Book Combobox SBA
    def comboCall(self,event):
        # get will get its value - note that this is always a string
        selIndex = event.widget.current()
        self.author = HenrySBA().searchAuthor()[selIndex]
        print("Selected Author", self.author[0])
        self.combobox2['values'] = HenrySBA().searchBook(self.author)
        self.book_choice = self.combobox2.bind("<<ComboboxSelected>>", self.combo2)
        # return self.author[0]
        # myList2 = backend.henryDB().getTitle(self.author)
        # com2['values'] = myList2
        # print("Index selected is: " + str(selIndex))
        # print(selIndex)
        # return myList2

    def combo2(self, event):

        selIndex2 = event.widget.current()
        self.combobox2.grid(column=6, row=30, padx=30)
        self.book_selected = HenrySBA().searchBook(self.author)[selIndex2]


        print(self.book_selected[0])
        #self.comboCall2()
        #return
        # print(self.author)
        # self.combobox2['values'] = HenrySBA().searchBook(self.author)
        #print(HenrySBA().searchAuthor()[event.widget.current()])     ***Send to SQL for next query search

    #def comboCall2(self, event):
        selIndex3 = event.widget.current()
        self.inventory = HenrySBA().searchAuthor()[selIndex3]
 #
 # ##Need branch number and

# selIndex = event.widget.current()
# print("Index selected is: " + str(selIndex))

"""Labels in SBC"""
        # self.label1 = ttk.Label(self.tab2)
        # self.label1.grid(column=3, row=3)
        # self.label1['text'] = " Selection:"





# class HenrySBA():
#
#     def __init__(self):
#         self.mydb = mysql.connector.connect(
#             user='root',
#             passwd='Atlanta91',
#             database='henry',
#             host='127.0.0.1')
#
#         self.mycur = self.mydb.cursor()
#
#     def searchAuthor(self):
#
#         #perform this query
#         sql = "SELECT * FROM henry_author"
#         self.mycur.execute(sql)
#
#         self.author_list = []
#         for row in self.mycur:
#             # self.author_id = row[0]
#             # self.last_name = row[1]
#             # self.first_name = row[2]
#             self.author_list.append([row[1]])
#             # print("AuthorID: " + str(self.author_id) + ", name " + self.first_name +" " + self.last_name)
#
#         return (self.author_list)
#
#     def searchBook(self, author):
#         sql = "SELECT book.TITLE " \
#               "FROM henry_author as author " \
#               "JOIN henry_wrote as wrote " \
#               "ON author.AUTHOR_NUM = wrote.AUTHOR_NUM " \
#               "JOIN henry_book as book " \
#               "ON wrote.BOOK_CODE = book.BOOK_CODE " \
#               "WHERE author.AUTHOR_LAST = '" + author + "'" \
#
#         #"WHERE author.AUTHOR_LAST = 'Morrison';"
#         self.mycur.execute(sql)
#
#         self.book_list = []
#
#         for row in self.mycur:
#             self.book_list.append(row)
#
#         return (self.book_list)
#



# print(HenrySBA().searchAuthor())
setup = GUIsetup()
setup.create()
author = HenrySBA()
author.searchAuthor()



###*Worked with classmate Duncan Furguson, Andy, and Danny*
