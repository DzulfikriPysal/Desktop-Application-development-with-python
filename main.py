from tkinter import *
import pygubu


class Application:
	def __init__(self, master):
		root.title("Hello World") # title
		lbl = Label(root, text="hello", font=("Arial Bold", 14)) # insert text
		lbl.grid(column=0, row=0) # text location 
		
		txt = Entry(root, width=10)
		txt.grid(column=1, row=0)
		
		def clicked():
			res = "Welcome to" + txt.get()
			lbl.configure(text="text is:" + res)

	
		btn = Button(root, text="Click Me", bg="orange", fg="red", command=clicked)
		btn.grid(column=2, row=0)


if __name__ == '__main__':
	root = Tk()
	app = Application(root)
	root.geometry('350x200'); # windows size
	root.mainloop()
	