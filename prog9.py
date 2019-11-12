from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        Label(self, text="Choose Language :").grid(row = 0, column = 0, sticky = W)
        self.radVar = StringVar()
        self.radVar.set(None)
        self.radEng = Radiobutton(self, text = "English", variable = self.radVar, value = "English", command = self.radUpdate)
        self.radEng.grid(row = 1, column = 0, sticky = W)
        self.radHindi = Radiobutton(self, text = "Hindi", variable = self.radVar, value = "Hindi", command = self.radUpdate)
        self.radHindi.grid(row = 1, column = 1, sticky = W)
        self.checkVar1 = BooleanVar()
        Label(self, text="Choose Movie :").grid(row = 2, column = 0, sticky = W)
        self.check1 = Checkbutton(self, text = "Movie1", variable = self.checkVar1, command = self.checkUpdate)
        self.check1.grid(row = 3, column = 0, sticky = W)
        self.checkVar2 = BooleanVar()
        self.check2 = Checkbutton(self, text = "Movie2", variable = self.checkVar2, command = self.checkUpdate)
        self.check2.grid(row = 4, column = 0, sticky = W)
        self.checkVar3 = BooleanVar()
        self.check3 = Checkbutton(self, text = "Movie3", variable = self.checkVar3, command = self.checkUpdate)
        self.check3.grid(row = 5, column = 0, sticky = W)
        Label(self, text="Choose Number of tickets :").grid(row = 2, column = 3, sticky = W)
        self.dropVar = StringVar()
        self.dropVar.set(None)
        self.dropList = OptionMenu(self, self.dropVar, "1", "2", "3", "4", "5")
        self.dropList.grid(row = 3, column = 3, sticky = W)
        self.butt = Button(self, text = "Book Tickets", command = self.update)
        self.butt.grid(row = 6, column = 0, sticky = W)
        self.txt = Text(self, width = 20, height = 2, wrap = WORD)
        self.txt.grid(row = 6, column = 3, sticky = W)
        Button(self,text = "Clear", command = self.clear).grid(row = 7, column = 0, sticky = W)
    
    def clear(self):
        self.txt.delete(0.0, END)
        self.dropVar.set(None)
        self.checkVar1.set(False)
        self.checkVar2.set(False)
        self.checkVar3.set(False)
        self.radVar.set(None)
    
    def radUpdate(self):
        if self.radVar.get() == "English":
            self.check1["text"] = "Top Gun"
            self.check2["text"] = "Avengers"
            self.check3["text"] = "Terminator"
        if self.radVar.get() == "Hindi":
            self.check1["text"] = "D.D.L.J"
            self.check2["text"] = "Dangal"
            self.check3["text"] = "Dabang"
    
    def checkUpdate(self):
        pass
            
    def update(self):
   
        if self.checkVar1.get() == True or self.checkVar2.get() == True or self.checkVar3.get() == True:
            if self.dropVar.get() is not None:
                self.txt.delete(0.0, END)
                self.txt.insert(0.0, "Successful")
            else:
                self.txt.delete(0.0, END)
                self.txt.insert(0.0, "Unsuccessful")
        else:
            self.txt.delete(0.0, END)
            self.txt.insert(0.0, "Unsuccessful")
        

root = Tk()
root.geometry("600x500")
root.title("Movie Booking System")
app = Application(root)
root.mainloop()
