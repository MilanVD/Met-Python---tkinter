import tkinter as tk
window = tk.Tk()

button = tk.Button(text='light switch', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
schakelaar = 0

def klik(event):
    global schakelaar
    if schakelaar == 0:
        print('Light is on...')
        button['text'] = 'The light switch is on...'
        window.configure(bg='red')
        schakelaar = 1
    else:
        print('Light is off...')
        button['text'] = 'The light switch is off'
        window.configure(bg='black')
        schakelaar = 0



button.bind("<Button>", klik)


# schijf hier tussen je code

window.mainloop()