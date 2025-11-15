import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import os


class HammingCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кодування Хемінга - Лабораторна робота 1")
        self.root.geometry("900x700")

        # Створення вкладок
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Вкладка 1: Ручне кодування
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Завдання 1: Ручне кодування")
        self.create_manual_tab()

        # Вкладка 2: Робота з файлами
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Завдання 2-3: Робота з файлами")
        self.create_file_tab()

    def create_manual_tab(self):
        """Вкладка для ручного кодування тексту"""
        # Фрейм введення
        input_frame = ttk.LabelFrame(self.tab1, text="Введення даних", padding=10)
        input_frame.pack(fill='x', padx=10, pady=5)

        ttk.Label(input_frame, text="Введіть текст (прізвище/ім'я):").grid(row=0, column=0, sticky='w')
        self.text_input = ttk.Entry(input_frame, width=40)
        self.text_input.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="Номер за журналом (N):").grid(row=1, column=0, sticky='w', pady=5)
        self.n_input = ttk.Entry(input_frame, width=10)
        self.n_input.grid(row=1, column=1, sticky='w', padx=5, pady=5)

        ttk.Button(input_frame, text="Кодувати", command=self.encode_manual).grid(row=2, column=0, columnspan=2, pady=5)

        # Фрейм результатів
        result_frame = ttk.LabelFrame(self.tab1, text="Результати", padding=10)
        result_frame.pack(fill='both', expand=True, padx=10, pady=5)

        self.result_text = scrolledtext.ScrolledText(result_frame, height=25, wrap=tk.WORD)
        self.result_text.pack(fill='both', expand=True)

    def create_file_tab(self):
        """Вкладка для роботи з файлами"""
        # Фрейм налаштувань
        settings_frame = ttk.LabelFrame(self.tab2, text="Налаштування", padding=10)
        settings_frame.pack(fill='x', padx=10, pady=5)

        ttk.Label(settings_frame, text="Розмір блоку (біт):").grid(row=0, column=0, sticky='w')
        self.block_size = ttk.Combobox(settings_frame, values=[8, 16, 32, 64, 128, 256], width=10)
        self.block_size.set(8)
        self.block_size.grid(row=0, column=1, padx=5)

        # Фрейм кодування
        encode_frame = ttk.LabelFrame(self.tab2, text="Кодування файлу", padding=10)
        encode_frame.pack(fill='x', padx=10, pady=5)

        ttk.Button(encode_frame, text="Вибрати файл для кодування", command=self.select_encode_file).pack(pady=5)
        self.encode_file_label = ttk.Label(encode_frame, text="Файл не вибрано")
        self.encode_file_label.pack()
        ttk.Button(encode_frame, text="Кодувати файл", command=self.encode_file).pack(pady=5)

        # Фрейм декодування
        decode_frame = ttk.LabelFrame(self.tab2, text="Декодування файлу", padding=10)
        decode_frame.pack(fill='x', padx=10, pady=5)

        ttk.Button(decode_frame, text="Вибрати файл для декодування", command=self.select_decode_file).pack(pady=5)
        self.decode_file_label = ttk.Label(decode_frame, text="Файл не вибрано")
        self.decode_file_label.pack()

        ttk.Label(decode_frame, text="Внести помилку в біт №:").pack()
        self.error_bit = ttk.Entry(decode_frame, width=10)
        self.error_bit.pack()
        ttk.Label(decode_frame, text="(0 = без помилок)").pack()

        ttk.Button(decode_frame, text="Декодувати файл", command=self.decode_file).pack(pady=5)

        # Фрейм логів
        log_frame = ttk.LabelFrame(self.tab2, text="Лог операцій", padding=10)
        log_frame.pack(fill='both', expand=True, padx=10, pady=5)

        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, wrap=tk.WORD)
        self.log_text.pack(fill='both', expand=True)

        self.encoded_file_path = None
        self.decoded_file_path = None

    def calculate_hamming_positions(self, n):
        """Обчислює позиції контрольних бітів"""
        control_positions = []
        i = 0
        while 2 ** i <= n:
            control_positions.append(2 ** i)
            i += 1
        return control_positions

    def encode_hamming(self, data_bits):
        """Кодує дані кодом Хемінга"""
        m = len(data_bits)

        # Визначаємо кількість контрольних бітів
        r = 0
        while 2 ** r < m + r + 1:
            r += 1

        # Загальна довжина кодового слова
        n = m + r

        # Створюємо кодове слово
        hamming_code = [0] * (n + 1)  # +1 бо нумерація з 1

        # Заповнюємо інформаційні біти
        j = 0
        for i in range(1, n + 1):
            # Перевіряємо чи це не позиція контрольного біту
            if (i & (i - 1)) != 0:  # не степінь 2
                hamming_code[i] = data_bits[j]
                j += 1

        # Обчислюємо контрольні біти
        for i in range(r):
            parity_pos = 2 ** i
            parity = 0
            for j in range(1, n + 1):
                if j & parity_pos and hamming_code[j]:
                    parity ^= 1
            hamming_code[parity_pos] = parity

        return hamming_code[1:]  # Повертаємо без нульового елемента

    def decode_hamming(self, hamming_code):
        """Декодує код Хемінга і виправляє одиночну помилку"""
        n = len(hamming_code)

        # Визначаємо кількість контрольних бітів
        r = 0
        while 2 ** r < n + 1:
            r += 1

        # Перевіряємо контрольні біти
        error_pos = 0
        for i in range(r):
            parity_pos = 2 ** i
            parity = 0
            for j in range(1, n + 1):
                if j & parity_pos and hamming_code[j - 1]:
                    parity ^= 1
            if parity != 0:
                error_pos += parity_pos

        # Якщо є помилка - виправляємо
        corrected_code = hamming_code.copy()
        if error_pos > 0:
            corrected_code[error_pos - 1] ^= 1

        # Витягуємо інформаційні біти
        data_bits = []
        for i in range(1, n + 1):
            if (i & (i - 1)) != 0:  # не степінь 2
                data_bits.append(corrected_code[i - 1])

        return data_bits, error_pos

    def text_to_binary(self, text):
        """Конвертує текст в двійкові біти"""
        binary = []
        for char in text:
            ascii_val = ord(char)
            bits = [int(b) for b in format(ascii_val, '08b')]
            binary.extend(bits)
        return binary

    def binary_to_text(self, binary):
        """Конвертує двійкові біти в текст"""
        text = ""
        for i in range(0, len(binary), 8):
            byte = binary[i:i + 8]
            if len(byte) == 8:
                ascii_val = int(''.join(map(str, byte)), 2)
                text += chr(ascii_val)
        return text

    def encode_manual(self):
        """Обробник для ручного кодування"""
        text = self.text_input.get()
        n_str = self.n_input.get()

        if not text or len(text) < 5:
            messagebox.showerror("Помилка", "Введіть текст мінімум 5 символів!")
            return

        if not n_str:
            messagebox.showerror("Помилка", "Введіть номер за журналом!")
            return

        try:
            n = int(n_str)
        except:
            messagebox.showerror("Помилка", "Номер за журналом має бути числом!")
            return

        # Очищаємо результати
        self.result_text.delete(1.0, tk.END)

        # Виводимо вихідний текст
        self.result_text.insert(tk.END, f"=== ЗАВДАННЯ 1 ===\n\n")
        self.result_text.insert(tk.END, f"Вихідний текст: {text}\n\n")

        # ASCII коди
        self.result_text.insert(tk.END, "ASCII коди (HEX):\n")
        for char in text:
            self.result_text.insert(tk.END, f"'{char}' = {ord(char)} = 0x{ord(char):02X}\n")

        # Двійкове представлення
        binary = self.text_to_binary(text)
        self.result_text.insert(tk.END, f"\nДвійкове представлення ({len(binary)} біт):\n")
        binary_str = ''.join(map(str, binary))
        for i in range(0, len(binary_str), 64):
            self.result_text.insert(tk.END, binary_str[i:i + 64] + "\n")

        # Кодування Хемінга
        self.result_text.insert(tk.END, f"\n=== КОДУВАННЯ ХЕМІНГА ===\n\n")
        hamming_code = self.encode_hamming(binary)
        self.result_text.insert(tk.END, f"Закодований код ({len(hamming_code)} біт):\n")
        hamming_str = ''.join(map(str, hamming_code))
        for i in range(0, len(hamming_str), 64):
            self.result_text.insert(tk.END, hamming_str[i:i + 64] + "\n")

        # Внесення помилки в N-ий біт
        if n > 0 and n <= len(hamming_code):
            self.result_text.insert(tk.END, f"\n=== ПОМИЛКА В БІТІ №{n} ===\n\n")
            corrupted = hamming_code.copy()
            corrupted[n - 1] ^= 1

            self.result_text.insert(tk.END, f"Пошкоджений код:\n")
            corrupted_str = ''.join(map(str, corrupted))
            for i in range(0, len(corrupted_str), 64):
                self.result_text.insert(tk.END, corrupted_str[i:i + 64] + "\n")

            # Декодування та виправлення
            decoded, error_pos = self.decode_hamming(corrupted)
            self.result_text.insert(tk.END, f"\nПозиція виявленої помилки: {error_pos}\n")

            if error_pos == n:
                self.result_text.insert(tk.END, "✓ Помилка успішно виявлена і виправлена!\n")

            # Відновлений текст
            recovered_text = self.binary_to_text(decoded)
            self.result_text.insert(tk.END, f"Відновлений текст: {recovered_text}\n")

        # Внесення двох помилок
        n2 = 35 - n
        if n > 0 and n <= len(hamming_code) and n2 > 0 and n2 <= len(hamming_code):
            self.result_text.insert(tk.END, f"\n=== ДВІ ПОМИЛКИ (біти №{n} та №{n2}) ===\n\n")
            corrupted2 = hamming_code.copy()
            corrupted2[n - 1] ^= 1
            corrupted2[n2 - 1] ^= 1

            self.result_text.insert(tk.END, f"Пошкоджений код (дві помилки):\n")
            corrupted2_str = ''.join(map(str, corrupted2))
            for i in range(0, len(corrupted2_str), 64):
                self.result_text.insert(tk.END, corrupted2_str[i:i + 64] + "\n")

            # Спроба декодування
            decoded2, error_pos2 = self.decode_hamming(corrupted2)
            self.result_text.insert(tk.END, f"\nПозиція виявленої помилки: {error_pos2}\n")

            recovered_text2 = self.binary_to_text(decoded2)
            self.result_text.insert(tk.END, f"Відновлений текст: {recovered_text2}\n")

            if recovered_text2 != text:
                self.result_text.insert(tk.END, "\n✗ ПОМИЛКА! Код Хемінга не може виправити дві помилки!\n")
                self.result_text.insert(tk.END, "Код Хемінга може виявити і виправити лише одиночні помилки.\n")
            else:
                self.result_text.insert(tk.END, "\n✓ Дані відновлено (випадково збіглося)\n")

    def select_encode_file(self):
        """Вибір файлу для кодування"""
        filename = filedialog.askopenfilename(
            title="Виберіть текстовий файл",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.encoded_file_path = filename
            self.encode_file_label.config(text=os.path.basename(filename))

    def select_decode_file(self):
        """Вибір файлу для декодування"""
        filename = filedialog.askopenfilename(
            title="Виберіть закодований файл",
            filetypes=[("Hamming files", "*.ham"), ("All files", "*.*")]
        )
        if filename:
            self.decoded_file_path = filename
            self.decode_file_label.config(text=os.path.basename(filename))

    def encode_file(self):
        """Кодування файлу"""
        if not self.encoded_file_path:
            messagebox.showerror("Помилка", "Виберіть файл для кодування!")
            return

        try:
            block_size = int(self.block_size.get())
        except:
            messagebox.showerror("Помилка", "Невірний розмір блоку!")
            return

        try:
            # Читаємо файл
            with open(self.encoded_file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.log_text.insert(tk.END, f"\n=== КОДУВАННЯ ФАЙЛУ ===\n")
            self.log_text.insert(tk.END, f"Файл: {os.path.basename(self.encoded_file_path)}\n")
            self.log_text.insert(tk.END, f"Розмір: {len(content)} символів\n")
            self.log_text.insert(tk.END, f"Розмір блоку: {block_size} біт\n\n")

            # Конвертуємо в біти
            all_bits = self.text_to_binary(content)
            self.log_text.insert(tk.END, f"Загальна кількість біт даних: {len(all_bits)}\n")

            # Розбиваємо на блоки і кодуємо
            encoded_blocks = []
            for i in range(0, len(all_bits), block_size):
                block = all_bits[i:i + block_size]

                # Доповнюємо останній блок нулями
                if len(block) < block_size:
                    block.extend([0] * (block_size - len(block)))

                encoded_block = self.encode_hamming(block)
                encoded_blocks.append(encoded_block)

            self.log_text.insert(tk.END, f"Кількість блоків: {len(encoded_blocks)}\n")

            # Зберігаємо закодований файл
            output_path = self.encoded_file_path + ".ham"
            with open(output_path, 'w') as f:
                f.write(f"{block_size}\n")  # Зберігаємо розмір блоку
                f.write(f"{len(all_bits)}\n")  # Зберігаємо оригінальну довжину
                for block in encoded_blocks:
                    f.write(''.join(map(str, block)) + '\n')

            self.log_text.insert(tk.END, f"\n✓ Файл закодовано: {os.path.basename(output_path)}\n")
            self.log_text.see(tk.END)

            messagebox.showinfo("Успіх", f"Файл закодовано!\nЗбережено як: {os.path.basename(output_path)}")

        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка при кодуванні:\n{str(e)}")
            self.log_text.insert(tk.END, f"\n✗ ПОМИЛКА: {str(e)}\n")

    def decode_file(self):
        """Декодування файлу"""
        if not self.decoded_file_path:
            messagebox.showerror("Помилка", "Виберіть файл для декодування!")
            return

        try:
            error_bit_num = 0
            if self.error_bit.get():
                error_bit_num = int(self.error_bit.get())
        except:
            messagebox.showerror("Помилка", "Невірний номер біту для помилки!")
            return

        try:
            # Читаємо закодований файл
            with open(self.decoded_file_path, 'r') as f:
                lines = f.readlines()

            block_size = int(lines[0].strip())
            original_length = int(lines[1].strip())
            encoded_blocks = [list(map(int, line.strip())) for line in lines[2:]]

            self.log_text.insert(tk.END, f"\n=== ДЕКОДУВАННЯ ФАЙЛУ ===\n")
            self.log_text.insert(tk.END, f"Файл: {os.path.basename(self.decoded_file_path)}\n")
            self.log_text.insert(tk.END, f"Розмір блоку: {block_size} біт\n")
            self.log_text.insert(tk.END, f"Кількість блоків: {len(encoded_blocks)}\n")

            # Внесення помилки якщо потрібно
            if error_bit_num > 0:
                total_bits = sum(len(block) for block in encoded_blocks)
                if error_bit_num <= total_bits:
                    block_idx = (error_bit_num - 1) // len(encoded_blocks[0])
                    bit_idx = (error_bit_num - 1) % len(encoded_blocks[0])
                    encoded_blocks[block_idx][bit_idx] ^= 1
                    self.log_text.insert(tk.END, f"Внесено помилку в біт №{error_bit_num}\n")

            # Декодуємо блоки
            all_decoded = []
            errors_found = 0
            for i, block in enumerate(encoded_blocks):
                decoded, error_pos = self.decode_hamming(block)
                if error_pos > 0:
                    errors_found += 1
                    self.log_text.insert(tk.END, f"Блок {i + 1}: виявлено помилку в позиції {error_pos}\n")
                all_decoded.extend(decoded)

            # Обрізаємо до оригінальної довжини
            all_decoded = all_decoded[:original_length]

            # Конвертуємо назад в текст
            recovered_text = self.binary_to_text(all_decoded)

            # Зберігаємо відновлений файл
            output_path = self.decoded_file_path.replace('.ham', '_decoded.txt')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(recovered_text)

            self.log_text.insert(tk.END, f"\nВиявлено помилок: {errors_found}\n")
            self.log_text.insert(tk.END, f"✓ Файл декодовано: {os.path.basename(output_path)}\n")
            self.log_text.insert(tk.END, f"Відновлено {len(recovered_text)} символів\n")
            self.log_text.see(tk.END)

            messagebox.showinfo("Успіх",
                                f"Файл декодовано!\n"
                                f"Виявлено помилок: {errors_found}\n"
                                f"Збережено як: {os.path.basename(output_path)}")

        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка при декодуванні:\n{str(e)}")
            self.log_text.insert(tk.END, f"\n✗ ПОМИЛКА: {str(e)}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = HammingCodeApp(root)
    root.mainloop()