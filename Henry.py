import tkinter as tk
from tkinter import ttk
import mysql.connector
import HenryDOA as HenryDOA
from HenryDOA import HenrySBA

myFont = ("Arial", 16, "bold")

#class GUIsetup():


def comboCallAuthor(event):
    global myList, A_List
        # get will get its value - note that this is always a string
    selIndex = event.widget.current()
    print(selIndex)
    author = myList[selIndex]
    #combobox2
    A_List = HenrySBA().searchBook(author[0])
    print(A_List)
    combobox2['values'] = A_List
    # print(A_List)
    # return A_List
    book_choice = combobox2.bind("<<ComboboxSelected>>", comboCallTitleAut)
    #     return .author[0]
    #     myList2 = backend.henryDB().getTitle(.author)
    #     com2['values'] = myList2
    #     print("Index selected is: " + str(selIndex))
    #     print(selIndex)
    #     return myList2

def comboCallTitleAut(event):
    selIndex2 = event.widget.current()
    #getting selection from combobox to populate the tree
    title = A_List[selIndex2]
    # print("Book Title: ", title)
    branch_names = HenryDOA.HenrySBA().branch_info(title)
    # combobox2['values'] = branch_names
    for i in tree1.get_children():  # Remove any old values in tree list
         tree1.delete(i)

    for i in range(len(HenryDOA.HenrySBA().branch_info(title))):
        vals = branch_names[i]

        # print(vals)
        tree1.insert("", "end", values=[vals[0], vals[1], vals[2]])






# main window
root = tk.Tk()
root.title('Henry Bookstore')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
tab1 = ttk.Frame(notebook, width=400, height=480)
tab2 = ttk.Frame(notebook, width=400, height=480)
tab3 = ttk.Frame(notebook, width=400, height=480)

tab1.pack(fill='both', expand=1)
tab2.pack(fill='both', expand=1)
tab3.pack(fill='both', expand=1)

# name the frames of each tab

notebook.add(tab1, text='Search by Author')
notebook.add(tab2, text='Search by Publisher')
notebook.add(tab3, text='Search by Category')


###AUTHOR TAB(

#Creation of Labels in Author Tab

label1 = ttk.Label(tab1)
label1.grid(column=3, row=3, padx = 25)
label1['text'] = "Author Selection:"

label2 = ttk.Label(tab1)
label2.grid(column=6, row=3, pady =2, padx = 30)
label2['text'] = "Book Selection:"

# Creating a Tree in Author Tab
tree1 = ttk.Treeview(tab1, columns=('Branch', 'Copies', 'Price'), show='headings')
tree1.heading('Branch', text='Branch Name')
tree1.heading('Copies', text='Copies Available')
tree1.heading('Price', text='Price')
tree1.grid(column=1, row=1)

        # .label3 = ttk.Label(.tab1)
        # .label3.grid(column=9, row=3)
        # .label3['text'] = "Price in USD:"

# Author Combobox SBA

combobox1 = ttk.Combobox(tab1, width=20, state="readonly", font = myFont)
combobox1.grid(column=3, row=30, padx= 25)
myList = HenrySBA().searchAuthor()
#Values in the dropdown meny obrained from the SQL code in search author function in DOA
combobox1['values'] = myList
combobox1.current(0)
combobox1.bind("<<ComboboxSelected>>", comboCallAuthor)


#Title Combobox SBA

combobox2 = ttk.Combobox(tab1, width=20, state="readonly", font = myFont)
combobox2.grid(column=6, row=30, padx=30)
T_List = []
# combobox2.bind("<<ComboboxSelected>>", comboCallTitlePub)

###AUTHOR TAB END)


###PUBLISHER TAB START(

#adding publisher names from query to dropdown
def comboCallPub(event):
    global pubList
    # get will get its value - note that this is always a string
    pubIndex = event.widget.current()
    publisher = myList(pubIndex)
    # combobox2
    pubList = HenrySBA().PubName(publisher)
    pubComboBox2['values'] = pubList
    return pubList

#retreive book info (same as above)
def comboCallTitlePub(event):

    pubIndex2 = event.widget.current()
    #getting selection from combobox to populate the tree
    title = pubList[pubIndex2]
    print("Book Title: ", title)
    branch_names = HenryDOA.HenrySBA().branch_info(title)
    pubComboBox2['values'] = branch_names
    # for i in tree2.get_children():  # Remove any old values in tree list
    #      tree2.delete(i)
    # i = 0
    # for row in branch_names:
    #     tree2.insert("", "end", values=[branch_names[0], branch_names[1], branch_names[2]])

#Tree creation in publisher tab(2)
tree2 = ttk.Treeview(tab2, columns=('Branch', 'Copies', 'Price'), show='headings')
tree2.heading('Branch', text='Branch Name')
tree2.heading('Copies', text='Copies Available')
tree2.heading('Price', text='Price')
tree2.grid(column=1, row=1)

#pub combobox label
pubLabel = ttk.Label(tab2)
pubLabel.grid(column=0, row=3)
pubLabel['text'] = "Publisher Selection:"

#pub combobox to get pub name

pubComboBox = ttk.Combobox(tab2, width = 20, state="readonly")
pubComboBox.grid(column=0, row=5)
pubList2 = HenryDOA.HenrySBA().PubName("Tor Books")
pubComboBox['values'] = pubList2
pubComboBox.current(0)
pubComboBox.bind("<<ComboboxSelected>>", comboCallPub)

#pub combobox 2 to get book title

pubList = []
pubComboBox2 = ttk.Combobox(tab2, width = 20, state="readonly")
pubComboBox2.grid(column=0, row=5)
# pubComboBox2.bind("<<ComboboxSelected>>", comboCallTitle)


###PUBLISHER TAB END)

###CATEGORY TYPE START(

def comboCallCat(event):
    global catList
    # get will get its value - note that this is always a string
    catIndex = event.widget.current()
    category = myList(catIndex)
    # combobox2
    catList = HenrySBA().PubName(category)
    print('Category List: ', catList)
    catComboBox2['values'] = catList
    return catList

def comboCallTitleCat(event):
    catIndex2 = event.widget.current()
    #getting selection from combobox to populate the tree
    title = catList[catIndex2]
    print("Book Title: ", title)
    # branch_names = HenryDOA.HenrySBA().branch_info(title)
    # catComboBox2['values'] = branch_names
    # for i in tree3.get_children():  # Remove any old values in tree list
    #      tree3.delete(i)
    # i = 0
    # for row in branch_names:
    #     tree3.insert("", "end", values=[branch_names[0], branch_names[1], branch_names[2]])
    #     i= i+1

#Tree Creation for category tab
tree3 = ttk.Treeview(tab3, columns=('Branch', 'Copies', 'Price'), show='headings')
tree3.heading('Branch', text='Branch Name')
tree3.heading('Copies', text='Copies Available')
tree3.heading('Price', text='Price')
tree3.grid(column=1, row=1)

#cat combobox label
catLabel = ttk.Label(tab3)
catLabel.grid(column=0, row=3)
catLabel['text'] = "Category Selection:"

#cat combobox to get cat name

catComboBox = ttk.Combobox(tab3, width = 20, state="readonly")
catComboBox.grid(column=0, row=5)
# catList2 = HenryDOA.HenrySBA().CatName(category)
# catComboBox['values'] = pubList
# catComboBox.current(0)
# catComboBox.bind("<<ComboboxSelected>>", comboCallCat)

#cat combobox 2 to get book title

catList = []
catComboBox2 = ttk.Combobox(tab3, width = 20, state="readonly")
catComboBox2.grid(column=0, row=5)
catComboBox2.bind("<<ComboboxSelected>>", comboCallTitleCat)


root.mainloop()


###*Worked with classmate Duncan , Andy, and Danny*
