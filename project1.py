import json
from tkinter import *






def resourceData():
    global dataSource
    dataSource = json.load(open("dictionary_compact.json", 'r'))


def wordSearch(word):
    resourceData()
    word = word.lower()

    corword = word

    if corword not in dataSource:
        length = len(word)

        while corword not in dataSource:
            corword = word[0:length]
            if corword in dataSource:
                '''
                print("Did you mean ", corword, "?")
                '''
                a = dataSource[corword]
                b = "Did you mean "+ corword+"?"+"\n\n"+a
                return b

            length = length - 1
            if length == 0:
                break

    else:
        a = dataSource[corword]
        return a


def display():
    ans = wordSearch(e1_value.get())

    t1.delete("1.0", END)
    t1.insert(END, ans)




window = Tk()


window.configure(background="light green")
head = Label(window, text="Enter the word you wish to search", height=5, width=100,fg='black', bg='light yellow', font="Sans")
e1_value =StringVar()

e1 = Entry(window, textvariable=e1_value, width=20,bg='light yellow')

t1 = Text(window, height=30, width=100, font="Sans")

b1 = Button(window, text="Search", command=display,fg='black', bg='light yellow',  width=10)


head.grid(row=0, column=0)
e1.grid(row=0, column=10)
t1.grid(row=2, column=0)
b1.grid(row=2, column=10)


window.mainloop()


'''
a = input("Enter any word :")
b = wordSearch(a)
print("\n",b)
'''

