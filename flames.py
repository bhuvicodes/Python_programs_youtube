from tkinter import *

def remove_match(name1, name2):

    for i in range(len(name1)):
        for j in range(len(name2)):

            if name1[i] == name2[j]:
                c = name1[i]

                name1.remove(c)
                name2.remove(c)

                list = name1 +["*"] + name2
                return [list, True]
    list = name1 + ["*"] + name2
    return[list, False]

def tell_status():

    p1 = person1_field.get()
    p1 = p1.lower()
    p1.replace(" ", "")
    p1_list = list(p1)

    p2 = person2_field.get()
    p2 = p2.lower()
    p2.replace(" ", "")
    p2_list = list(p2)

    proceed = True

    while proceed:
        ret_list = remove_match(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index+1 : ]
    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Sibilings"]

    while len(result) > 1:
        split_index = (count % len(result)-1)
        if split_index >=0:
            right = result[split_index + 1 : ]
            left = result[: split_index]

            result = right + left
        else:
            result = result[ : len(result)- 1]

    status_field.insert(10, result[0])

def clear_all():
    person1_field.delete(0, END)
    person2_field.delete(0, END)
    status_field.delete(0, END)

    person1_field.focus_set()

if __name__ == "__main__":
    root = Tk()
    root.configure(background = "black")
    root.geometry("350x125")
    root.title("FLAMES")

    label1 = Label(root, text = "Nmae of the person 1:",
                   fg = "white", bg = "black")
    label2 = Label(root, text = "Name of the person 2:", 
                   fg = "white", bg = "black")
    label3 = Label(root, text = "Relationship Status:",
                   fg = "white", bg = "red")

    label1.grid(row = 1, column = 0, sticky = "E")
    label2.grid(row = 2, column = 0, sticky = "E")
    label3.grid(row = 4, column = 0, sticky ="E")

    person1_field = Entry(root)
    person2_field = Entry(root)
    status_field = Entry(root)

    person1_field.grid(row = 1, column = 1, ipadx = "50")
    person2_field.grid(row = 2, column = 1, ipadx = "50")
    status_field.grid(row = 4, column = 1, ipadx = "50")

    button1 = Button(root, text = "Submit", bg = "red",
                    fg = "black", command = tell_status)
    button2 = Button(root, text = "Clear", bg = "red",
                    fg = "black", command = clear_all)
    
    button1.grid(row = 3, column = 1)
    button2.grid(row = 5, column = 1)

    root.mainloop()
    
