import tkinter as tk
from tkinter import filedialog
import os

class MainApp(tk.Frame):
    def __init__(self, master):
        '''Main Application'''
        tk.Frame.__init__(self, master)
        self.master = master
        self.fileName = tk.Label(self, text="Hello World", font=("Times New Roman", 30, "italic"), padx=10, pady=10)
        self.fileName.pack()
        self.openFileButton = tk.Button(self, text="Select File to Display Text File Name", command=self.file_select, font=("Arial", 16), padx=10, pady=10, background="white", border=5)
        self.openFileButton.pack()

    def file_select(self):
        '''Function to Open and Display Text File Name'''
        filetypes= (("Text files","*.txt")
                ,("All files","*.*"))
        self.openFileDialog = filedialog.askopenfilename(title='Select File', filetypes=filetypes)

        # Using os to split file path to get file name
        fileName = os.path.split(self.openFileDialog)

        if fileName != ('',''): 
            # Change the Label to Selected File Name
            self.fileName.config(text=fileName[1])


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Post Lab Question 2")
    MainApp(root).pack()
    root.mainloop()
