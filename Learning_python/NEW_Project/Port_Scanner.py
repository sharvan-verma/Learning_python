import socket
import sys
import threading
import time
import tkinter as tk
from tkinter import scrolledtext, messagebox

def scan_ports():
    target = target_entry.get()
    start_port = start_port_entry.get()
    end_port = end_port_entry.get()

    if not target or not start_port or not end_port:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        target = socket.gethostbyname(target)
        start_port = int(start_port)
        end_port = int(end_port)
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range")
    except socket.gaierror:
        messagebox.showerror("Error", "Name Resolution error")
        return
    except ValueError as e:
        messagebox.showerror("Error", f"Error: {e}")
        return

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Scanning target {target}\n", "header")
    open_ports = []
    start_time = time.time()

    def scan_port(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            conn = s.connect_ex((target, port))
            if conn == 0:
                output_text.insert(tk.END, f"port {port} is open\n", "open")
                open_ports.append(port)
        except socket.error:
            pass
        finally:
            s.close()

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    output_text.insert(tk.END, "Scan Complete\n", "header")
    output_text.insert(tk.END, f"Time elapsed: {end_time - start_time} s\n", "info")
    output_text.insert(tk.END, f"Open ports: {open_ports}\n", "info")
    output_text.insert(tk.END, f"Total open ports: {len(open_ports)}\n", "info")

def clear_output():
    output_text.delete(1.0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Enhanced Port Scanner")
root.configure(bg="#f0f0f0")

# Center the window
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width / 2) - (window_width / 2)
y_coord = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coord)}+{int(y_coord)}")

# Styling
root.option_add("*Font", "TkDefaultFont 10")
root.option_add("*background", "#f0f0f0")
root.option_add("*foreground", "#333333")

# Labels and entries
target_label = tk.Label(root, text="Target:")
target_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
target_entry = tk.Entry(root, width=40)
target_entry.grid(row=0, column=1, padx=10, pady=5)

start_port_label = tk.Label(root, text="Start Port:")
start_port_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
start_port_entry = tk.Entry(root, width=15)
start_port_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)

end_port_label = tk.Label(root, text="End Port:")
end_port_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
end_port_entry = tk.Entry(root, width=15)
end_port_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

# Buttons
scan_button = tk.Button(root, text="Scan", command=scan_ports, bg="#4CAF50", fg="white", padx=15, pady=8)
scan_button.grid(row=3, column=0, columnspan=1, padx=10, pady=15)

clear_button = tk.Button(root, text="Clear", command=clear_output, bg="#f44336", fg="white", padx=15, pady=8)
clear_button.grid(row=3, column=1, columnspan=1, padx=10, pady=15)

# Output text
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=18, bg="#e0e0e0", fg="#222222")
output_text.grid(row=4, columnspan=2, padx=10, pady=10)

# Text tags for color
output_text.tag_config("header", foreground="#007bff", font=("TkDefaultFont", 10, "bold"))
output_text.tag_config("open", foreground="#28a745")
output_text.tag_config("info", foreground="#555555")

root.mainloop()
