from customtkinter import *

app = CTk()
app.title("Calculator")
app.config(bg = "#252422")
app.geometry("405x462")


line = ""


def adder(element):
    global line , result
    line += element
    if not(element.isdigit()):
        result.delete(0, END)
    else:
        result.insert(END, element)

def clear():
    global line, result
    result.delete(0, END)
    line = ""

    

def equal():
    global result, line
    try:
        endline = eval(line)
        result.delete(0, END)
        result.insert(END, endline)
    except:
        line = ""
        result.delete(0, END)
        result.insert(END, "Xato bo`ldi")
        
    
def special():
    global line , result
    line = line[:-1]
    m = result.get()
    m = m[:-1]
    result.delete(0, END)
    result.insert(END, m)
    
    
def specialsqrt():
    global line, result
    x = eval(line)
    x = x ** (1/2)
    result.delete(0, END)
    result.insert(END, x)
    line = str(x)



result = CTkEntry(app, width=358,corner_radius=35, height=63, bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ))
result.place(x = 23, y=40)


button7 = CTkButton(app,text="7" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("7"))
button7.place(x = 14, y = 142)
button8 = CTkButton(app,text="8" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("8"))
button8.place(x = 90, y = 142)
button9 = CTkButton(app,text="9" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("9"))
button9.place(x = 166, y = 142)
buttonbo = CTkButton(app,text="/" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command = lambda: adder("/"))
buttonbo.place(x = 242, y = 142)
buttonc = CTkButton(app,text="c" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=clear)
buttonc.place(x = 318, y =142 )
button4 = CTkButton(app,text="4" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("4"))
button4.place(x = 14, y =217 )
button5 = CTkButton(app,text="5" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("5"))
button5.place(x = 90, y = 217)
button6 = CTkButton(app,text="6" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("6"))
button6.place(x = 166, y = 217)
buttonko = CTkButton(app,text="*" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command = lambda: adder("*"))
buttonko.place(x = 242, y = 217)
buttonil = CTkButton(app,text="√" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=specialsqrt)
buttonil.place(x = 318, y = 217)
button1 = CTkButton(app,text="1" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("1"))
button1.place(x = 14, y = 292)
button2 = CTkButton(app,text="2" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("2"))
button2.place(x = 90, y = 292)
button3 = CTkButton(app,text="3" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("3"))
button3.place(x = 166, y = 292)
buttonmi = CTkButton(app,text="-" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command = lambda: adder("-"))
buttonmi.place(x = 242, y = 292)
buttonpow = CTkButton(app,text="<" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command= special)
buttonpow.place(x = 318, y = 292)
buttondot = CTkButton(app,text="." ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("."))
buttondot.place(x = 14, y = 367)
button0 = CTkButton(app,text="0" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("0"))
button0.place(x = 90, y = 367)
button00 = CTkButton(app,text="00" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command=lambda: adder("00"))
button00.place(x = 160, y = 367)
buttonp = CTkButton(app,text="+" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ), command = lambda: adder("+"))
buttonp.place(x = 242, y = 367)
buttonm = CTkButton(app,text="=" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ) , command = equal)
buttonm.place(x = 318, y = 367)





# button1 = CTkButton(app,text="7" ,width=30, height=56,corner_radius=56,  bg_color="#252422", fg_color="#ffffff", text_color="#252422" , font = ("Comic Sans MS", 15, "bold" ))

app.mainloop()