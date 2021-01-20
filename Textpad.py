# Importing required modules
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser
import tkinter as tk
import win32print
import win32api
import os

# creating the basic things
root = Tk()
root.title('Texpad - By Nishanth')
root.iconbitmap('img/logo.ico')
root.geometry("1200x680")
root.resizable(False, False)

# Setting open file to none
global open_status_name
open_status_name = False

# Setting selected text to none
global selected
selected = False


# Functions
# Creating a new file
def new_file(event=""):
    my_text.delete("1.0", END)
    # Updating the status bar
    root.title('New file - Textpad')
    status_bar.config(text="New file")
    global open_status_name
    open_status_name = False


# Opening a file
def open_file(event=""):
    # Deleting the previous text
    my_text.delete("1.0", END)
    # Grabing the filename
    text_file = filedialog.askopenfilename(title="Open file", initialdir="G:/", filetypes=(
    ("Text file", "*.txt"), ("HTML file", "*.html"), ("CSS file", "*.css"), ("Javascript file", "*.js"),
    ("PHP file", "*.php"), ("Python file", "*.py")))
    if text_file:
        global open_status_name
        open_status_name = text_file
    if text_file:
        name_in_fullform = text_file
        name_in_list = os.path.split(name_in_fullform)
        name = name_in_list[-1]
        status_bar.config(text="%s" % name)
        root.title("%s" % name)
        # opening the file
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        # Adding file to text box
        my_text.insert(END, stuff)
        # Closing the file
        text_file.close()
        messagebox.showinfo("Textpad - By Nishanth", "The file was sucsesfully opened!")


# Saving the file as
def save_as_file(event=""):
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="G:/", title="Save file as", filetypes=(
    ("Text file", "*.txt"), ("HTML file", "*.html"), ("CSS file", "*.css"), ("Javascript file", "*.js"),
    ("PHP file", "*.php"), ("Python file", "*.py")))
    if text_file:
        global open_status_name
        open_status_name = text_file
        name_in_fullform = text_file
        name_in_list = os.path.split(name_in_fullform)
        name = name_in_list[-1]
        status_bar.config(text="Saved:%s" % name)
        root.title("%s" % name)
        messagebox.showinfo("Textpad - By Nishanth", "The file was sucsesfully saved!")
        # Saviing the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()


# Save the file
def save_file(event=""):
    global open_status_name
    if open_status_name:
        # Saviing the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        name_in_fullform = open_status_name
        name_in_list = os.path.split(name_in_fullform)
        name = name_in_list[-1]
        status_bar.config(text="Saved:%s" % name)
        messagebox.showinfo("Textpad - By Nishanth", "The file was successfully saved!")
    else:
        save_as_file()


# Closing app
def on_closing(event=""):
    if messagebox.askyesno("Textpad - By Nishanth", "Do you want to quit?"):
        root.quit()


# Cutting the text
def cut_text(event=""):
    global selected
    if event:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


# Copying the text
def copy_text(event=""):
    global selected
    if event:
        selected = root.clipboard_get()
    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


# Pasting the text
def paste_text(event=""):
    if event:
        selected = root.clipboard_get()
    else:
        if selected != 0:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


# Undo text
def undo_text(event=""):
    my_text.edit_undo()


# Redo text
def redo_text(event=""):
    my_text.edit_redo()


# Italic text
def italic_it(event=""):
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")
    my_text.tag_configure("italic", font=italic_font)
    current_tags = my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


# Bold text
def bold_it(event=""):
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    my_text.tag_configure("bold", font=bold_font)
    current_tags = my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


# Selecting the text color for all text
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.configure(fg=my_color)


# Background color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.configure(bg=my_color)


# Select all
def select_all():
    my_text.tag_add('sel', '1.0', 'end')


# Clear all
def clear_all(event=""):
    my_text.delete(1.0, END)
# Printing the file
def print_file(event=""):
    # printer_name = win32print.GetDefaultPrinter()
    # status_bar.config(text=printer_name)
    file_to_print = filedialog.askopenfilename(defaultextension=".*", initialdir="G:/", title="Print file", filetypes=(
    ("Text file", "*.txt"), ("HTML file", "*.html"), ("CSS file", "*.css"), ("Javascript file", "*.js"),
    ("PHP file", "*.php"), ("Python file", "*.py")))
    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, "None", ".",  0)
# About app
def about_app():
    messagebox.showinfo("About - Textpad", "Textpad is a text editor which can be used to write and edit text, python, javascript, css and html files. hey can later be printed into a pdf or can be directly printed")
# Version of the app
def version_app():
    messagebox.showinfo("Textpad - By Nishanth", "Version - 1.0.0 - By Nishanth")

# Closing app
root.protocol("WM_DELETE_WINDOW", on_closing)
# Creating the keyboard shortcuts
root.bind('<Control-n>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-Alt-s>', save_as_file)
root.bind('<Control-s>', save_file)
root.bind('<Alt-F4>', on_closing)   
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)
root.bind('<Control-z>', undo_text)
root.bind('<Control-y>', redo_text)
root.bind('<Control-p>', print_file)
root.bind('<Alt-b>', bold_it)
root.bind('<Alt-i>', italic_it)
root.bind('<Alt-a>', clear_all)

# Creating the toolbar
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X, pady=5)

# Creating the main frame
my_frame = Frame(root)
my_frame.pack()

# Creating the scrollbar for the textbox
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side="right", fill=Y)

# Horizontal scrollbar
text_scrollx = Scrollbar(my_frame, orient="horizonta")
text_scrollx.pack(side="bottom", fill=X)

# Creating the text widget
my_text = Text(my_frame, width=100, height=21, font=("Arial", 18), selectbackground="lightblue",
               selectforeground="black", undo=True, wrap="none", yscrollcommand=text_scroll.set,
               xscrollcommand=text_scrollx.set)
my_text.pack()

# Configuring the scrollbar
text_scroll.config(command=my_text.yview)
text_scrollx.config(command=my_text.xview)

# Creating the menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Creating file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As    ", command=save_as_file, accelerator="Ctrl+Alt+S")
file_menu.add_separator()
file_menu.add_command(label="Print File", accelerator="Ctrl+P", command="print_file")
file_menu.add_separator()
file_menu.add_command(label="Quit", command=on_closing, accelerator="Alt+F4")

# Creating the Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="paste", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo_text, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo       ", command=redo_text, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Select all", command=select_all, accelerator="Ctrl+A")
edit_menu.add_command(label="Clear all", command=clear_all, accelerator="Ctrl+Alt+A")

# Creating the color menu
font_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Italic", command=italic_it)
font_menu.add_command(label="Bold", command=bold_it)
font_menu.add_separator()
font_menu.add_command(label="Font colour", command=all_text_color)
font_menu.add_command(label="Background colour", command=bg_color)

# Creating about menu
about_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About", command=about_app, accelerator="    ")
about_menu.add_command(label="Version", command=version_app, accelerator="   ")

# Creating the buttons
bold_button = Button(toolbar_frame, text="Bold", bg="#f5f5f5", command=bold_it, padx=5, pady=3, bd=2, relief=tk.RIDGE,
                     borderwidt=2, activebackground="#fff", activeforeground="#000")
bold_button.grid(row=0, column=0, sticky=W, padx=5)
italic_button = Button(toolbar_frame, text="Italic", bg="#f5f5f5", command=italic_it, padx=5, pady=3, bd=2,
                       relief=tk.RIDGE, borderwidt=2, activebackground="#fff", activeforeground="#000")
italic_button.grid(row=0, column=1, padx=5)
all_text_color_button = Button(toolbar_frame, text="All text colour", bg="#f5f5f5", command=all_text_color, padx=5,
                               pady=3, bd=2, relief=tk.RIDGE, borderwidt=2, activebackground="#fff",
                               activeforeground="#000")
all_text_color_button.grid(row=0, column=2, padx=5)
bg_button = Button(toolbar_frame, text="Whole background colour", bg="#f5f5f5", command=bg_color, padx=5, pady=3, bd=2,
                   relief=tk.RIDGE, borderwidt=2, activebackground="#fff", activeforeground="#000")
bg_button.grid(row=0, column=3, padx=5)
undo_button = Button(toolbar_frame, text="Undo", bg="#f5f5f5", command=undo_text, padx=5, pady=3, bd=2, relief=tk.RIDGE,
                     borderwidt=2, activebackground="#fff", activeforeground="#000")
undo_button.grid(row=0, column=4, padx=5)
redo_button = Button(toolbar_frame, text="Redo", bg="#f5f5f5", command=redo_text, padx=5, pady=3, bd=2, relief=tk.RIDGE,
                     borderwidt=2, activebackground="#fff", activeforeground="#000")
redo_button.grid(row=0, column=5, padx=5)


# Adding the status bar
status_bar = Label(root, text="Ready", anchor=E, font="Arial 17", padx=12)
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
