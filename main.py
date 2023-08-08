import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lr
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sklearn.ensemble import RandomForestRegressor as rfg
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from sklearn.svm import SVR
import seaborn as sns

class App:

    

    def __init__(self):
        self.width = 1000
        self.height = 600
        self.frame = tk.Tk()
        self.frame.resizable(False, False)
        self.frame.geometry(str(self.width) + "x" + str(self.height))
        self.frame.title("GUI Project")
        self.file = None
        self.frame.configure(bg="pink")
        self.initGUI()
        
       

        
    
    def getFilePath(self):
        self.filePathStr = fd.askopenfilename(filetypes=(("csv files","*.csv"), ("All files", "*.*")))
        self.filePathLabel.config(text=self.filePathStr)
        self.file = pd.read_csv(self.filePathStr)
        strVal = []
        for str in self.file.columns.values:
            strVal.append(str)
        
        self.varSelectorX["values"] = strVal
        self.varSelectorY["values"] = strVal
        self.varSelectorX.set("")
        self.varSelectorY.set("")
        

    def runLinearRegression(self):
        
        if(self.file is not None):
            if len(self.varSelectorX.get()) != 0 and len(self.varSelectorY.get()) != 0:
                
                x = self.file[self.varSelectorX.get()]
                y = self.file[self.varSelectorY.get()]
                fig, ax = plt.subplots()
                regress = lr()
                try:
                    regress.fit(x.values.reshape(-1, 1),y.values.reshape(-1,1))
                    yPred = regress.predict(x.values.reshape(-1, 1))
                    ax.scatter(x, yPred)
                    ax.scatter(x, y, color = "#00ff00")
                    ax.set_xlabel(self.varSelectorX.get())
                    ax.set_ylabel(self.varSelectorY.get())
                    ax.plot(x, yPred, color = "#ff00ff")
                    
                    canvas = FigureCanvasTkAgg(fig, master = self.frame)
                    
                    self.canvas_widget = canvas.get_tk_widget()
                    self.canvas_widget.place(x=180, y=0)
                except ValueError as ve:
                    messagebox.showerror("ERROR", "Please select numerical variables")

            else:
                messagebox.showerror("ERROR", "No selected variables")
        else:
            messagebox.showerror("ERROR", "No file selected")


    def runRandomForestRegression(self):
        
        if(self.file is not None):
            if len(self.varSelectorX.get()) != 0 and len(self.varSelectorY.get()) != 0:
                
                x = self.file[self.varSelectorX.get()]
                y = self.file[self.varSelectorY.get()]
                fig, ax = plt.subplots()
                regress = rfg()
                try:
                    regress.fit(x.values.reshape(-1, 1),y.values.reshape(-1,1))
                    yPred = regress.predict(x.values.reshape(-1, 1))
                    ax.scatter(x, yPred)
                    ax.scatter(x, y, color = "#00ff00")
                    ax.set_xlabel(self.varSelectorX.get())
                    ax.set_ylabel(self.varSelectorY.get())
                    ax.plot(x, yPred, color = "#ff00ff")
                    
                    canvas = FigureCanvasTkAgg(fig, master = self.frame)
                    
                    self.canvas_widget = canvas.get_tk_widget()
                    self.canvas_widget.place(x=180, y=0)
                except ValueError as ve:
                    messagebox.showerror("ERROR", "Please select numerical variables")

            else:
                messagebox.showerror("ERROR", "No selected variables")
        else:
            messagebox.showerror("ERROR", "No file selected")


    def runSVR(self):
        
        if(self.file is not None):
            if len(self.varSelectorX.get()) != 0 and len(self.varSelectorY.get()) != 0:
                
                x = self.file[self.varSelectorX.get()]
                y = self.file[self.varSelectorY.get()]
                fig, ax = plt.subplots()
                regress = SVR()
                try:
                    regress.fit(x.values.reshape(-1, 1),y.values.reshape(-1,1))
                    yPred = regress.predict(x.values.reshape(-1, 1))
                    ax.scatter(x, yPred)
                    ax.scatter(x, y, color = "#00ff00")
                    ax.set_xlabel(self.varSelectorX.get())
                    ax.set_ylabel(self.varSelectorY.get())
                    ax.plot(x, yPred, color = "#ff00ff")
                    
                    canvas = FigureCanvasTkAgg(fig, master = self.frame)
                    
                    self.canvas_widget = canvas.get_tk_widget()
                    self.canvas_widget.place(x=180, y=0)
                except ValueError as ve:
                    messagebox.showerror("ERROR", "Please select numerical variables")

            else:
                messagebox.showerror("ERROR", "No selected variables")
        else:
            messagebox.showerror("ERROR", "No file selected")

    def runLogisticRegression(self):
        
        if(self.file is not None):
            if len(self.varSelectorX.get()) != 0 and len(self.varSelectorY.get()) != 0:
                
                x = self.file[self.varSelectorX.get()]
                y = self.file[self.varSelectorY.get()]
                fig, ax = plt.subplots()
                regress = LogisticRegression()
                try:
                    regress.fit(x.values.reshape(-1, 1),y.values.reshape(-1,1))
                    yPred = regress.predict(x.values.reshape(-1, 1))
                    ax.scatter(x, yPred)
                    ax.scatter(x, y, color = "#00ff00")
                    ax.set_xlabel(self.varSelectorX.get())
                    ax.set_ylabel(self.varSelectorY.get())
                    ax.plot(x, yPred, color = "#ff00ff")
                    
                    canvas = FigureCanvasTkAgg(fig, master = self.frame)
                    
                    self.canvas_widget = canvas.get_tk_widget()
                    self.canvas_widget.place(x=180, y=0)
                except ValueError as ve:
                    messagebox.showerror("ERROR", "Please select numerical variables")

            else:
                messagebox.showerror("ERROR", "No selected variables")
        else:
            messagebox.showerror("ERROR", "No file selected")
    

    def runKMEANS(self):
        
        if(self.file is not None):
            if len(self.varSelectorX.get()) != 0 and len(self.varSelectorY.get()) != 0:
                

               
                x = self.varSelectorX.get()
                y = self.varSelectorY.get()
                
                fig, ax = plt.subplots()
                regress = KMeans(n_clusters=3)
                X = self.file.loc[:, [x, y]].values
                try:
                    yPred = regress.fit_predict(X)
                    ax.set_xlabel(self.varSelectorX.get())
                    ax.set_ylabel(self.varSelectorY.get())
                    ax.scatter(X[:, 0], X[:, 1], c=yPred)
                    ax.set_title("K-Means Clusters")
                    canvas = FigureCanvasTkAgg(fig, master = self.frame)
                    
                    self.canvas_widget = canvas.get_tk_widget()
                    self.canvas_widget.place(x=180, y=0)
                except ValueError as ve:
                    messagebox.showerror("ERROR", "Please select proper data type variables")

            else:
                messagebox.showerror("ERROR", "No selected variables")
        else:
            messagebox.showerror("ERROR", "No file selected")


    def runDecisionTreeClassifier(self):
        if(self.file is not None):
            if len(self.varSelectorX.get()) != 0 and len(self.varSelectorY.get()) != 0:
                
                x = self.file[self.varSelectorX.get()]
                y = self.file[self.varSelectorY.get()]
                fig, ax = plt.subplots()
                regress = DecisionTreeClassifier()
                try:
                    regress.fit(x.values.reshape(-1, 1),y.values.reshape(-1,1))
                    
                    X_encoded = pd.get_dummies(x, columns=y)
                    yPred = regress.predict(x.values.reshape(-1, 1))
                    
                    ax.set_xlabel(self.varSelectorX.get())
                    ax.set_ylabel(self.varSelectorY.get())
                    ax.set_title("Decision Tree Classifier")
                    tree.plot_tree(regress, feature_names=(X_encoded.columns), class_names=regress.classes_)
                    
                    canvas = FigureCanvasTkAgg(fig, master = self.frame)
                    
                    self.canvas_widget = canvas.get_tk_widget()
                    self.canvas_widget.place(x=180, y=0)
                except ValueError as ve:
                    messagebox.showerror("ERROR", ve)

            else:
                messagebox.showerror("ERROR", "No selected variables")
        else:
            messagebox.showerror("ERROR", "No file selected")
        

    def runNaiveBayesian(self):
        if(self.file is not None):
            if len(self.varSelectorX.get()) != 0 and len(self.varSelectorY.get()) != 0:
                
                x = self.file[self.varSelectorX.get()]
                y = self.file[self.varSelectorY.get()]
                fig, ax = plt.subplots()
                regress = DecisionTreeClassifier()
                try:
                    regress.fit(x.values.reshape(-1, 1),y.values.reshape(-1,1))
                    
                    X_encoded = pd.get_dummies(x, columns=y)
                    yPred = regress.predict(x.values.reshape(-1, 1))
                    
                    ax.set_xlabel(self.varSelectorX.get())
                    ax.set_ylabel(self.varSelectorY.get())
                    ax.set_title("Confusion Matrix")
                    cm = confusion_matrix(y.values.reshape(-1,1), yPred)
                    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d", xticklabels=regress.classes_, yticklabels=regress.classes_)
                    canvas = FigureCanvasTkAgg(fig, master = self.frame)
                    
                    self.canvas_widget = canvas.get_tk_widget()
                    self.canvas_widget.place(x=180, y=0)
                except ValueError as ve:
                    messagebox.showerror("ERROR", ve)

            else:
                messagebox.showerror("ERROR", "No selected variables")
        else:
            messagebox.showerror("ERROR", "No file selected")

    def initGUI(self):

        self.uploadButton = tk.Button(self.frame, text="OPEN", bg="#ff1010", fg = "white", command= self.getFilePath, font=("Times New Roman", 10, "bold"))
        self.uploadButton.place(x=20,y=self.height*0.80)
        self.uploadButton.update_idletasks()

        self.lrButton = tk.Button(self.frame, text="LINEAR REGRESSION", bg="#afafaf", command=self.runLinearRegression, font=("Times New Roman", 10, "bold"), fg = "red")
        self.lrButton.place(x=20,y=self.height*0.85)
        self.lrButton.update_idletasks()

        self.frButton = tk.Button(self.frame, text="RANDOM FORREST REG", bg="#afafaf", command=self.runRandomForestRegression, font=("Times New Roman", 10, "bold"), fg = "maroon")
        self.frButton.place(x=20,y=self.height*0.90)
        self.frButton.update_idletasks()

        self.srButton = tk.Button(self.frame, text="SUPPORT VECTOR REG", bg="#afafaf", command=self.runSVR, font=("Times New Roman", 10, "bold"), fg = "green")
        self.srButton.place(x=20,y=self.height*0.95)

        self.logRButton = tk.Button(self.frame, text="LOGISTIC REGRESSION", bg="#afafaf", command=self.runLogisticRegression, font=("Times New Roman", 10, "bold"), fg = "blue")
        self.logRButton.place(x=self.lrButton.winfo_width() + 25,y=self.height*0.85)
        self.logRButton.update_idletasks()

        self.kmeanButton = tk.Button(self.frame, text="KMEANS CLUSTERING", bg="#afafaf", command=self.runKMEANS, font=("Times New Roman", 10, "bold"), fg = "dark green")
        self.kmeanButton.place(x=self.frButton.winfo_width() + 25,y=self.height*0.90)
        
        self.treeButton = tk.Button(self.frame, text="TREE CLASSIFIER", bg="#afafaf", command=self.runDecisionTreeClassifier, font=("Times New Roman", 10, "bold"), fg ="dark blue")
        self.treeButton.place(x=self.frButton.winfo_width() + 25,y=self.height*0.95)

        self.naiveButton = tk.Button(self.frame, text="NAIVE BAYESIAN", bg="#afafaf", command=self.runNaiveBayesian, font=("Times New Roman", 10, "bold"), fg = "#f7ff17")
        self.naiveButton.place(x=self.logRButton.winfo_width()*2 + 20,y=self.height*0.85)

        self.filePathLabel = tk.Label(self.frame, text="C:/FilePath", bg="blue", fg="light blue", font=("Times New Roman", 10, "bold"))
        self.filePathLabel.place(x = self.uploadButton.winfo_x() + self.uploadButton.winfo_width()+5, y=self.uploadButton.winfo_y() + self.uploadButton.winfo_height()/8)


        creditsLabel = tk.Label(self.frame, text="Credits: Sam Juanite - 提古尔斯", bg="#2A0080", fg="light blue", font=("Times New Roman", 12, "bold"))
        creditsLabel.place(x=480, y=570)

        selectedXVar = ""
        self.varSelectorX = ttk.Combobox(self.frame, textvariable=selectedXVar)
        self.varSelectorX.place(x=self.width*0.85, y=self.height*0.80)
        self.varSelectorX.update_idletasks()
        xLabel = tk.Label(self.frame, text="X:", font=("Times New Roman", 10, "bold"), fg = "red")
        xLabel.place(x=self.varSelectorX.winfo_x() - 25,y=self.height*0.8)

        selectedYVar = ""
        self.varSelectorY = ttk.Combobox(self.frame, textvariable=selectedYVar)
        self.varSelectorY.place(x=self.width*0.85, y=self.height*0.85)
        self.varSelectorY.update_idletasks()
        yLabel = tk.Label(self.frame, text="Y:", font=("Times New Roman", 10, "bold"), fg = "blue")
        yLabel.place(x=self.varSelectorX.winfo_x() - 25,y=self.height*0.85)
    
    
    def runApp(self):
        self.frame.mainloop()



if __name__ == "__main__":
    myApp = App()
    myApp.runApp()


