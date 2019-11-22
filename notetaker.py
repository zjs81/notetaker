from tkinter import *
from tkinter import messagebox
import pandas as pd


window = Tk()
 
window.title("Call Command Notes")
window.geometry('350x200')
lbl = Label(window, text="Ticket")
lbl2 = Label(window, text="Number")
lbl3 = Label(window, text="Name")
lbl4 = Label(window, text="Issue")
lbl.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=2)
lbl4.grid(column=0, row=3)



txt = Entry(window,width=20)
txt2 = Entry(window,width=20)
txt3 = Entry(window,width=20)
txt4 = Entry(window,width=20)

txt.grid(column=1, row=0)
txt2.grid(column=1, row=1)
txt3.grid(column=1, row=2)
txt4.grid(column=1, row=3)
def save():
    messagebox.showinfo('Attention', 'Saved')
    global txt,txt2,txt3,txt4
    data = {}
    data['Ticket Number'] = txt.get()
    data['Phone Number'] = txt2.get()
    data['Name'] = txt3.get()
    data['Issue'] = txt4.get()
    data = pd.DataFrame.from_dict(data)
    writer = pd.ExcelWriter('logs.xlsx')
    data.to_excel(writer,'test')
    writer.save()
 
btn = Button(window, text="save", command=save)
 
btn.grid(column=0, row=4)



window.mainloop()



def save():
    messagebox.showinfo('Attention', 'Saved')
    #with pd.ExcelWriter('logs.xlsx') as writer:
    #    df_info.to_excel(writer, sheet_name='note')
