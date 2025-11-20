import tkinter as tk
from tkinter import messagebox

class ModularCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Arithmetic Calculator")
        self.root.geometry("600x700")
        self.root.configure(bg='#f0f4f8')
        
        main_frame = tk.Frame(root, bg='#f0f4f8', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        title_label = tk.Label(
            main_frame,
            text="Modular Arithmetic Calculator",
            font=('Arial', 20, 'bold'),
            bg='#f0f4f8',
            fg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        modulus_frame = tk.LabelFrame(
            main_frame,
            text="Modulus",
            font=('Arial', 12, 'bold'),
            bg='#e8f4f8',
            fg='#34495e',
            padx=10,
            pady=10
        )
        modulus_frame.pack(fill='x', pady=(0, 15))
        
        tk.Label(
            modulus_frame,
            text="m =",
            font=('Arial', 12),
            bg='#e8f4f8'
        ).pack(side='left', padx=(0, 10))
        
        self.modulus_entry = tk.Entry(
            modulus_frame,
            font=('Arial', 14),
            width=10,
            justify='center'
        )
        self.modulus_entry.pack(side='left', fill='x', expand=True)
        self.modulus_entry.insert(0, "7")
        
        input_frame = tk.LabelFrame(
            main_frame,
            text="Input Values",
            font=('Arial', 12, 'bold'),
            bg='#fef5e7',
            fg='#34495e',
            padx=10,
            pady=10
        )
        input_frame.pack(fill='x', pady=(0, 15))
        
        a_frame = tk.Frame(input_frame, bg='#fef5e7')
        a_frame.pack(fill='x', pady=5)
        
        tk.Label(
            a_frame,
            text="a =",
            font=('Arial', 12),
            bg='#fef5e7',
            width=5
        ).pack(side='left')
        
        self.a_entry = tk.Entry(
            a_frame,
            font=('Arial', 14),
            justify='center'
        )
        self.a_entry.pack(side='left', fill='x', expand=True)
        
        b_frame = tk.Frame(input_frame, bg='#fef5e7')
        b_frame.pack(fill='x', pady=5)
        
        tk.Label(
            b_frame,
            text="b =",
            font=('Arial', 12),
            bg='#fef5e7',
            width=5
        ).pack(side='left')
        
        self.b_entry = tk.Entry(
            b_frame,
            font=('Arial', 14),
            justify='center'
        )
        self.b_entry.pack(side='left', fill='x', expand=True)
        
        operations_frame = tk.LabelFrame(
            main_frame,
            text="Operations",
            font=('Arial', 12, 'bold'),
            bg='#e8f8f5',
            fg='#34495e',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill='x', pady=(0, 15))
        
        button_configs = [
            ("a + b", self.add, '#27ae60', 0, 0),
            ("a - b", self.subtract, '#f39c12', 0, 1),
            ("-a", self.negate, '#e67e22', 0, 2),
            ("Clear", self.clear, '#e74c3c', 0, 3),
            ("a × b", self.multiply, '#3498db', 1, 0),
            ("a ÷ b", self.divide, '#9b59b6', 1, 1),
            ("a⁻¹", self.inverse, '#e91e63', 1, 2),
            ("a^b", self.power, '#8e44ad', 1, 3)
        ]
        
        for text, command, color, row, col in button_configs:
            btn = tk.Button(
                operations_frame,
                text=text,
                command=command,
                font=('Arial', 11, 'bold'),
                bg=color,
                fg='white',
                width=10,
                height=2,
                relief='raised',
                bd=3,
                cursor='hand2'
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        for i in range(4):
            operations_frame.columnconfigure(i, weight=1)
        
        result_frame = tk.LabelFrame(
            main_frame,
            text="Result",
            font=('Arial', 12, 'bold'),
            bg='#e8f5e9',
            fg='#34495e',
            padx=10,
            pady=10
        )
        result_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        self.result_text = tk.Text(
            result_frame,
            font=('Courier New', 12),
            height=8,
            wrap='word',
            bg='#ffffff',
            relief='sunken',
            bd=2
        )
        self.result_text.pack(fill='both', expand=True)
        
        dev_label = tk.Label(
            main_frame,
            text="Developed by: Demchuk Oksana (Ba-121-22-4-Se)",
            font=('Arial', 10),
            bg='#f0f4f8',
            fg='#7f8c8d'
        )
        dev_label.pack()
    
    def get_values(self):
        try:
            m = int(self.modulus_entry.get())
            if m <= 0:
                raise ValueError("Modulus must be positive")
            return m, None, None
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid modulus: {e}")
            return None, None, None
    
    def get_a(self):
        try:
            return int(self.a_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid value for a")
            return None
    
    def get_b(self):
        try:
            return int(self.b_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid value for b")
            return None
    
    def mod(self, n, m):
        result = n % m
        return result if result >= 0 else result + m
    
    def display_result(self, text):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, text)
    
    def add(self):
        m, _, _ = self.get_values()
        a = self.get_a()
        b = self.get_b()
        
        if m is None or a is None or b is None:
            return
        
        result = self.mod(a + b, m)
        output = f"Operation: a + b mod m\n\n"
        output += f"a = {a}\n"
        output += f"b = {b}\n"
        output += f"m = {m}\n\n"
        output += f"Calculation:\n"
        output += f"{a} + {b} = {a + b}\n"
        output += f"{a + b} mod {m} = {result}\n\n"
        output += f"Result: {result}"
        
        self.display_result(output)
    
    def subtract(self):
        m, _, _ = self.get_values()
        a = self.get_a()
        b = self.get_b()
        
        if m is None or a is None or b is None:
            return
        
        result = self.mod(a - b, m)
        output = f"Operation: a - b mod m\n\n"
        output += f"a = {a}\n"
        output += f"b = {b}\n"
        output += f"m = {m}\n\n"
        output += f"Calculation:\n"
        output += f"{a} - {b} = {a - b}\n"
        output += f"{a - b} mod {m} = {result}\n\n"
        output += f"Result: {result}"
        
        self.display_result(output)
    
    def negate(self):
        m, _, _ = self.get_values()
        a = self.get_a()
        
        if m is None or a is None:
            return
        
        result = self.mod(-a, m)
        output = f"Operation: -a mod m (Additive Inverse)\n\n"
        output += f"a = {a}\n"
        output += f"m = {m}\n\n"
        output += f"Calculation:\n"
        output += f"-{a} mod {m} = {result}\n\n"
        output += f"Verification:\n"
        output += f"{a} + {result} = {a + result}\n"
        output += f"{a + result} mod {m} = {self.mod(a + result, m)}\n\n"
        output += f"Result: {result}"
        
        self.display_result(output)
    
    def multiply(self):
        m, _, _ = self.get_values()
        a = self.get_a()
        b = self.get_b()
        
        if m is None or a is None or b is None:
            return
        
        result = self.mod(a * b, m)
        output = f"Operation: a × b mod m\n\n"
        output += f"a = {a}\n"
        output += f"b = {b}\n"
        output += f"m = {m}\n\n"
        output += f"Calculation:\n"
        output += f"{a} × {b} = {a * b}\n"
        output += f"{a * b} mod {m} = {result}\n\n"
        output += f"Result: {result}"
        
        self.display_result(output)
    
    def mod_inverse(self, a, m):
        a = self.mod(a, m)
        for x in range(1, m):
            if self.mod(a * x, m) == 1:
                return x
        return None
    
    def inverse(self):
        m, _, _ = self.get_values()
        a = self.get_a()
        
        if m is None or a is None:
            return
        
        inv = self.mod_inverse(a, m)
        
        if inv is None:
            output = f"Operation: a⁻¹ mod m (Multiplicative Inverse)\n\n"
            output += f"a = {a}\n"
            output += f"m = {m}\n\n"
            output += f"Result: NO INVERSE EXISTS\n\n"
            output += f"Reason: gcd({a}, {m}) ≠ 1"
        else:
            output = f"Operation: a⁻¹ mod m (Multiplicative Inverse)\n\n"
            output += f"a = {a}\n"
            output += f"m = {m}\n\n"
            output += f"Calculation:\n"
            output += f"Finding x where {a} × x ≡ 1 (mod {m})\n\n"
            output += f"Verification:\n"
            output += f"{a} × {inv} = {a * inv}\n"
            output += f"{a * inv} mod {m} = {self.mod(a * inv, m)}\n\n"
            output += f"Result: {inv}"
        
        self.display_result(output)
    
    def divide(self):
        m, _, _ = self.get_values()
        a = self.get_a()
        b = self.get_b()
        
        if m is None or a is None or b is None:
            return
        
        b_inv = self.mod_inverse(b, m)
        
        if b_inv is None:
            output = f"Operation: a ÷ b mod m\n\n"
            output += f"a = {a}\n"
            output += f"b = {b}\n"
            output += f"m = {m}\n\n"
            output += f"Result: DIVISION IMPOSSIBLE\n\n"
            output += f"Reason: {b} has no inverse mod {m}"
        else:
            result = self.mod(a * b_inv, m)
            output = f"Operation: a ÷ b mod m\n\n"
            output += f"a = {a}\n"
            output += f"b = {b}\n"
            output += f"m = {m}\n\n"
            output += f"Calculation:\n"
            output += f"First find b⁻¹: {b}⁻¹ mod {m} = {b_inv}\n"
            output += f"Then: {a} × {b_inv} = {a * b_inv}\n"
            output += f"{a * b_inv} mod {m} = {result}\n\n"
            output += f"Verification:\n"
            output += f"{result} × {b} = {result * b}\n"
            output += f"{result * b} mod {m} = {self.mod(result * b, m)}\n\n"
            output += f"Result: {result}"
        
        self.display_result(output)
    
    def mod_power(self, base, exp, m):
        result = 1
        base = self.mod(base, m)
        
        for i in range(exp):
            result = self.mod(result * base, m)
        
        return result
    
    def power(self):
        m, _, _ = self.get_values()
        a = self.get_a()
        b = self.get_b()
        
        if m is None or a is None or b is None:
            return
        
        if b < 0:
            messagebox.showerror("Error", "Exponent must be non-negative")
            return
        
        result = self.mod_power(a, b, m)
        
        output = f"Operation: a^b mod m\n\n"
        output += f"a = {a}\n"
        output += f"b = {b}\n"
        output += f"m = {m}\n\n"
        output += f"Calculation (iterative method):\n"
        
        if b <= 10:
            temp = 1
            for i in range(1, b + 1):
                temp = self.mod(temp * a, m)
                output += f"Step {i}: result = {temp}\n"
        else:
            output += f"Computing {a}^{b} mod {m} iteratively...\n"
        
        output += f"\nResult: {result}"
        
        self.display_result(output)
    
    def clear(self):
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)


def main():
    root = tk.Tk()
    app = ModularCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()