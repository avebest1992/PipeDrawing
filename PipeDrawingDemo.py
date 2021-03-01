import turtle
from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk
import os

"""初始化屏幕、画布、画笔"""
root = Tk()
root.title('单线图绘制-By 周啸天')
root.geometry('950x700+0+0')
canva = Canvas(root, width=950, height=700)
canva.place(x=0, y=0)
theScreen = turtle.TurtleScreen(canva)
t = turtle.RawTurtle(theScreen)
# 初始化龟龟位置
t.speed(0)
t.penup()
t.setpos(-350, -100)
t.pendown()


"""便捷区函数"""
def get_resource_path(relative_path):
    """打包exe时资源文件的路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def whfd(x):
    # 无痕前进
    t.penup()
    t.forward(x)
    t.pendown()


def whgt(x, y=None):
    # 无痕移位by位置
    t.penup()
    t.goto(x, y)
    t.pendown()


"""移动区函数"""
def change_button():
    # 点击切换坐标系
    temp = button_northeast['text']
    button_northeast['text'] = button_southeast['text']
    button_southeast['text'] = button_southwest['text']
    button_southwest['text'] = button_northwest['text']
    button_northwest['text'] = temp


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


"""元件区函数"""
def gang(x=7):
    t.left(90)
    t.fd(x)
    t.back(2 * x)
    t.fd(x)
    t.right(90)


def falan():
    gang()
    whfd(5)
    gang()


def shape_s():
    t.penup()
    t.circle(5, 210)
    t.pendown()
    t.circle(5, 150)
    t.circle(-5, 150)
    t.penup()
    t.circle(-5, 210)
    t.pendown()


def xiaofamen():
    gang(5)
    whfd(3)
    t.left(90)
    t.fd(5)
    t.right(120)
    t.fd(10)
    pos1 = t.pos()
    t.fd(10)
    t.left(120)
    t.fd(10)
    t.left(120)
    t.fd(20)
    t.right(120)
    t.fd(5)
    t.right(90)
    whfd(20.32)
    pos2 = t.pos()
    gang(5)
    whgt(pos1)
    t.left(90)
    t.fd(12)
    gang(5)
    whgt(pos2)
    t.right(90)


def dafamen():
    gang(10)
    whfd(4)
    t.left(90)
    t.fd(10)
    t.right(120)
    t.fd(20)
    pos1 = t.pos()
    t.fd(20)
    t.left(120)
    t.fd(20)
    t.left(120)
    t.fd(40)
    t.right(120)
    t.fd(10)
    t.right(90)
    whfd(39.64)
    pos2 = t.pos()
    gang(10)
    whgt(pos1)
    t.left(90)
    t.fd(24)
    gang(10)
    whgt(pos2)
    t.right(90)


def ltob():
    t.rt(90)
    t.fd(5)
    t.left(71.57)
    t.fd(15.81)
    t.left(108.43)
    t.fd(20)
    t.left(108.43)
    t.fd(15.81)
    t.left(71.57)
    t.fd(5)
    t.left(90)
    whfd(15)


def btol():
    t.rt(90)
    t.fd(10)
    t.left(108.43)
    t.fd(15.81)
    t.left(71.57)
    t.fd(10)
    t.left(71.57)
    t.fd(15.81)
    t.left(108.43)
    t.fd(10)
    t.left(90)
    whfd(15)


def yibiao():
    xiaofamen()
    angle = t.heading()
    t.fd(10)
    t.rt(90)
    t.circle(7)
    t.circle(7, 90-angle)
    word = theScreen.textinput("添加文字", "请输入字母")
    t.write(word, align='center', font=("宋体", 10, 'normal'))


def quan():
    pos = t.pos()
    t.back(5)
    t.right(90)
    t.circle(5)
    whgt(pos)


"""功能区函数"""
def biaoti():
    word = theScreen.textinput("标题", "请输入标题内容")
    t.write(word, align='center', font=("宋体", 20, "bold"))

image_tb_inserted = None
im = None
def insert_image():
    global image_tobe_inserted,im
    file_path = tkinter.filedialog.askopenfilename(title="选择要插入的图片")
    x, y = t.xcor(), -t.ycor()
    image_tb_inserted = Image.open(file_path)
    im = ImageTk.PhotoImage(image_tb_inserted)
    canva.create_image(x, y, image=im)


def daduan():
    t.fd(15)
    whfd(10)
    t.fd(15)


def eraser():
    # TODO function eraser
    pass


def long():
    length = theScreen.numinput("远距离", "输入长度（目前每一步是20）")
    t.fd(length)


def start(event):
    x, y = event.x - 476, -event.y + 351
    whgt(x, y)
    root.unbind("<Button-1>")
    canva['cursor'] = 'arrow'


def new():
    root.bind("<Button-1>", start)
    canva['cursor'] = 'crosshair'


def save():
    os.startfile(get_resource_path("snip.exe"))


def word_action(event):
    x, y = event.x - 476, -event.y + 351
    whgt(x, y)
    root.unbind("<Button-1>")
    word = theScreen.textinput("添加文字", "请输入要添加的文字")
    t.write(word, align='center', font=("宋体", 10, 'normal'))
    canva['cursor'] = 'arrow'


def new_word():
    root.bind("<Button-1>", word_action)
    canva['cursor'] = 'crosshair'


def manual_action(event):
    x, y = event.x - 476, -event.y + 351
    t.goto(x, y)
    root.unbind("<Button-1>")
    canva['cursor'] = 'arrow'


def manual():
    root.bind("<Button-1>", manual_action)
    canva['cursor'] = 'crosshair'


"""移动按键区"""
# 坐标图片
photo = PhotoImage(file=get_resource_path("six.gif"))
label_photo = Label(root, image=photo, borderwidth=0)
label_photo.place(x=741, y=615, anchor='center')
# 更改坐标
button_change_button = Button(root, text="更改坐标方向", command=change_button).pack(side='right')
# 手动施法
button_manual = Button(root, text="手动施法", command=manual).place(x=0, y=670)
# 方向按钮
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
"""功能按键区"""
button_new_word = Button(root, text="添加文字", command=new_word).place(x=865, y=430)
button_new = Button(root, text="新起点", command=new).place(x=865, y=465)
button_biaoti = Button(root, text='点击添加标题（先用新起点设定位置）', command=biaoti).pack()
button_long = Button(root, text="远距离", command=long).place(x=865, y=500)
button_undo = Button(root, text='撤销', command=t.undo).place(x=865, y=570)
button_clear = Button(root, text="清屏", command=t.clear).place(x=865, y=605)
button_hide = Button(root, text='隐藏', command=t.hideturtle).place(x=865, y=640)
button_show = Button(root, text='显示', command=t.showturtle).place(x=900, y=640)
button_save = Button(root, text='保存', command=save).place(x=865, y=675)
button_insert_image = Button(root, text="插图", command=insert_image).place(x=900, y=675)
"""元件符号区"""
# 起止符号
icon_shape_s = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_shape_s.jpg")))
button_shape_s = Button(root, image=icon_shape_s, command=shape_s).place(x=100, y=640)
# 法兰
icon_falan = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_falan.jpg")))
button_falan = Button(root, image=icon_falan, command=falan).place(x=100, y=670)
# 异径管
icon_btol = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_btol.jpg")))
button_btol = Button(root, image=icon_btol, command=btol).place(x=150, y=640)
icon_ltob = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_ltob.jpg")))
button_ltob = Button(root, image=icon_ltob, command=ltob).place(x=150, y=670)
# 测厚杠圈
icon_gang = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_gang.jpg")))
button_gang = Button(root, image=icon_gang, command=gang).place(x=200, y=640)
icon_quan = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_quan.jpg")))
button_quan = Button(root, image=icon_quan, command=quan).place(x=200, y=670)
# 阀门
button_xiaofamen = Button(root, text='小阀', command=xiaofamen).place(x=250, y=670)
button_dafamen = Button(root, text='大阀', command=dafamen).place(x=250, y=640)
# 仪表
button_yibiao = Button(root, text="仪表", command=yibiao).place(x=300, y=640)
# 打断
button_daduan = Button(root, text="打断", command=daduan).place(x=300, y=670)
"""逻辑结束"""
theScreen.mainloop()
root.mainloop()
