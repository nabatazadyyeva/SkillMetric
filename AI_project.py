import tkinter as tk
from tkinter import messagebox
import json
import os

# --- DATABASE: 50 QUESTIONS (English Version) ---
questions_db = [
    # Syntax
    {"q": "Exponentiation operator in Python?", "a": "**", "cat": "Syntax", "pts": 1},
    {"q": "Data type for immutable lists?", "a": "tuple", "cat": "Syntax", "pts": 1},
    {"q": "Function to output to console?", "a": "print", "cat": "Syntax", "pts": 1},
    {"q": "Convert '10' to an integer?", "a": "int", "cat": "Syntax", "pts": 1},
    {"q": "String method for lowercase?", "a": "lower", "cat": "Syntax", "pts": 2},
    {"q": "How to check type of variable x?", "a": "type(x)", "cat": "Syntax", "pts": 1},
    {"q": "Keyword to break a loop?", "a": "break", "cat": "Syntax", "pts": 1},
    {"q": "What does bool(0) return?", "a": "false", "cat": "Syntax", "pts": 2},
    {"q": "The null data type in Python?", "a": "none", "cat": "Syntax", "pts": 1},
    {"q": "Method to replace substring?", "a": "replace", "cat": "Syntax", "pts": 2},
    {"q": "Operator to check membership?", "a": "in", "cat": "Syntax", "pts": 1},
    {"q": "Index of the last element?", "a": "-1", "cat": "Syntax", "pts": 2},
    {"q": "Keyword used in generators?", "a": "yield", "cat": "Syntax", "pts": 3},
    {"q": "Function to open a file?", "a": "open", "cat": "Syntax", "pts": 1},
    {"q": "Import module with alias keyword?", "a": "as", "cat": "Syntax", "pts": 1},
    {"q": "Method to remove whitespaces?", "a": "strip", "cat": "Syntax", "pts": 2},
    {"q": "Function for string length?", "a": "len", "cat": "Syntax", "pts": 1},
    # Algorithms
    {"q": "Search that divides array in half?", "a": "binary", "cat": "Algorithms", "pts": 3},
    {"q": "Result of 10 % 3?", "a": "1", "cat": "Algorithms", "pts": 2},
    {"q": "Complexity of a single loop (O...)?", "a": "O(n)", "cat": "Algorithms", "pts": 3},
    {"q": "Function calling itself is called...?", "a": "recursion", "cat": "Algorithms", "pts": 3},
    {"q": "Result of 5 > 3 and 2 > 10?", "a": "false", "cat": "Algorithms", "pts": 2},
    {"q": "Sort by choosing the minimum?", "a": "selection", "cat": "Algorithms", "pts": 2},
    {"q": "Result of 2 ** 10?", "a": "1024", "cat": "Algorithms", "pts": 2},
    {"q": "A graph without cycles?", "a": "tree", "cat": "Algorithms", "pts": 2},
    {"q": "Search complexity in a dictionary?", "a": "O(1)", "cat": "Algorithms", "pts": 3},
    {"q": "Shortest path algorithm name?", "a": "dijkstra", "cat": "Algorithms", "pts": 3},
    {"q": "LIFO data structure name?", "a": "stack", "cat": "Algorithms", "pts": 2},
    {"q": "How many times range(5) iterates?", "a": "5", "cat": "Algorithms", "pts": 1},
    {"q": "Find maximum in list — function?", "a": "max", "cat": "Algorithms", "pts": 1},
    {"q": "Structure with nodes and edges?", "a": "graph", "cat": "Algorithms", "pts": 2},
    {"q": "Result of 10 // 3?", "a": "3", "cat": "Algorithms", "pts": 2},
    {"q": "Trial of all possible variants?", "a": "bruteforce", "cat": "Algorithms", "pts": 3},
    {"q": "Which is faster: O(1) or O(n)?", "a": "o(1)", "cat": "Algorithms", "pts": 2},
    # OOP
    {"q": "New class based on an old one?", "a": "inheritance", "cat": "OOP", "pts": 2},
    {"q": "FIFO data structure name?", "a": "queue", "cat": "OOP", "pts": 3},
    {"q": "Keyword to create a class?", "a": "class", "cat": "OOP", "pts": 1},
    {"q": "Method called during object creation?", "a": "__init__", "cat": "OOP", "pts": 2},
    {"q": "Hiding data inside a class?", "a": "encapsulation", "cat": "OOP", "pts": 3},
    {"q": "Reference to parent class in OOP?", "a": "super", "cat": "OOP", "pts": 2},
    {"q": "Data type for True/False?", "a": "bool", "cat": "OOP", "pts": 1},
    {"q": "Key-value structure in Python?", "a": "dict", "cat": "OOP", "pts": 1},
    {"q": "Method to remove by value?", "a": "remove", "cat": "OOP", "pts": 2},
    {"q": "Class that cannot be instantiated?", "a": "abstract", "cat": "OOP", "pts": 3},
    {"q": "Immutable version of a set?", "a": "frozenset", "cat": "OOP", "pts": 3},
    {"q": "Changing operator behavior?", "a": "overloading", "cat": "OOP", "pts": 3},
    {"q": "Handling errors — keyword?", "a": "except", "cat": "OOP", "pts": 2},
    {"q": "String representation method?", "a": "__str__", "cat": "OOP", "pts": 3},
    {"q": "Collection of unique elements?", "a": "set", "cat": "OOP", "pts": 2},
    {"q": "How to create an empty dict?", "a": "{}", "cat": "OOP", "pts": 1}
]

class SkillApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SkillMetric ")
        self.root.geometry("650x600")
        self.root.configure(bg="#f4f7f9")
        self.results_file = "skillmetric_v1.json"
        self.main_menu()

    def main_menu(self):
        self.clear()
        tk.Label(self.root, text="Professional Dev Assessment", font=("Arial", 22, "bold"), bg="#f4f7f9", fg="#007d43").pack(pady=40)
        tk.Label(self.root, text="Enter your name:", font=("Arial", 12), bg="#f4f7f9").pack()
        self.name_ent = tk.Entry(self.root, font=("Arial", 14), width=25)
        self.name_ent.pack(pady=10)
        tk.Button(self.root, text="START TEST", command=self.start, bg="#007d43", fg="white", font=("Arial", 12, "bold"), width=20, height=2).pack(pady=20)
        tk.Button(self.root, text="LEADERBOARD", command=self.show_rating, font=("Arial", 11), width=20).pack()

    def start(self):
        self.user = self.name_ent.get().strip()
        if not self.user: 
            messagebox.showwarning("Warning", "Please enter your name!")
            return
        self.idx, self.score = 0, 0
        self.stats = {"Syntax": 0, "Algorithms": 0, "OOP": 0}
        self.ask()

    def ask(self):
        self.clear()
        if self.idx < len(questions_db):
            q = questions_db[self.idx]
            tk.Label(self.root, text=f"Question {self.idx + 1}/50 | {q['cat']}", fg="gray", bg="#f4f7f9").pack()
            tk.Label(self.root, text=q['q'], font=("Arial", 16, "bold"), wraplength=550, bg="#f4f7f9").pack(pady=40)
            self.ans_ent = tk.Entry(self.root, font=("Arial", 16))
            self.ans_ent.pack()
            self.ans_ent.focus_set()
            self.root.bind('<Return>', lambda e: self.check())
            tk.Button(self.root, text="SUBMIT", command=self.check, bg="#1a73e8", fg="white", font=("Arial", 12, "bold"), width=15).pack(pady=30)
        else:
            self.finish()

    def check(self):
        ans = self.ans_ent.get().lower().strip()
        q = questions_db[self.idx]
        if ans == q['a'].lower():
            self.score += q['pts']
            self.stats[q['cat']] += q['pts']
        self.idx += 1
        self.ask()

    def finish(self):
        self.clear()
        level = "Junior"
        if self.score > 15: level = "Middle"
        if self.score > 30: level = "Senior"
        if self.score > 45: level = "Master"
        best = max(self.stats, key=self.stats.get)
        
        tk.Label(self.root, text="TEST COMPLETED", font=("Arial", 22, "bold"), bg="#f4f7f9", fg="#1a73e8").pack(pady=20)
        tk.Label(self.root, text=f"Candidate: {self.user}", font=("Arial", 14), bg="#f4f7f9").pack()
        tk.Label(self.root, text=f"Total Score: {self.score} | Rank: {level}", font=("Arial", 16, "bold"), fg="#007d43", bg="#f4f7f9").pack(pady=10)
        tk.Label(self.root, text=f"Top Skill: {best}", font=("Arial", 12), bg="#f4f7f9").pack(pady=10)
        
        self.save(level, best)
        tk.Button(self.root, text="VIEW LEADERBOARD", command=self.show_rating, bg="#1a73e8", fg="white", width=22).pack(pady=20)
        tk.Button(self.root, text="MAIN MENU", command=self.main_menu).pack()

    def save(self, level, best):
        data = []
        if os.path.exists(self.results_file):
            try:
                with open(self.results_file, "r", encoding="utf-8") as f: data = json.load(f)
            except: data = []
        data.append({"name": self.user, "score": self.score, "level": level, "best": best})
        with open(self.results_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def show_rating(self):
        self.clear()
        tk.Label(self.root, text="GLOBAL TOP 10", font=("Arial", 20, "bold"), fg="#007d43", bg="#f4f7f9").pack(pady=20)
        container = tk.Frame(self.root, bg="white", relief="solid", bd=1)
        container.pack(padx=20, fill="both", expand=True)

        if os.path.exists(self.results_file):
            with open(self.results_file, "r", encoding="utf-8") as f:
                records = sorted(json.load(f), key=lambda x: x['score'], reverse=True)
                for i, r in enumerate(records[:10]):
                    txt = f"{i+1}. {r['name']} | Score: {r['score']} | {r.get('level')} | Expert in {r.get('best')}"
                    tk.Label(container, text=txt, font=("Arial", 10), bg="white", anchor="w").pack(fill="x", padx=15, pady=5)
        else:
            tk.Label(container, text="No records found.", bg="white").pack(pady=20)
            
        tk.Button(self.root, text="BACK TO MENU", command=self.main_menu, bg="#1a73e8", fg="white", width=20).pack(pady=20)

    def clear(self):
        for w in self.root.winfo_children(): w.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SkillApp(root)
    root.mainloop()
