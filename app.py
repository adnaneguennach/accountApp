from tkinter import *
import tkinter as tk
import re
from tkinter import messagebox, simpledialog
from tkinter import ttk
import csv

testvar = 1


class Compte:
    nb = 0

    def __init__(self, proprietaire, solde):
        self.__proprietaire = proprietaire
        self.__solde = solde
        Compte.nb += 0
        self.__num = Compte.nb

    def get_num(self):
        return self.__num

class std(): 
    def __init__(self, master):
        self.master = master
        self.stock_name_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        self.quantity_varrr = StringVar()
        self.compte = Compte("Proprietaire", 0)
        self.master.geometry('1800x960')
        self.master.state('zoomed')
        self.master.title("GUI TP36 ")
        self.label1 = Label(text='Numéro : ')
        self.label1.grid(column=0, row=0, padx=10, pady=5)
        self.input1 = Entry(master, fg='blue')  
        self.input1.grid(row=0, column=1, padx=10, pady=5)
        self.input1.insert(END, self.compte.get_num())
        self.input1.config(state='disabled')      
        self.label2 = Label(text='Propriétaire :')
        self.label2.grid(row=1, column=0, padx=10, pady=5)
        self.inputprop = Entry(master, textvariable=self.stock_name_var)
        self.inputprop.grid(row=1, column=1, padx=10, pady=5)
        self.label3 = Label(text='Solde initial :')
        self.label3.grid(row=2, column=0, padx=10, pady=5)
        self.labeleuro = Label(text='Euro')
        self.labeleuro.grid(row=2, column=2, padx=10, pady=5)
        self.input_solde_int = Entry(master, textvariable=self.price_var)
        self.input_solde_int.grid(row=2, column=1, padx=10, pady=5)
        self.label4 = Label(text='Type :')
        self.label4.grid(row=3, column=0, padx=0, pady=5)
        self.selected_option = tk.StringVar()
        self.selected_option.set("Courant")
        self.selected_option2 = tk.StringVar()
        self.selected_option2.set("Epargne")
        self.radiobtn1 = Radiobutton(master, text="Courant", value="Courant", variable= self.selected_option, command=self.disable_func_courant)
        self.radiobtn1.grid(row=3, column=1)
        self.radiobtn2 = Radiobutton(master, text="Epargne", value="Epargne",variable= self.selected_option,  command=self.disable_func_epargne )
        self.radiobtn2.grid(row=4, column=1)
        self.label5 = Label(text='Taux interêt :')
        self.label5.grid(row=5, column=0, padx=10, pady=5)
        self.input_taux = Entry(master, state='disabled', textvariable=self.quantity_var)
        self.input_taux.grid(row=5, column=1, padx=10, pady=5)
        self.label5 = Label(text='%')
        self.label5.grid(row=5, column=2, padx=10, pady=5)
        self.label6 = Label(text='M.Découvert :')
        self.label6.grid(row=6, column=0, padx=10, pady=5)
        self.input_decouvert = Entry(master, textvariable=self.quantity_varrr )
        self.input_decouvert.grid(row=6, column=1, padx=10, pady=5)
        self.my_btn1 = Button(master, text='Création de compte', command=self.print_cm)
        self.my_btn1.grid(row=7, column=1, padx=10, pady=5)
        self.stock_data = []
        self.tree = ttk.Treeview(master, columns=("acc_num", "num", "proprietaire", "solde_intial", "type","taux", "m_decouvert"), show="headings")
        self.tree.heading("acc_num", text="#")
        self.tree.heading("num", text="Numéro")
        self.tree.heading("proprietaire", text="Propriétaire")
        self.tree.heading("solde_intial", text="Solde initial")
        self.tree.heading("type", text="Type")
        self.tree.heading("taux", text="Taux intérêt")
        self.tree.heading("m_decouvert", text="Montant Découvert")
        self.update_treeview()
        self.tree.grid(row=8, column=3, pady=0)
        self.btn_import = Button(master, text='Import', command=self.import_csv)
        self.btn_import.grid(row=6, column=3, padx=10, pady=5)
        self.btn_export = Button(master, text='Export', command=self.export_csv)
        self.btn_export.grid(row=7, column=3, padx=10, pady=5)

    
    def print_cm(self):
        pattern = re.compile(r'[a-z]+[A-Z]+')
        pattern2 = re.compile(r'[0-9]+')     

        stock_name = str(self.stock_name_var.get())
        input1 = str(self.input_decouvert.get())
        input2 = str(self.price_var.get())
        input3 = str(self.quantity_var.get())
        input4 = str(self.quantity_varrr.get())
        boolvar = 1
 
        if testvar == 1:
                if  pattern.match(input1):
                    messagebox.showerror("Error", "Le contenu n'est pas correct")
                    boolvar = 0

                elif pattern2.match(stock_name) : 
                    messagebox.showerror("Error", "Le contenu n'est pas correct")
                    boolvar = 0

                elif not pattern2.match(input2) and not pattern2.match(input3):
                    messagebox.showerror("Error", "Le contenu n'est pas correct")
                    boolvar = 0

                elif not pattern2.match(input4) and not pattern.match(stock_name) :
                    messagebox.showerror("Error", "Le contenu n'est pas correct")
                    boolvar = 0

                if stock_name == ''  and input1 == '' :
                    messagebox.showerror("Error", "Fields are empty.")
                    boolvar = 0

        else: 
                if not pattern2.match(input2):
                    messagebox.showerror("Error", "Le contenu n'est pas correct")
                    boolvar = 0

                elif pattern2.match(stock_name) : 
                    messagebox.showerror("Error", "Le contenu n'est pas correct")
                    boolvar = 0

                elif not pattern2.match(input4) and not pattern2.match(input3):
                    messagebox.showerror("Error", "Le contenu n'est pas correct")
                    boolvar = 0

        if boolvar == 1:
                Compte.nb += 1
                # self.input_solde_int.get()
                self.input1.config(state='normal')
                self.input1.delete(0, END)
                self.input1.insert(END, Compte.nb) 
                self.input1.config(state='disabled')
                stock_name = '', Compte.nb,  self.stock_name_var.get(), self.price_var.get(), self.selected_option.get(), self.quantity_var.get(), self.quantity_varrr.get()    
                new_stock = (stock_name)
                self.stock_data.append(new_stock)
                self.update_treeview()
                messagebox.showinfo("Success", "The account was created by success")

        elif boolvar == 0 : 
                messagebox.showerror("Error", "The account was not created")

    def disable_func_courant(self):
        self.input_decouvert.config(state='normal')
        self.input_taux.delete(0, END)
        self.input_taux.config(state='disabled')
        global testvar 
        testvar = 1
                                     
    def disable_func_epargne(self):
        self.input_decouvert.delete(0, END)
        self.input_decouvert.config(state='disabled')
        self.input_taux.config(state='normal')
        global testvar 
        testvar = 0

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)    
        for stock in self.stock_data:
            self.tree.insert("", "end", values=stock)

           
    def import_csv(self):
        patterncsv = r'^\w+\.csv$'
        answer = simpledialog.askstring("Input", "Write your file name .csv",
                                        parent=self.master)

        if answer is not None and re.match(patterncsv, answer):
            try:
                with open(answer, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    self.stock_data = list(reader)
                    self.update_treeview()
                    messagebox.showinfo("Success", "Data imported successfully from the CSV file.")
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Write the proper name for the file (file.csv)")

    def export_csv(self):
        filecsv = simpledialog.askstring(title='export', prompt='please enter the full name of the file(name.csv)')

        if filecsv is not None and re.match(r'^\w+\.csv$', filecsv):
            try:
                with open(filecsv, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(self.stock_data)
                messagebox.showinfo("Success", "Data exported successfully to the CSV file.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showerror("Error", "Write the proper name for the file (file.csv)")
             


if __name__ == '__main__':

    master = tk.Tk()
    op = std(master)
    master.mainloop()