import turtle
from tkinter import *

# 初始化屏幕、画布、画笔
root = Tk()
root.title('单线图绘制-By 周啸天')
root.geometry('950x700+0+0')
canva = Canvas(root, width=950, height=700)
canva.place(x=0,y=0)
theScreen = turtle.TurtleScreen(canva)
t = turtle.RawTurtle(theScreen)
# 初始化龟龟位置
t.speed(0)
t.penup()
t.setpos(-350, -100)
t.pendown()

def northeast():
    t.seth(30)
    t.fd(20)
def up():
    t.seth(90)
    t.fd(20)
def northwest():
    t.seth(150)
    t.fd(20)
def southwest():
    t.seth(210)
    t.fd(20)
def down():
    t.seth(270)
    t.fd(20)
def southeast():
    t.seth(330)
    t.fd(20)
def falan():
    t.lt(90)
    t.fd(5)
    t.bk(10)
    t.penup()
    t.rt(90)
    t.fd(3)
    t.lt(90)
    t.pendown()
    t.fd(10)
    t.bk(5)
    t.rt(90)
def famen():
    t.left(90)
    t.fd(5)
    t.back(10)
    t.penup()
    t.right(90)
    t.fd(3)
    t.left(90)
    t.pendown()
    t.fd(10)
    t.right(120)
    t.fd(20)
    t.left(120)
    t.fd(10)
    t.left(120)
    t.fd(20)
    t.penup()
    t.right(210)
    t.fd(20.32)
    t.left(90)
    t.pendown()
    t.fd(10)
    t.back(5)
    t.right(90)
# def finish():
#     falan()
#     t.hideturtle()
def biaoti():
    word = theScreen.textinput("标题","请输入标题内容")
    pos = t.pos()
    t.penup()
    t.setposition(0,250)
    t.pendown()
    t.write(word,align='center',font=("宋体",20,"bold"))
    t.penup()
    t.setposition(pos)
    t.pendown()
def daduan():
    t.fd(15)
    t.penup()
    t.fd(10)
    t.pendown()
    t.fd(15)
def long():
    length = theScreen.numinput("远距离","输入长度（目前每一步是20）")
    t.fd(length)


# 移动按键区
photo = PhotoImage(file="six.gif")
label_photo = Label(root, image=photo, borderwidth=0)
label_photo.place(x=741, y=615, anchor='center')
button_northwest = Button(root, text='西', command=northwest)
button_northwest.place(x=663, y=560)
button_up = Button(root, text='上', command=up)
button_up.place(x=726, y=520)
button_northeast = Button(root, text='北', command=northeast)
button_northeast.place(x=791, y=560)
button_southeast = Button(root, text='东', command=southeast)
button_southeast.place(x=791, y=633)
button_down = Button(root, text='下', command=down)
button_down.place(x=726, y=673)
button_southwest = Button(root, text='南', command=southwest)
button_southwest.place(x=663, y=633)
# 功能按键区
button_biaoti = Button(root, text='点击添加标题',command=biaoti).pack()
button_long = Button(root, text="远距离", command=long).place(x=865, y=500)
button_daduan = Button(root, text="打断", command=daduan).place(x=865, y=530)
button_undo = Button(root, text='撤销', command=t.undo).place(x=865, y=560)
button_finish = Button(root, text='结束', command=t.hideturtle).place(x=865, y=600)
# 元件符号区
button_falan = Button(root, text='法兰', command=falan)
button_falan.place(x=530, y=670)
button_famen = Button(root, text='阀门', command=famen)
button_famen.place(x=470, y=670)




theScreen.mainloop()
root.mainloop()
