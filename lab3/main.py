import tkinter as tk
from tkinter import messagebox, ttk
import math

class ModularCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Arithmetic Calculator - Lab 3 Extended")
        self.root.geometry("700x800")
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
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(
            main_frame,
            text="Lab 3: Prime Numbers & Euler Function",
            font=('Arial', 12),
            bg='#f0f4f8',
            fg='#7f8c8d'
        )
        subtitle_label.pack(pady=(0, 15))
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True)
        
        # Tab 1: Basic Operations (from Lab 2)
        self.basic_tab = tk.Frame(self.notebook, bg='#f0f4f8')
        self.notebook.add(self.basic_tab, text='Basic Operations')
        self.create_basic_tab()
        
        # Tab 2: Prime Numbers
        self.prime_tab = tk.Frame(self.notebook, bg='#f0f4f8')
        self.notebook.add(self.prime_tab, text='Prime Numbers')
        self.create_prime_tab()
        
        # Tab 3: GCD (Euclidean Algorithm)
        self.gcd_tab = tk.Frame(self.notebook, bg='#f0f4f8')
        self.notebook.add(self.gcd_tab, text='GCD Algorithm')
        self.create_gcd_tab()
        
        # Tab 4: Euler Function
        self.euler_tab = tk.Frame(self.notebook, bg='#f0f4f8')
        self.notebook.add(self.euler_tab, text='Euler Function')
        self.create_euler_tab()
        
        # Tab 5: Modular Inverse
        self.inverse_tab = tk.Frame(self.notebook, bg='#f0f4f8')
        self.notebook.add(self.inverse_tab, text='Modular Inverse')
        self.create_inverse_tab()
        
        dev_label = tk.Label(
            main_frame,
            text="Developed by: Demchuk Oksana (Ba-121-22-4-Se)",
            font=('Arial', 10),
            bg='#f0f4f8',
            fg='#7f8c8d'
        )
        dev_label.pack(pady=(10, 0))
    
    def create_basic_tab(self):
        modulus_frame = tk.LabelFrame(
            self.basic_tab,
            text="Modulus",
            font=('Arial', 11, 'bold'),
            bg='#e8f4f8',
            fg='#34495e',
            padx=10,
            pady=10
        )
        modulus_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(modulus_frame, text="m =", font=('Arial', 11), bg='#e8f4f8').pack(side='left', padx=(0, 10))
        self.modulus_entry = tk.Entry(modulus_frame, font=('Arial', 12), width=10, justify='center')
        self.modulus_entry.pack(side='left', fill='x', expand=True)
        self.modulus_entry.insert(0, "7")
        
        input_frame = tk.LabelFrame(
            self.basic_tab,
            text="Input Values",
            font=('Arial', 11, 'bold'),
            bg='#fef5e7',
            fg='#34495e',
            padx=10,
            pady=10
        )
        input_frame.pack(fill='x', padx=10, pady=10)
        
        a_frame = tk.Frame(input_frame, bg='#fef5e7')
        a_frame.pack(fill='x', pady=5)
        tk.Label(a_frame, text="a =", font=('Arial', 11), bg='#fef5e7', width=5).pack(side='left')
        self.a_entry = tk.Entry(a_frame, font=('Arial', 12), justify='center')
        self.a_entry.pack(side='left', fill='x', expand=True)
        
        b_frame = tk.Frame(input_frame, bg='#fef5e7')
        b_frame.pack(fill='x', pady=5)
        tk.Label(b_frame, text="b =", font=('Arial', 11), bg='#fef5e7', width=5).pack(side='left')
        self.b_entry = tk.Entry(b_frame, font=('Arial', 12), justify='center')
        self.b_entry.pack(side='left', fill='x', expand=True)
        
        operations_frame = tk.LabelFrame(
            self.basic_tab,
            text="Operations",
            font=('Arial', 11, 'bold'),
            bg='#e8f8f5',
            fg='#34495e',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill='x', padx=10, pady=10)
        
        button_configs = [
            ("a + b", self.add, '#27ae60', 0, 0),
            ("a - b", self.subtract, '#f39c12', 0, 1),
            ("-a", self.negate, '#e67e22', 0, 2),
            ("Clear", self.clear_basic, '#e74c3c', 0, 3),
            ("a × b", self.multiply, '#3498db', 1, 0),
            ("a ÷ b", self.divide, '#9b59b6', 1, 1),
            ("a⁻¹", self.inverse_basic, '#e91e63', 1, 2),
            ("a^b", self.power, '#8e44ad', 1, 3)
        ]
        
        for text, command, color, row, col in button_configs:
            btn = tk.Button(
                operations_frame,
                text=text,
                command=command,
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=9,
                height=2,
                relief='raised',
                bd=3,
                cursor='hand2'
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
        
        for i in range(4):
            operations_frame.columnconfigure(i, weight=1)
        
        result_frame = tk.LabelFrame(
            self.basic_tab,
            text="Result",
            font=('Arial', 11, 'bold'),
            bg='#e8f5e9',
            fg='#34495e',
            padx=10,
            pady=10
        )
        result_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.result_text = tk.Text(
            result_frame,
            font=('Courier New', 10),
            height=10,
            wrap='word',
            bg='#ffffff',
            relief='sunken',
            bd=2
        )
        self.result_text.pack(fill='both', expand=True)
    
    def create_prime_tab(self):
        input_frame = tk.LabelFrame(
            self.prime_tab,
            text="Input",
            font=('Arial', 11, 'bold'),
            bg='#fef5e7',
            fg='#34495e',
            padx=10,
            pady=10
        )
        input_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(input_frame, text="Number:", font=('Arial', 11), bg='#fef5e7').pack(side='left', padx=(0, 10))
        self.prime_entry = tk.Entry(input_frame, font=('Arial', 12), width=15, justify='center')
        self.prime_entry.pack(side='left', fill='x', expand=True)
        
        operations_frame = tk.LabelFrame(
            self.prime_tab,
            text="Operations",
            font=('Arial', 11, 'bold'),
            bg='#e8f8f5',
            fg='#34495e',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Button(
            operations_frame,
            text="Check Primality (Fermat Test)",
            command=self.check_prime,
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        gen_frame = tk.Frame(operations_frame, bg='#e8f8f5')
        gen_frame.pack(fill='x', pady=5)
        
        tk.Label(gen_frame, text="Upper bound A:", font=('Arial', 10), bg='#e8f8f5').pack(side='left', padx=(0, 10))
        self.prime_bound_entry = tk.Entry(gen_frame, font=('Arial', 11), width=10, justify='center')
        self.prime_bound_entry.pack(side='left', padx=(0, 10))
        
        tk.Button(
            gen_frame,
            text="Generate Prime p ≤ A",
            command=self.generate_prime,
            font=('Arial', 10, 'bold'),
            bg='#27ae60',
            fg='white',
            cursor='hand2'
        ).pack(side='left', fill='x', expand=True)
        
        tk.Button(
            operations_frame,
            text="Clear",
            command=self.clear_prime,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        result_frame = tk.LabelFrame(
            self.prime_tab,
            text="Result",
            font=('Arial', 11, 'bold'),
            bg='#e8f5e9',
            fg='#34495e',
            padx=10,
            pady=10
        )
        result_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.prime_result = tk.Text(
            result_frame,
            font=('Courier New', 10),
            height=15,
            wrap='word',
            bg='#ffffff',
            relief='sunken',
            bd=2
        )
        self.prime_result.pack(fill='both', expand=True)
    
    def create_gcd_tab(self):
        input_frame = tk.LabelFrame(
            self.gcd_tab,
            text="Input Two Numbers",
            font=('Arial', 11, 'bold'),
            bg='#fef5e7',
            fg='#34495e',
            padx=10,
            pady=10
        )
        input_frame.pack(fill='x', padx=10, pady=10)
        
        a_frame = tk.Frame(input_frame, bg='#fef5e7')
        a_frame.pack(fill='x', pady=5)
        tk.Label(a_frame, text="a =", font=('Arial', 11), bg='#fef5e7', width=5).pack(side='left')
        self.gcd_a_entry = tk.Entry(a_frame, font=('Arial', 12), justify='center')
        self.gcd_a_entry.pack(side='left', fill='x', expand=True)
        
        b_frame = tk.Frame(input_frame, bg='#fef5e7')
        b_frame.pack(fill='x', pady=5)
        tk.Label(b_frame, text="b =", font=('Arial', 11), bg='#fef5e7', width=5).pack(side='left')
        self.gcd_b_entry = tk.Entry(b_frame, font=('Arial', 12), justify='center')
        self.gcd_b_entry.pack(side='left', fill='x', expand=True)
        
        operations_frame = tk.LabelFrame(
            self.gcd_tab,
            text="Operations",
            font=('Arial', 11, 'bold'),
            bg='#e8f8f5',
            fg='#34495e',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Button(
            operations_frame,
            text="Calculate GCD (Euclidean Algorithm)",
            command=self.calculate_gcd,
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        tk.Button(
            operations_frame,
            text="Clear",
            command=self.clear_gcd,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        result_frame = tk.LabelFrame(
            self.gcd_tab,
            text="Result",
            font=('Arial', 11, 'bold'),
            bg='#e8f5e9',
            fg='#34495e',
            padx=10,
            pady=10
        )
        result_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.gcd_result = tk.Text(
            result_frame,
            font=('Courier New', 10),
            height=15,
            wrap='word',
            bg='#ffffff',
            relief='sunken',
            bd=2
        )
        self.gcd_result.pack(fill='both', expand=True)
    
    def create_euler_tab(self):
        input_frame = tk.LabelFrame(
            self.euler_tab,
            text="Input",
            font=('Arial', 11, 'bold'),
            bg='#fef5e7',
            fg='#34495e',
            padx=10,
            pady=10
        )
        input_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(input_frame, text="n =", font=('Arial', 11), bg='#fef5e7').pack(side='left', padx=(0, 10))
        self.euler_entry = tk.Entry(input_frame, font=('Arial', 12), width=15, justify='center')
        self.euler_entry.pack(side='left', fill='x', expand=True)
        
        operations_frame = tk.LabelFrame(
            self.euler_tab,
            text="Operations",
            font=('Arial', 11, 'bold'),
            bg='#e8f8f5',
            fg='#34495e',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Button(
            operations_frame,
            text="Calculate φ(n) - Euler's Totient Function",
            command=self.calculate_euler,
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        tk.Button(
            operations_frame,
            text="Clear",
            command=self.clear_euler,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        result_frame = tk.LabelFrame(
            self.euler_tab,
            text="Result",
            font=('Arial', 11, 'bold'),
            bg='#e8f5e9',
            fg='#34495e',
            padx=10,
            pady=10
        )
        result_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.euler_result = tk.Text(
            result_frame,
            font=('Courier New', 10),
            height=15,
            wrap='word',
            bg='#ffffff',
            relief='sunken',
            bd=2
        )
        self.euler_result.pack(fill='both', expand=True)
    
    def create_inverse_tab(self):
        input_frame = tk.LabelFrame(
            self.inverse_tab,
            text="Input",
            font=('Arial', 11, 'bold'),
            bg='#fef5e7',
            fg='#34495e',
            padx=10,
            pady=10
        )
        input_frame.pack(fill='x', padx=10, pady=10)
        
        a_frame = tk.Frame(input_frame, bg='#fef5e7')
        a_frame.pack(fill='x', pady=5)
        tk.Label(a_frame, text="a =", font=('Arial', 11), bg='#fef5e7', width=5).pack(side='left')
        self.inv_a_entry = tk.Entry(a_frame, font=('Arial', 12), justify='center')
        self.inv_a_entry.pack(side='left', fill='x', expand=True)
        
        p_frame = tk.Frame(input_frame, bg='#fef5e7')
        p_frame.pack(fill='x', pady=5)
        tk.Label(p_frame, text="p =", font=('Arial', 11), bg='#fef5e7', width=5).pack(side='left')
        self.inv_p_entry = tk.Entry(p_frame, font=('Arial', 12), justify='center')
        self.inv_p_entry.pack(side='left', fill='x', expand=True)
        
        operations_frame = tk.LabelFrame(
            self.inverse_tab,
            text="Operations",
            font=('Arial', 11, 'bold'),
            bg='#e8f8f5',
            fg='#34495e',
            padx=10,
            pady=10
        )
        operations_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Button(
            operations_frame,
            text="Find a⁻¹ in G(p,*) using Euler's Theorem",
            command=self.calculate_inverse_euler,
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        tk.Button(
            operations_frame,
            text="Clear",
            command=self.clear_inverse,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            height=2,
            cursor='hand2'
        ).pack(fill='x', pady=5)
        
        result_frame = tk.LabelFrame(
            self.inverse_tab,
            text="Result",
            font=('Arial', 11, 'bold'),
            bg='#e8f5e9',
            fg='#34495e',
            padx=10,
            pady=10
        )
        result_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.inv_result = tk.Text(
            result_frame,
            font=('Courier New', 10),
            height=15,
            wrap='word',
            bg='#ffffff',
            relief='sunken',
            bd=2
        )
        self.inv_result.pack(fill='both', expand=True)
    
    # Basic operations (Lab 2)
    def mod(self, n, m):
        result = n % m
        return result if result >= 0 else result + m
    
    def add(self):
        try:
            m = int(self.modulus_entry.get())
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
            
            result = self.mod(a + b, m)
            output = f"Operation: a + b mod m\n\n"
            output += f"a = {a}, b = {b}, m = {m}\n\n"
            output += f"{a} + {b} = {a + b}\n"
            output += f"{a + b} mod {m} = {result}\n\n"
            output += f"Result: {result}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def subtract(self):
        try:
            m = int(self.modulus_entry.get())
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
            
            result = self.mod(a - b, m)
            output = f"Operation: a - b mod m\n\n"
            output += f"a = {a}, b = {b}, m = {m}\n\n"
            output += f"{a} - {b} = {a - b}\n"
            output += f"{a - b} mod {m} = {result}\n\n"
            output += f"Result: {result}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def negate(self):
        try:
            m = int(self.modulus_entry.get())
            a = int(self.a_entry.get())
            
            result = self.mod(-a, m)
            output = f"Operation: -a mod m\n\n"
            output += f"a = {a}, m = {m}\n\n"
            output += f"-{a} mod {m} = {result}\n\n"
            output += f"Verification: {a} + {result} = {self.mod(a + result, m)}\n\n"
            output += f"Result: {result}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def multiply(self):
        try:
            m = int(self.modulus_entry.get())
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
            
            result = self.mod(a * b, m)
            output = f"Operation: a × b mod m\n\n"
            output += f"a = {a}, b = {b}, m = {m}\n\n"
            output += f"{a} × {b} = {a * b}\n"
            output += f"{a * b} mod {m} = {result}\n\n"
            output += f"Result: {result}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def mod_inverse(self, a, m):
        a = self.mod(a, m)
        for x in range(1, m):
            if self.mod(a * x, m) == 1:
                return x
        return None
    
    def inverse_basic(self):
        try:
            m = int(self.modulus_entry.get())
            a = int(self.a_entry.get())
            
            inv = self.mod_inverse(a, m)
            
            if inv is None:
                output = f"Operation: a⁻¹ mod m\n\n"
                output += f"a = {a}, m = {m}\n\n"
                output += f"Result: NO INVERSE EXISTS\n"
                output += f"Reason: gcd({a}, {m}) ≠ 1"
            else:
                output = f"Operation: a⁻¹ mod m\n\n"
                output += f"a = {a}, m = {m}\n\n"
                output += f"Finding x where {a} × x ≡ 1 (mod {m})\n"
                output += f"Verification: {a} × {inv} = {self.mod(a * inv, m)}\n\n"
                output += f"Result: {inv}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def divide(self):
        try:
            m = int(self.modulus_entry.get())
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
            
            b_inv = self.mod_inverse(b, m)
            
            if b_inv is None:
                output = f"Operation: a ÷ b mod m\n\n"
                output += f"a = {a}, b = {b}, m = {m}\n\n"
                output += f"Result: DIVISION IMPOSSIBLE\n"
                output += f"Reason: {b} has no inverse mod {m}"
            else:
                result = self.mod(a * b_inv, m)
                output = f"Operation: a ÷ b mod m\n\n"
                output += f"a = {a}, b = {b}, m = {m}\n\n"
                output += f"b⁻¹ mod {m} = {b_inv}\n"
                output += f"{a} × {b_inv} = {self.mod(a * b_inv, m)}\n\n"
                output += f"Result: {result}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def mod_power(self, base, exp, m):
        result = 1
        base = self.mod(base, m)
        for i in range(exp):
            result = self.mod(result * base, m)
        return result
    
    def power(self):
        try:
            m = int(self.modulus_entry.get())
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
            
            if b < 0:
                messagebox.showerror("Error", "Exponent must be non-negative")
                return
            
            result = self.mod_power(a, b, m)
            
            output = f"Operation: a^b mod m\n\n"
            output += f"a = {a}, b = {b}, m = {m}\n\n"
            output += f"Computing {a}^{b} mod {m}\n\n"
            output += f"Result: {result}"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def clear_basic(self):
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
    
    # Prime number operations
    def is_prime_fermat(self, p, iterations=10):
        if p < 2:
            return False
        if p == 2 or p == 3:
            return True
        if p % 2 == 0:
            return False
        
        import random
        for _ in range(iterations):
            a = random.randint(2, p - 2)
            if self.mod_power(a, p - 1, p) != 1:
                return False
        return True
    
    def check_prime(self):
        try:
            n = int(self.prime_entry.get())
            
            output = f"Primality Test using Fermat's Little Theorem\n"
            output += f"=" * 50 + "\n\n"
            output += f"Number to test: {n}\n\n"
            
            if n < 2:
                output += f"Result: NOT PRIME (less than 2)\n"
            else:
                output += f"Testing: a^(p-1) ≡ 1 (mod p) for random a ∈ [2, {n-2}]\n\n"
                
                is_prime = self.is_prime_fermat(n, 10)
                
                if is_prime:
                    output += f"All tests passed!\n"
                    output += f"Result: {n} is PROBABLY PRIME\n"
                else:
                    output += f"Test failed!\n"
                    output += f"Result: {n} is COMPOSITE\n"
            
            self.prime_result.delete(1.0, tk.END)
            self.prime_result.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input value")
    
    def generate_prime(self):
        try:
            bound = int(self.prime_bound_entry.get())
            
            if bound < 2:
                messagebox.showerror("Error", "Bound must be at least 2")
                return
            
            output = f"Generate Prime Number p ≤ {bound}\n"
            output += f"=" * 50 + "\n\n"
            
            # Find largest prime <= bound
            import random
            candidates = []
            
            for p in range(max(2, bound - 100), bound + 1):
                if self.is_prime_fermat(p, 5):
                    candidates.append(p)
            
            if candidates:
                prime = random.choice(candidates)
                output += f"Generated prime: {prime}\n\n"
                output += f"Verification using Fermat's test:\n"
                output += f"{prime}^({prime}-1) ≡ 1 (mod {prime}) for random bases\n\n"
                output += f"Result: {prime} is PRIME\n"
            else:
                output += f"No prime found in range [2, {bound}]\n"
            
            self.prime_result.delete(1.0, tk.END)
            self.prime_result.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid bound value")
    
    def clear_prime(self):
        self.prime_entry.delete(0, tk.END)
        self.prime_bound_entry.delete(0, tk.END)
        self.prime_result.delete(1.0, tk.END)
    
    # GCD operations
    def gcd_euclidean(self, a, b):
        steps = []
        original_a, original_b = a, b
        
        step_num = 1
        while b != 0:
            q = a // b
            r = a % b
            steps.append({
                'step': step_num,
                'a': a,
                'b': b,
                'q': q,
                'r': r,
                'equation': f"{a} = {q} × {b} + {r}"
            })
            a, b = b, r
            step_num += 1
        
        return a, steps
    
    def calculate_gcd(self):
        try:
            a = int(self.gcd_a_entry.get())
            b = int(self.gcd_b_entry.get())
            
            if a < 0 or b < 0:
                messagebox.showerror("Error", "Numbers must be non-negative")
                return
            
            if a < b:
                a, b = b, a
            
            gcd, steps = self.gcd_euclidean(a, b)
            
            output = f"Euclidean Algorithm for GCD({a}, {b})\n"
            output += f"=" * 50 + "\n\n"
            
            output += f"Step | a     | b     | a = q × b + r\n"
            output += f"-----|-------|-------|" + "-" * 30 + "\n"
            
            for step in steps:
                output += f"{step['step']:4d} | {step['a']:5d} | {step['b']:5d} | {step['equation']}\n"
                if step['r'] == 0:
                    output += f"\nr = 0, algorithm stops\n"
            
            output += f"\n" + "=" * 50 + "\n"
            output += f"GCD({a}, {b}) = {gcd}\n\n"
            
            if gcd == 1:
                output += f"Numbers {a} and {b} are COPRIME (mutually prime)\n"
            else:
                output += f"Numbers {a} and {b} are NOT coprime\n"
                output += f"Common divisor: {gcd}\n"
            
            self.gcd_result.delete(1.0, tk.END)
            self.gcd_result.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def clear_gcd(self):
        self.gcd_a_entry.delete(0, tk.END)
        self.gcd_b_entry.delete(0, tk.END)
        self.gcd_result.delete(1.0, tk.END)
    
    # Euler function operations
    def phi_euler(self, n):
        result = n
        factors = []
        original_n = n
        
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
                result -= result // i
            i += 1
        
        if n > 1:
            factors.append(n)
            result -= result // n
        
        return result, factors, original_n
    
    def calculate_euler(self):
        try:
            n = int(self.euler_entry.get())
            
            if n < 1:
                messagebox.showerror("Error", "n must be positive")
                return
            
            phi, factors, original = self.phi_euler(n)
            
            output = f"Euler's Totient Function φ({n})\n"
            output += f"=" * 50 + "\n\n"
            
            if n == 1:
                output += f"φ(1) = 1 (by definition)\n"
            else:
                output += f"Step 1: Prime factorization of {n}\n"
                
                # Show factorization
                temp_n = n
                factorization = []
                for p in factors:
                    count = 0
                    while temp_n % p == 0:
                        temp_n //= p
                        count += 1
                    if count == 1:
                        factorization.append(str(p))
                    else:
                        factorization.append(f"{p}^{count}")
                
                output += f"{n} = {' × '.join(factorization)}\n\n"
                
                output += f"Step 2: Apply Euler's formula\n"
                output += f"φ(n) = n"
                for p in factors:
                    output += f" × (1 - 1/{p})"
                output += "\n\n"
                
                output += f"Step 3: Calculate\n"
                output += f"φ({n}) = {n}"
                for p in factors:
                    output += f" × ({p}-1)/{p}"
                output += f"\n"
                output += f"φ({n}) = {phi}\n\n"
            
            output += f"=" * 50 + "\n"
            output += f"Result: φ({n}) = {phi}\n\n"
            output += f"Meaning: There are {phi} positive integers\n"
            output += f"less than {n} that are coprime to {n}\n"
            
            self.euler_result.delete(1.0, tk.END)
            self.euler_result.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input value")
    
    def clear_euler(self):
        self.euler_entry.delete(0, tk.END)
        self.euler_result.delete(1.0, tk.END)
    
    # Modular inverse using Euler's theorem
    def calculate_inverse_euler(self):
        try:
            a = int(self.inv_a_entry.get())
            p = int(self.inv_p_entry.get())
            
            # Check if a and p are coprime
            gcd, _ = self.gcd_euclidean(a, p)
            
            if gcd != 1:
                output = f"Modular Inverse using Euler's Theorem\n"
                output += f"=" * 50 + "\n\n"
                output += f"a = {a}, p = {p}\n\n"
                output += f"ERROR: Cannot find inverse!\n"
                output += f"Reason: gcd({a}, {p}) = {gcd} ≠ 1\n"
                output += f"Numbers must be coprime.\n"
            else:
                # Calculate φ(p)
                phi_p, factors, _ = self.phi_euler(p)
                
                output = f"Modular Inverse using Euler's Theorem\n"
                output += f"=" * 50 + "\n\n"
                output += f"Find a⁻¹ in multiplicative group G({p}, *)\n\n"
                output += f"Given: a = {a}, p = {p}\n\n"
                
                output += f"Step 1: Calculate φ({p})\n"
                output += f"φ({p}) = {phi_p}\n\n"
                
                output += f"Step 2: Apply Euler's theorem\n"
                output += f"a^φ(m) ≡ 1 (mod m) when gcd(a,m) = 1\n"
                output += f"Therefore: a^(φ(m)-1) ≡ a⁻¹ (mod m)\n\n"
                
                output += f"Step 3: Calculate a⁻¹\n"
                output += f"a⁻¹ = a^(φ({p})-1) mod {p}\n"
                output += f"a⁻¹ = {a}^({phi_p}-1) mod {p}\n"
                output += f"a⁻¹ = {a}^{phi_p-1} mod {p}\n"
                
                # Calculate inverse
                inverse = self.mod_power(a, phi_p - 1, p)
                
                output += f"a⁻¹ = {inverse}\n\n"
                
                output += f"Step 4: Verification\n"
                verification = self.mod(a * inverse, p)
                output += f"{a} × {inverse} mod {p} = {a * inverse} mod {p} = {verification}\n\n"
                
                if verification == 1:
                    output += f"✓ Verification successful!\n\n"
                
                output += f"=" * 50 + "\n"
                output += f"Result: {a}⁻¹ ≡ {inverse} (mod {p})\n"
            
            self.inv_result.delete(1.0, tk.END)
            self.inv_result.insert(1.0, output)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")
    
    def clear_inverse(self):
        self.inv_a_entry.delete(0, tk.END)
        self.inv_p_entry.delete(0, tk.END)
        self.inv_result.delete(1.0, tk.END)


def main():
    root = tk.Tk()
    app = ModularCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()