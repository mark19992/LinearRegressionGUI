import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lr
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
import pandas as pd
fileDirectory = ""





window = tk.Tk()
window.resizable(False, False)
window.title('Linear Regression')
window.geometry("1000x600")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=1)


top_section = tk.Frame(window, bg="lightgray")
top_section.grid(row=0, column=0, sticky="ew")

bottom_section = tk.Frame(window, bg="lightblue")
bottom_section.grid(row=1, column=0, sticky="nsew")




def open_directory():
    fileDirectory = fd.askopenfilename(filetypes=(("csv files","*.csv"), ("All files", "*.*")))
    
    fig, ax = plt.subplots()
    file = pd.read_csv(fileDirectory)
    xName = file.columns.values[0]
    yName = file.columns.values[1]
    print(xName, " ", yName)
    x = file[xName]
    y = file[yName]
    regress = lr()
    regress.fit(x.values.reshape(-1, 1),y.values.reshape(-1,1))
    yPred = regress.predict(x.values.reshape(-1, 1))
    ax.scatter(x, yPred)
    ax.scatter(x, y, color = "#00ff00")
    ax.set_xlabel(xName)
    ax.set_ylabel(yName)
    ax.plot(x, yPred, color = "#ff00ff")
    for widget in top_section.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master = top_section)
    can_widget = canvas.get_tk_widget()
    can_widget.pack()
    



openFile = tk.Button(bottom_section, text ="OPEN", command=open_directory)



openFile.pack()


window.mainloop()



