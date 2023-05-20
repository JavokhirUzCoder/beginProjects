from tkinter import *
root = Tk()
root.title( "Python code editor")
root.geometry("700x700")
# App size and simple values

#Main function
def MainFunc():
    code = inputArea.get(1.0, "end-1c")


    # output code
    # codeee = exec(code)

    import sys
    from io import StringIO
    import contextlib

    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    with stdoutIO() as s:
        try:
            exec(code)
        except:
            print("Something wrong with the code")

    outputArea.delete(1.0, END)
    outputArea.insert("end-1c", str(s.getvalue()))
    
    
textAlert = Label(text = "Enter the your python codes")
textAlert.pack()
inputArea = Text(root,
                 height = 20,
                 width = 50,
                 fg = "green",)
inputArea.pack()

buttonForRun = Button(root,
                       height = 3,
                        width = 10,
                        text = "Run",
                        bg = "red",
                        fg = "white",
                        activebackground='blue',
                        activeforeground='white',
                        borderwidth=3,
                        relief="solid",
                        command = MainFunc)
buttonForRun.pack()

outputArea = Text(root, height = 20, width = 50)
outputArea.pack()




mainloop()