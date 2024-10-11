from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from output1 import output  

def get_notepad():
    def newfile():
        global file
        root.title("Untitled - Notepad")
        file = None
        textarea.delete(1.0, END)

    def openfile():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            textarea.delete(1.0, END)
            try:
                with open(file, "r") as f:
                    textarea.insert(1.0, f.read())
            except Exception as e:
                tmsg.showerror("Error", f"Failed to open file: {e}")

    def savefile():
        global file
        if file is None:
            file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file == "":
                file = None
            if file is not None:
                try:
                    with open(file, "w") as f:
                        f.write(textarea.get(1.0, END))
                    root.title(os.path.basename(file) + " - Notepad")
                    print("File saved")
                except Exception as e:
                    tmsg.showerror("Error", f"Failed to save file: {e}")
        else:
            try:
                with open(file, "w") as f:
                    f.write(textarea.get(1.0, END))
                root.title(os.path.basename(file) + " - Notepad")
                print("File saved")
            except Exception as e:
                tmsg.showerror("Error", f"Failed to save file: {e}")

    def quitfile():
        root.quit()

    def cutfile():
        textarea.event_generate("<<Cut>>")

    def copyfile():
        textarea.event_generate("<<Copy>>")

    def pastefile():
        textarea.event_generate("<<Paste>>")

    def about():
        tmsg.showinfo("Notepad", "This Notepad is created by Navin Kumar Singh")

    global root
    root = Tk()
    root.geometry("665x435")
    root.title("Notepad by Navin")
    root.wm_iconbitmap("notepad.ico")

    textarea = Text(root, font="Arial 12", bg="#EEF7FF")
    file = None
    textarea.pack(expand=True, fill=BOTH)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0, bg="#EEF7FF")
    filemenu.add_command(label="New", command=newfile)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitfile)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0, bg="#EEF7FF")
    editmenu.add_command(label="Cut", command=cutfile)
    editmenu.add_command(label="Copy", command=copyfile)
    editmenu.add_command(label="Paste", command=pastefile)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0, bg="#EEF7FF")
    helpmenu.add_command(label="About Us", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    scroll = Scrollbar(textarea)
    scroll.pack(fill=Y, side=RIGHT)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    root.config(menu=menubar)

    root.mainloop()

    content = "Notepad is end sir"
    output(content)
