import tkinter as tk
from tkinter import ttk, messagebox
import logic
import storage

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x500")
        
        
        self.use_letters = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=False)
        
        self.create_widgets()
        self.update_history_view()

    def create_widgets(self):
        
        tk.Label(self.root, text="Длина пароля:", font=("Arial", 10, "bold")).pack(pady=5)
        self.length_slider = tk.Scale(self.root, from_=4, to=64, orient="horizontal", length=300)
        self.length_slider.set(12)
        self.length_slider.pack()

        
        frame_cb = tk.Frame(self.root)
        frame_cb.pack(pady=10)
        tk.Checkbutton(frame_cb, text="Буквы", variable=self.use_letters).grid(row=0, column=0)
        tk.Checkbutton(frame_cb, text="Цифры", variable=self.use_numbers).grid(row=0, column=1)
        tk.Checkbutton(frame_cb, text="Символы", variable=self.use_symbols).grid(row=0, column=2)

        
        tk.Button(self.root, text="СГЕНЕРИРОВАТЬ", bg="#4CAF50", fg="white", 
                  command=self.generate, font=("Arial", 10, "bold"), height=2).pack(pady=10, fill="x", padx=40)

        
        self.result_entry = tk.Entry(self.root, font=("Courier", 14), justify="center")
        self.result_entry.pack(pady=5, padx=20, fill="x")

        
        tk.Label(self.root, text="История последних паролей:").pack(pady=(10, 0))
        self.tree = ttk.Treeview(self.root, columns=("pass"), show="headings", height=8)
        self.tree.heading("pass", text="Пароль")
        self.tree.pack(pady=5, padx=20, fill="both")

    def generate(self):
        length = self.length_slider.get()
        try:
            pwd = logic.generate_password(
                length, 
                self.use_letters.get(), 
                self.use_numbers.get(), 
                self.use_symbols.get()
            )
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, pwd)
            
            storage.save_to_history(pwd)
            self.update_history_view()
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def update_history_view(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for pwd in reversed(storage.load_history()):
            self.tree.insert("", "end", values=(pwd,))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()