from tkinter import *

dimension = 3

def plusDim():
    global dimension 
    if (dimension < 9): dimension += 2
    custom_kernel.config(text = "Size: " + str(dimension))
    createForms()

def minusDim():
    global dimension
    if (dimension > 3): dimension -= 2
    custom_kernel.config(text = "Size: " + str(dimension))
    createForms()

def createForms():
    # Clear forms
    for form in entry_frame.winfo_children():
        form.destroy()

    for i in range(dimension):
        for j in range(dimension):
            f=Entry(entry_frame,width=3)
            f.grid(row=i,column=j)

win = Tk()
win.title("Kernel Visualizer")
win.geometry('1600x900')
win.configure(background = "grey")

custom_kernel_frame = Frame()
entry_frame = Frame()

size_m_b = Button(custom_kernel_frame,
                  text = "-",
                  height = 1,
                  width = 3,
                  command = minusDim)

size_p_b = Button(custom_kernel_frame,
                  text = "+",
                  height = 1,
                  width = 3,
                  command = plusDim)


algoSelec = StringVar()
algoSelec.set("Select Algorithm")
drop = OptionMenu(win, algoSelec,   "Sobel Edge Detector",
                                    "Prewitt Edge Detector",
                                    "Roberts Edge Detector",
                                    "Laplacian Filter",
                                    "Custom")

custom_kernel = Label(custom_kernel_frame, text = "Size: " + str(dimension))


drop.pack()

custom_kernel_frame.pack()
size_m_b.grid(row=1,column=1)
size_p_b.grid(row=1,column=2)
custom_kernel.grid(row=2, column=1)
entry_frame.pack()


createForms()

win.mainloop()

print(dimension)