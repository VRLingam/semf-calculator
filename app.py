import tkinter as tk
from tkinter import messagebox
import json
from semf import semf  

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binding Energy Calculator")
        self.geometry("400x200")
        
        self.label_author = tk.Label(self, text="SEMF Binding Energy Calculator", font=("Arial", 10, "bold"))
        self.label_author.pack()

        self.label_A = tk.Label(self, text="Atomic Mass Number (A):")
        self.label_A.pack()
        self.entry_A = tk.Entry(self)
        self.entry_A.pack()

        self.label_Z = tk.Label(self, text="Atomic Number (Z):")
        self.label_Z.pack()
        self.entry_Z = tk.Entry(self)
        self.entry_Z.pack()

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_binding_energy)
        self.calculate_button.pack(pady=15)
        
        self.label_author = tk.Label(self, text="Author: Vishaal Lingam", font=("Arial", 8))
        self.label_author.pack()
        self.label_author = tk.Label(self, text="Date: 14 March 2024", font=("Arial", 8))
        self.label_author.pack()

    def calculate_binding_energy(self):
        try:
            A = int(self.entry_A.get())
            Z = int(self.entry_Z.get())
            result = semf(A, Z)
            messagebox.showinfo("Binding Energy", f"The binding energy is {result:.8f} MeV")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for A and Z")

if __name__ == "__main__":
    app = App()
    app.mainloop()
