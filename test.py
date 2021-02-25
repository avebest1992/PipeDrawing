import turtle
from tkinter import *
import os

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
# 便捷区函数
def whfd(x):
    '''无痕前进'''
    t.penup()
    t.forward(x)
    t.pendown()
def whgt(x, y):
    '''无痕移位by坐标'''
    t.penup()
    t.goto(x, y)
    t.pendown()
def whmv(pos):
    '''无痕移位by位置'''
    t.penup()
    t.goto(pos)
    t.pendown()
# 移动区函数
def change_button():
    '''点击切换坐标系'''
    if button_northeast['text'] =="北":
        button_northeast['text'] = "东"
        button_southeast['text'] = "南"
        button_southwest['text'] = "西"
        button_northwest['text'] = "北"
    else:
        button_northeast['text'] = "北"
        button_southeast['text'] = "东"
        button_southwest['text'] = "南"
        button_northwest['text'] = "西"
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
# 元件区函数
def falan():
    t.lt(90)
    t.fd(6)
    t.bk(12)
    t.rt(90)
    whfd(4)
    t.lt(90)
    t.fd(12)
    t.bk(6)
    t.rt(90)
def xiaofamen():
    t.left(90)
    t.fd(5)
    t.back(10)
    t.right(90)
    whfd(3)
    t.left(90)
    t.fd(10)
    t.right(120)
    t.fd(20)
    t.left(120)
    t.fd(10)
    t.left(120)
    t.fd(20)
    t.right(210)
    whfd(20.32)
    t.left(90)
    t.fd(10)
    t.back(5)
    t.right(90)
def dafamen():
    t.left(90)
    t.fd(10)
    t.back(20)
    t.right(90)
    whfd(3)
    t.left(90)
    t.fd(20)
    t.right(120)
    t.fd(40)
    t.left(120)
    t.fd(20)
    t.left(120)
    t.fd(40)
    t.right(210)
    whfd(37.64)
    t.left(90)
    t.fd(20)
    t.back(10)
    t.right(90)
def ltob():
    pos1 = t.pos()
    angle = t.heading()
    t.rt(90)
    t.fd(5)
    t.left(71.57)
    t.fd(15.81)
    t.left(108.43)
    t.fd(10)
    pos2 = t.pos()
    t.fd(10)
    t.left(108.43)
    t.fd(15.81)
    t.goto(pos1)
    whmv(pos2)
    t.seth(angle)
def btol():
    pos1 = t.pos()
    angle = t.heading()
    t.rt(90)
    t.fd(10)
    t.left(108.43)
    t.fd(15.81)
    t.left(71.57)
    t.fd(5)
    pos2 = t.pos()
    t.fd(5)
    t.left(71.57)
    t.fd(15.81)
    t.goto(pos1)
    whmv(pos2)
    t.seth(angle)
def yibiao():
    t.fd(10)
    xiaofamen()
    t.fd(10)
    t.rt(90)
    t.circle(7)
    t.lt(90)
    whfd(14)
def gang():
    t.left(90)
    t.fd(7)
    t.back(14)
    t.fd(7)
    t.right(90)
def quan():
    pos = t.pos()
    t.back(5)
    t.right(90)
    t.circle(5)
    whmv(pos)
# def finish():
#     falan()
#     t.hideturtle()
# 功能区函数
def biaoti():
    word = theScreen.textinput("标题","请输入标题内容")
    t.write(word,align='center',font=("宋体",20,"bold"))
def daduan():
    t.fd(15)
    whfd(10)
    t.fd(15)
def long():
    length = theScreen.numinput("远距离","输入长度（目前每一步是20）")
    t.fd(length)
def start(event):
    x, y = event.x-476, -event.y+351
    whgt(x, y)
    root.unbind("<Button-1>")
def new():
    root.bind("<Button-1>", start)
def save():
    os.startfile("snip.exe")
def word_action(event):
    x, y = event.x-476, -event.y+351
    whgt(x, y)
    root.unbind("<Button-1>")
    word = theScreen.textinput("添加文字", "请输入要添加的文字")
    t.write(word, align='center', font=("宋体", 10))
def new_word():
    root.bind("<Button-1>", word_action)


# 移动按键区
photo = PhotoImage(file="six.gif")
label_photo = Label(root, image=photo, borderwidth=0)
label_photo.place(x=741, y=615, anchor='center')
button_change_button = Button(root, text="更改坐标方向", command=change_button).pack(side='right')
button_northeast = Button(root, text='北', command=northeast)
button_southeast = Button(root, text='东', command=southeast)
button_southwest = Button(root, text='南', command=southwest)
button_northwest = Button(root, text='西', command=northwest)
button_northwest.place(x=663, y=560)
button_northeast.place(x=791, y=560)
button_southeast.place(x=791, y=633)
button_southwest.place(x=663, y=633)
button_up = Button(root, text='上', command=up)
button_up.place(x=726, y=520)
button_down = Button(root, text='下', command=down)
button_down.place(x=726, y=673)
# 功能按键区
button_new_word=Button(root, text="添加文字", command=new_word).place(x=865, y=430)
button_new=Button(root, text="新起点", command=new).place(x=865, y=465)
button_biaoti = Button(root, text='点击添加标题（先用新起点设定位置）',command=biaoti).pack()
button_long = Button(root, text="远距离", command=long).place(x=865, y=500)
button_daduan = Button(root, text="打断", command=daduan).place(x=865, y=535)
button_undo = Button(root, text='撤销', command=t.undo).place(x=865, y=570)
button_clear = Button(root, text="清屏", command=t.clear).place(x=865, y=605)
button_hide = Button(root, text='隐藏', command=t.hideturtle).place(x=865, y=640)
button_show = Button(root, text='显示', command=t.showturtle).place(x=900, y=640)
button_save=Button(root, text='保存',command=save).place(x=865, y=675)
# 元件符号区
button_falan = Button(root, text='法兰', command=falan).place(x=100, y=670)
button_xiaofamen = Button(root, text='小阀', command=xiaofamen).place(x=150, y=670)
button_dafamen = Button(root, text='大阀', command=dafamen).place(x=150, y=640)
button_ltob = Button(root, text="小大",command=ltob).place(x=200, y=670)
button_btol = Button(root, text="大小",command=btol).place(x=200, y=640)
button_yibiao = Button(root, text="仪表", command=yibiao).place(x=250, y=670)
button_gang = Button(root, text='画杠', command=gang).place(x=300, y=640)
button_quan = Button(root, text='画圈', command=quan).place(x=300, y=670)
# 逻辑结束
theScreen.mainloop()
root.mainloop()
