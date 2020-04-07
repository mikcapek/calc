
import tkinter as tk

fields = ('Capital', 'Stoploss', 'Lotsize')

def makestuff(entries):
    r = (float(entries['Capital'].get()) / 100)
    stp = float(entries['Stoploss'].get())
    ls =  float(entries['Lotsize'].get())
   
    

def calculate():
    num = float(r/stp)
    if r or stp or ls == 0:
    	return 0
	
    if num < ls:
	    print(float(ls/num))
    if num > ls:
	    print(float(num/ls))




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




