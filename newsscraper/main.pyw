import tkinter as tk
import newsscraper as ns
def gui():
    window = tk.Tk()
    window.geometry("")
    window.title("headline aggregation")
    tk.Label(
        window,
        text="please enter the keyword you would like to see  BBC headlines for:"
    ).grid(row=0, sticky="w")
    key_ent = tk.Entry(window)
    key_ent.grid(row=0, column=1, sticky="w")
    def get_arts():
        key = key_ent.get()
        heads = ns.scrape(key)
        if len(heads) > 0:
            for i in range(0,len(heads)):
                tk.Label(window,text= heads[i]).grid(row=2 + i, sticky="w")
        else:
            tk.Label(window, text = "No articles found.").grid(row = 2, sticky = "w")
    tk.Button(text="search",command=get_arts).grid(row=1, column=1)
    return window
if __name__ == "__main__":
    gui = gui()
    gui.mainloop()