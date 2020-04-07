
# from currency_converter import CurrencyConverter

import tkinter as tk

# c = CurrencyConverter()

fields = ('Capital', 'Stoploss', 'Lotsize', 'Amount')

    

def calculate(entries):
    r = (float(entries['Capital'].get()) / 100)
    # d = c.convert(r, 'CZK', 'USD')
    stp = float(entries['Stoploss'].get())
    ls =  float(entries['Lotsize'].get())
    
    num = float((r/stp)/10)
    entries['Amount'].delete(0, tk.END)
    entries['Amount'].insert(0, "%.2f" % num)
    if r or stp or ls == 0:
        return 0
	
    



def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='How much?',
           command=(lambda e=ents: calculate(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    
    root.mainloop()




