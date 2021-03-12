import tkinter as tk
#basic configuration
app = tk.Tk()
app.title("Calculator")
app.configure(bg="#010207")


e = tk.Entry(app,width=30,bg="#3f7a3d",fg="#1e180c")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#function configuration

def button_show(num):
	current = e.get()
	e.delete(0,'end')
	
	e.insert(0,str(current)+str(num))

def button_plus():
	first_num = e.get()

	global fnumber
	fnumber = int(first_num)
	e.delete(0,'end')

def button_equal():
	
	second_num = e.get()
	result = int(fnumber+int(second_num))
	e.delete(0,'end')
	e.insert(0,result)


def button_clear():
	e.delete(0,'end')

#button configuration

button_1 = tk.Button(app,text="1",padx=40,pady=20,command=lambda: button_show(1),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_2 = tk.Button(app,text="2",padx=40,pady=20,command=lambda: button_show(2),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_3 = tk.Button(app,text="3",padx=40,pady=20,command=lambda: button_show(3),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_4 = tk.Button(app,text="4",padx=40,pady=20,command=lambda: button_show(4),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_5 = tk.Button(app,text="5",padx=40,pady=20,command=lambda: button_show(5),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_6 = tk.Button(app,text="6",padx=40,pady=20,command=lambda: button_show(6),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_7 = tk.Button(app,text="7",padx=40,pady=20,command=lambda: button_show(7),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_8 = tk.Button(app,text="8",padx=40,pady=20,command=lambda: button_show(8),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_9 = tk.Button(app,text="9",padx=40,pady=20,command=lambda: button_show(9),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_0 = tk.Button(app,text="0",padx=40,pady=20,command=lambda: button_show(0),bg="#010207",fg="white",activebackground="#040635",activeforeground="white")

button_plus = tk.Button(app,text="+",padx=39,pady=20,command=button_plus,bg="#010207",fg="white",activebackground="#040635",activeforeground="white")
button_equal = tk.Button(app,text="=",padx=40,pady=20,command=button_equal,bg="#24b59a",fg="white",activebackground="#24b59a",activeforeground="white")
button_clear = tk.Button(app,text="Clear",padx=30,pady=20,command=button_clear,bg="#010207",fg="white",activebackground="#040635",activeforeground="white")

#buttons set

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_plus.grid(row=4,column=1)
button_equal.grid(row=5,column=1)
button_clear.grid(row=4,column=2)

app.mainloop()