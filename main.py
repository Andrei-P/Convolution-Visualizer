from tkinter import *

dimension = 3

def plusDim():
    global dimension 
    if (dimension < 8): dimension += 1
    custom_kernel.config(text = "Size: " + str(dimension))

def minusDim():
    global dimension
    if (dimension > 3): dimension -= 1
    custom_kernel.config(text = "Size: " + str(dimension))

win = Tk()
win.title("Kernel Visualizer")
win.geometry('1600x900')
win.configure(background = "grey")

custom_kernel_frame=Frame()

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

win.mainloop()

print(dimension)