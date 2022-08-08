import project_functions as pf
from sklearn.ensemble import RandomForestClassifier
from tkinter import *

main_window = Tk() 

main_window.title("Product Classifier")
main_window.geometry("280x100") 

main_window.grid()

frame = Frame(main_window)
frame.grid()

l_url = Label(frame, text="Insert a url: ")
l_url.grid(row=0, column=0)

e_mensagem = Entry(frame)
e_mensagem.grid(row=0, column=1)

frame2 = Frame(main_window)
frame2.grid(row=1,column=0)
v = StringVar()

l_answer = Label(frame, text="Category: ")
l_answer.grid(row=2, column=0)

Label(frame2, textvariable=v).grid()

v.set("")

def get_product_category():      
    url = e_mensagem.get()
    v.set("analyzing the url...")
    answer = pf.get_classification(url)
    v.set(answer)
        
Button(frame, text="Run", command=get_product_category).grid(row=0, column=2)


main_window.mainloop()
