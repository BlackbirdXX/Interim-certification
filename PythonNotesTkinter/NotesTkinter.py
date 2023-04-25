from tkinter import *
from tkinter import messagebox
from tkinter import filedialog



def notes_close():
    ask = messagebox.askokcancel('Exit', 'Do you want to close notes?')
    if ask:
        root.destroy()

def open_file():
    file_path = filedialog.askopenfilename(title= "File Change", filetypes=(('Text docs (*.txt)', '*.txt'), ('All types', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='UTF-8').read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Text docs (*.txt)', '*.txt'), ('All types', '*.*')))
    f = open(file_path, 'w', encoding='UTF-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()


root = Tk()
root.title('Заметки')
root.geometry('600x400')

menu_bar = Menu(root)
menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label='Open', command= open_file)
menu_file.add_command(label='Save', command=save_file)
menu_file.add_command(label='Close', command= notes_close)
root.config(menu=menu_file)
root.config(menu=menu_bar)

menu_bar.add_cascade(label= "File", menu=menu_file)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text, bg='white', fg='black', padx=15, pady=15, wrap=WORD, insertbackground="grey", width=15)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)


root.mainloop()