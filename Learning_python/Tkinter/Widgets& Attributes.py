"""                                         Widgets & Attributes                        """

"""   Tkinter Widgets :   """                       """               Attributes              """

"""
Button                                                                  Dimension            
Canvas                                                                  Colors
Checkbutton                                                             Fonts
Entry                                                                   Anchors
Frame                                                                   Relief styles
Label                                                                   Bitmaps
Listbox                                                                 Cursors
Menubutton
Menu
Message
Radiobutton                                   "Geometry Management"
Scale                                             Pack , Grid, Place where place Elements.
Scrolbar
Text
Toplevel
Spinbox
PanedWindows
LabelFrame
tkMessageBox
"""
"""How to create First GUI """
  

""" imoprting lib of tkinter by Two ways is 
import tkinter as tk   
from tkinter import *


|| Creating  Window
  
    import tkinter as tk
    win = tk.Tk()
    win.mainloop()

    from tkinter import *
    win = TK()
    win.mainloop()

|| Changing in Tkinter Windows like: Title, Transparency, Default icon, Background_color

    from tkinter import *
    win = Tk()
    win.title("*** Hacker ****")
    win.iconbitmap("location\ Name_of_Image)
    win.attributes('alpha', 0.5) // transpancy of windows
    win.config(bg="red") || Change background colour
    win['bg]="yellow || Change background colour 

|| Chnaging Size and Location of windows
    from tkinter import *
    win= TK()
    win.title("Hacker"
    win.gemoetry("300x500") ||  min and max size of windows
    
    //Setting min and max size fixed

    win.minsize(100,100)
    win.maxsize(500,500)

    // Fixed resizable of the windows
     
    win.resizable(False,False)

    win.gemoetry("300x500+100+100) location of the windows
    win.mainloop()
|| How widnows in Center

    win = Tk()
     width = 300
     height = 500
     sys_width = win.winfo_screenwidth()
     sys_width = win.winfo_screenheight()
     c_x = int(sys_width/2 - width/2)
     C_Y = int(sys_heigth/2 -height/2)

    win.gemoetry(f"{width}x{heigth)+{c_x]+C_y}")
    win = mainloop()
    
||| Layout Management |||

pack -- fill, expand, side, ipadx, ipady, padx, and pady.

lab =Label(win, text ="Hacker", font





"""