# tkButton
A simple solution to using styled tkinter buttons on MacOS
Since MacOS does not allow the styling of tkinter buttons, tkButton.Button() is an alternative to tkinter.Button() that does allow styling of buttons, similar to the Windows.

## Creating a tkButton
Just like the default tkinter button, the tkButton can be created as below:
```
button = tkButton.Button(root,text="hello world",bg="black",fg="white",width=100,height=20,font="Arial 12",command=hello_world
```
The button can then be added to the tkinter application using any of the default tkinter methods, for example:
```
button.place(anchor="center",relx=0.5,rely=0.5)
```

## Supported Options
The root parameter is the only required one and must be an instance of Tk() or tkinter.Frame(). All optional parameters serve the same function as they would in a tkinter.Button(), and they are listed below.

### Supported Optional Parameters
- text
- width
- height
- text
- bg
- fg
- font
- command

### Beta parameters:
- bordercolor
- bordersize
