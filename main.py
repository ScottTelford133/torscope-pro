# main.py
import tkinter as tk
from tkinter import messagebox

def start_research():
    messagebox.showinfo("TorScope Pro", "Research started!\nFull version includes Tor verification and AI.")

# GUI Setup
root = tk.Tk()
root.title("TorScope Pro v6.0")
root.geometry("900x600")
root.configure(bg="#1a1a1a")

# Header
title = tk.Label(root, text="🔐 TorScope Pro", font=("Segoe UI", 28, "bold"), fg="#00d4aa", bg="#1a1a1a")
title.pack(pady=30)

subtitle = tk.Label(root, text="Advanced Tor Research & Monitoring Suite", font=("Segoe UI", 14), fg="#b0b0b0", bg="#1a1a1a")
subtitle.pack(pady=10)

# Button
start_btn = tk.Button(root, text="Launch Research Suite", font=("Segoe UI", 16, "bold"),
                      bg="#00d4aa", fg="white", width=25, height=2, command=start_research)
start_btn.pack(pady=50)

# Footer
footer = tk.Label(root, text="Ethical Use Only • Open Source • v6.0", font=("Segoe UI", 10), fg="#555555", bg="#1a1a1a")
footer.pack(side="bottom", pady=20)

root.mainloop()