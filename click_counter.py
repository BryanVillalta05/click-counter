import tkinter as tk
import time
import matplotlib.pyplot as plt

wn = tk.Tk()
wn.title('Clicks per Second')
wn.geometry("300x400")
wn.resizable(0, 0)
clps = 0
t = 30
click_times = []
click_counts = []

def count():
    global clps
    clps += 1
    contador_lbl.config(text=str(clps))
    elapsed_time = time.time() - t_i
    click_times.append(elapsed_time)
    click_counts.append(clps)

def start():
    global t_i
    t_i = time.time()
    ck_btn.config(state="normal")
    start_btn.config(state="disabled")
    wn.after(int(t * 1000), finish)

def finish():
    ck_btn.config(state="disabled")
    generate_graph()

def generate_graph():
    plt.title("Clicks per second")
    plt.plot(click_times, click_counts)
    plt.xlabel('Time (s)')
    plt.ylabel('Clicks')
    plt.title('Clics per second')
    plt.show()

start_btn = tk.Button(wn, text="Start", font="Arial 30 bold", relief=tk.SOLID, border=3, command=start, activebackground='#345', bg="#ADA7A7")
start_btn.place(x=90, y=10)

ck_btn = tk.Button(wn, text="Click here", font="Arial 30 bold", relief=tk.SOLID, border=3, command=count, activebackground='#345', bg="#ADA7A7")
ck_btn.place(x=35, y=100)
ck_btn.config(state="disabled")

contador_lbl = tk.Label(wn, text="0", font="Arial 30 bold")
contador_lbl.place(x=140, y=200)

wn.mainloop()
