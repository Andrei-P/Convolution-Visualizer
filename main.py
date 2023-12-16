from tkinter import *
from tkinter import filedialog
import numpy as np
from conv_script import *

dimension = 3
file_name = ""

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
    for form in entry_frame.winfo_children():
        form.destroy()

    for i in range(dimension):
        for j in range(dimension):
            f=Entry(entry_frame,width=3)
            f.grid(row=i,column=j)

def uploadImage():
    global file_name
    file_name = filedialog.askopenfilename()

def start():
    if (algoSelec.get() == "Sobel Edge Detector"):
        kernel = np.array([[-1 -1j, 0 -2j, 1 -1j],
                           [-2 +0j, 0 -0j, 2 +0j],
                           [-1 +1j, 0 +2j, 1 +1j]])
        
    elif (algoSelec.get() == "Prewitt Edge Detector"):
        kernel = np.array([[-1 -1j, 0 -1j, 1 -1j],
                           [-1 +0j, 0 -0j, 1 +0j],
                           [-1 +1j, 0 +1j, 1 +1j]])
        
    elif (algoSelec.get() == "Roberts Edge Detector"):
        kernel = np.array([[1 +0j, 0 +1j],
                           [0 -1j, -1 +0j],])
        
    elif (algoSelec.get() == "Laplacian Filter"):
        kernel = np.array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]])
        
    elif (algoSelec.get() == "3x3 Average Smoothing"):
        kernel = np.array([[1/9, 1/9, 1/9],
                           [1/9, 1/9, 1/9],
                           [1/9, 1/9, 1/9]])
        
    elif (algoSelec.get() == "5x5 Average Smoothing"):
        kernel = np.array([[1/25, 1/25, 1/25, 1/25, 1/25],
                           [1/25, 1/25, 1/25, 1/25, 1/25],
                           [1/25, 1/25, 1/25, 1/25, 1/25],
                           [1/25, 1/25, 1/25, 1/25, 1/25],
                           [1/25, 1/25, 1/25, 1/25, 1/25]])
        
    elif (algoSelec.get() == "9x9 Average Smoothing"):
        kernel = np.array([[1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81],
                           [1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81, 1/81]])
        
    elif (algoSelec.get() == "Custom"):
        kernel = []
        global dimension

        forms = list(entry_frame.children.values())

        for i in range(dimension):
            kernel.append([])
            for j in range(dimension):
                kernel[i].append(float(forms[j+(i*dimension)].get()))
    
    else:
        print("Please select an algorithm.")
        return
    
    global file_name
    if (file_name == ""):
        print("Please upload an image.")
        return
    
    convolve(file_name,kernel)

win = Tk()
win.title("Kernel Visualizer")
win.geometry('500x500')
win.configure(background = "grey")

custom_kernel_frame = Frame()
entry_frame = Frame()
 
upload_button=Button(win,
                     text = "Upload Image",
                     command = uploadImage)

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

start_button = Button(win,
                      text = "Start Visualizer",
                      command = start)

algoSelec = StringVar()
algoSelec.set("Select Algorithm")
drop = OptionMenu(win, algoSelec,   "Sobel Edge Detector",
                                    "Prewitt Edge Detector",
                                    "Roberts Edge Detector",
                                    "Laplacian Filter",
                                    "3x3 Average Smoothing",
                                    "5x5 Average Smoothing",
                                    "9x9 Average Smoothing",
                                    "Custom")

custom_kernel = Label(custom_kernel_frame, text = "Size: " + str(dimension))


drop.pack()
upload_button.pack()
start_button.pack()

custom_kernel_frame.pack()
size_m_b.grid(row=1,column=1)
size_p_b.grid(row=1,column=2)
custom_kernel.grid(row=2, column=1)
entry_frame.pack()


createForms()

win.mainloop()

print(dimension)