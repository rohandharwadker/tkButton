import tkinter as tk

class Button():
    button_frame = None
    root = None
    width=100
    height=20
    text=""
    bg="white"
    fg="black"
    font="f 12"
    bordercolor = "black"
    bordersize = 3
    label = None
    command = None

    def __init__(self,root,width=100,height=20,text="",bg="white",fg="black",font="f 12",command=None,bordercolor="black",bordersize=0):
        self.root = root
        self.width=width
        self.height=height
        self.text=text
        self.bg=bg
        self.fg=fg
        self.font=font
        self.command = command
        self.bordercolor = bordercolor
        self.bordersize = bordersize
        self.button_frame = tk.Frame(root,width=width,height=height,bg=bg)
        self.label = tk.Label(self.button_frame,text=self.text,bg=self.bg,width=self.width,height=self.height,fg=self.fg,font=self.font,highlightbackground=self.bordercolor,highlightthickness=self.bordersize)
        self.label.place(anchor="center",relx=0.5,rely=0.5,relheight=1,relwidth=1)
        self.label.bind("<Button-1>",self.call_command)

    def call_command(self,event):
        if (self.command != None):
            self.command()
    
    def place(self,anchor="nw",relx=0,rely=0):
        self.button_frame.place(anchor=anchor,relx=relx,rely=rely)

    def configure(self,width=width,height=height,text=text,bg=bg,fg=fg,font=font,command=command,bordercolor=bordercolor,bordersize=bordersize):
        self.button_frame.configure(width=width,height=height,bg=bg)
        self.label.configure(text=text,bg=bg,width=width,height=height,fg=fg,font=font,highlightbackground=bordercolor,highlightthickness=bordersize)
        self.command = command