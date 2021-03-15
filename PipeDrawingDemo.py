import turtle
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageTk
import os, time
from sys import exit
from tkinter import ttk

"""初始化屏幕、画布、画笔"""
root = Tk()
root.title('单线图绘制-By 周啸天')
root.geometry('950x700+0+0')
canva = Canvas(root, width=950, height=700)
canva.pack()
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
location = []
location_count = 0
location_id = []
def set_location():
    global location, location_id
    location.append(t.pos())
    t.shape('turtle')
    t.color('blue')
    stampid = t.stamp()
    location_id.append(stampid)
    t.color('black')
    t.shape('classic')


def goto_location():
    global location, location_count
    if len(location) == 0:
        tkinter.messagebox.showinfo(title="提示",message="现在还没有定位，点击编辑菜单->添加定位")
    elif location_count<len(location):
        whgt(location[location_count])
        location_count += 1
    else:
        location_count = 1
        whgt(location[0])


def clear_location():
    global location, location_count, location_id
    for i in range(len(location_id)):
        t.clearstamp(location_id[i])
    location.clear()
    location_count = 0
    location_id.clear()

word_ne, word_se, word_sw, word_nw = "北", "东", "南", "西"
def change_button():
    # 点击切换坐标系
    global word_ne, word_se, word_sw, word_nw
    temp = word_ne
    word_ne = word_se
    word_se = word_sw
    word_sw = word_nw
    word_nw = temp
    button_northeast.config(text=word_ne+'E')
    button_southeast.config(text=word_se+'D')
    button_southwest.config(text=word_sw+'A')
    button_northwest.config(text=word_nw+'Q')


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
    t.fd(3)
    t.left(71.57)
    t.fd(9.49)
    t.left(108.43)
    t.fd(12)
    t.left(108.43)
    t.fd(9.49)
    t.left(71.57)
    t.fd(3)
    t.left(90)
    whfd(9)


def btol():
    t.rt(90)
    t.fd(6)
    t.left(108.43)
    t.fd(9.49)
    t.left(71.57)
    t.fd(6)
    t.left(71.57)
    t.fd(9.49)
    t.left(108.43)
    t.fd(6)
    t.left(90)
    whfd(9)


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


def daduan():
    t.fd(15)
    whfd(10)
    t.fd(15)


"""功能区函数"""
def biaoti_action(event):
    x, y = event.x - 476, -event.y + 351
    whgt(x, y)
    root.unbind("<Button-1>")
    word = theScreen.textinput("标题", "请输入标题内容")
    t.write(word, align='center', font=("宋体", 20, "bold"))
    canva['cursor'] = 'arrow'


def biaoti():
    root.bind("<Button-1>", biaoti_action)
    canva['cursor'] = 'crosshair'


image_tb_inserted = None
im = None
def insert_image():
    global image_tobe_inserted,im
    file_path = tkinter.filedialog.askopenfilename(title="选择要插入的图片")
    x, y = t.xcor(), -t.ycor()
    image_tb_inserted = Image.open(file_path)
    im = ImageTk.PhotoImage(image_tb_inserted)
    canva.create_image(x, y, image=im)


def eraser():
    # TODO function eraser
    pass


def long():
    length = theScreen.numinput("远距离", "输入长度（目前每一步是20）")
    t.fd(length)


def new_action(event):
    x, y = event.x - 476, -event.y + 351
    whgt(x, y)
    root.unbind("<Button-1>")
    canva['cursor'] = 'arrow'


def new(event=None):
    root.bind("<Button-1>", new_action)
    canva['cursor'] = 'crosshair'


def save(event=None):
    time.sleep(0.2)
    os.startfile(get_resource_path("snip.exe"))


def quit(event=None):
    answer = tkinter.messagebox.askyesnocancel(title="正在关闭程序", message="是否现在保存？")
    if answer == True:
        save()
    elif answer == False:
        exit()
    else:
        return


new_word_size = 12
def change_word_size():
    global new_word_size
    new_word_size = int(theScreen.numinput(title="更改字号",prompt=f"请输入字号（当前是{new_word_size}）：",default=12))


def new_word_action(event):
    x, y = event.x - 475.00, -event.y + 350.00
    whgt(x, y)
    root.unbind("<Button-1>")
    global new_word_size
    word = theScreen.textinput("添加文字", "请输入要添加的文字")
    t.write(word, align='center', font=("宋体", new_word_size, 'normal'))
    canva['cursor'] = 'arrow'


def new_word(event=None):
    root.bind("<Button-1>", new_word_action)
    canva['cursor'] = 'crosshair'


def manual_action(event):
    x, y = event.x - 476, -event.y + 351
    t.goto(x, y)
    root.unbind("<Button-1>")
    canva['cursor'] = 'arrow'


def manual():
    root.bind("<Button-1>", manual_action)
    canva['cursor'] = 'crosshair'


def help():
    os.startfile(get_resource_path("使用说明.txt"))


def senior():
    senior_window = tkinter.Toplevel()
    turtle_coordinate_pic = Image.open(get_resource_path(r"icons\t_coor.png"))
    t_coor = ImageTk.PhotoImage(turtle_coordinate_pic)
    canvas_coor = tkinter.Canvas(senior_window,width=turtle_coordinate_pic.width,height=turtle_coordinate_pic.height)
    canvas_coor.create_image(0,0,image=t_coor,anchor="nw")
    canvas_coor.pack()
    senior_window.mainloop()


"""顶部菜单区"""
menubar = Menu(root)
root.config(menu=menubar)
menu_files = Menu(menubar, tearoff=0)
menu_files.add_command(label="导入图片", command=insert_image)
menu_files.add_command(label="保 存", command=save,accelerator='Ctrl+S')
menu_files.add_command(label="退 出", command=quit, accelerator='Ctrl+Q')
menubar.add_cascade(label="文 件", menu=menu_files)
menu_edit = Menu(menubar, tearoff=1)
menu_edit.add_command(label="点击上方虚线可取出菜单")
menu_edit.add_separator()
menu_edit.add_command(label="清 屏", command=t.clear)
menu_edit.add_command(label="更改坐标", command=change_button)
menu_edit.add_separator()
menu_edit.add_command(label="隐藏箭头", command=t.hideturtle)
menu_edit.add_command(label="显示箭头", command=t.showturtle)
menu_edit.add_separator()
menu_edit.add_command(label="添加标题",command=biaoti)
menu_edit.add_command(label="添加文字",command=new_word, accelerator='Ctrl+W')
menu_edit.add_command(label="更改字号",command=change_word_size)
menu_edit.add_separator()
menu_edit.add_command(label="新起点",command=new, accelerator='Ctrl+X')
menu_edit.add_command(label="远距离",command=long)
menu_edit.add_separator()
menu_edit.add_command(label="撤 销",command=t.undo, accelerator='Ctrl+Z')
menu_edit.add_separator()
menu_edit.add_command(label="添加标记",command=set_location)
menu_edit.add_command(label="定位标记",command=goto_location)
menu_edit.add_command(label="清除标记",command=clear_location)
menubar.add_cascade(label="编 辑", menu=menu_edit)
menu_help = Menu(menubar, tearoff=0)
menu_help.add_command(label="使用说明",command=help)
menu_help.add_command(label="高级模式",command=senior)
menubar.add_cascade(label="帮 助", menu=menu_help)
# 快捷键绑定区
root.bind("<Control-s>", save)
root.bind("<Control-q>", quit)
root.bind("<Control-w>", new_word)
root.bind("<Control-x>", lambda event:new())
root.bind("<Control-z>", lambda event:t.undo())
root.bind("<w>", lambda event:up())
root.bind("<s>", lambda event:down())
root.bind("<e>", lambda event:northeast())
root.bind("<d>", lambda event:southeast())
root.bind("<a>", lambda event:southwest())
root.bind("<q>", lambda event:northwest())
"""移动按键区"""
# 更改坐标
# button_change_button = Button(root, text="更改坐标方向", command=change_button, relief='groove').pack(side='right')
# 坐标框架
# frame_move = Frame(canva,bg="red",relief="groove",height=150,width=150)
# frame_move.place(relx=0.8,rely=0,anchor="center")
# 坐标图片
photo_six = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\six.jpg")))
label_photo = Label(canva, image=photo_six, borderwidth=0)
label_photo.place(x=600,y=600,anchor='center')
# 方向按钮
# ttk.Style().configure("TButton", width=3, relief="groove",background="white",font=(10))
# button_northeast = ttk.Button(canva, text='北', command=northeast)
button_northeast = Button(canva, text=word_ne+'E', command=northeast, relief='groove',width=3,bg='white')
button_southeast = Button(canva, text=word_se+'D', command=southeast, relief='groove',width=3,bg='white')
button_southwest = Button(canva, text=word_sw+'A', command=southwest, relief='groove',width=3,bg='white')
button_northwest = Button(canva, text=word_nw+'Q', command=northwest, relief='groove',width=3,bg='white')
button_up = Button(canva, text='上W', command=up, relief='groove',width=3,bg='white')
button_down = Button(canva, text='下S', command=down, relief='groove',width=3,bg='white')
button_northeast.place(x=634, y=565)
button_southeast.place(x=634, y=605)
button_southwest.place(x=533, y=605)
button_northwest.place(x=533, y=565)
button_up.place(x=584, y=530)
button_down.place(x=584, y=640)
"""功能按键区"""
# button_new_word = Button(root, text="添加文字", command=new_word, relief='groove').place(x=865, y=430)
# button_new = Button(root, text="新起点", command=new, relief='groove').place(x=865, y=465)
# button_biaoti = Button(root, text='点击添加标题（先用新起点设定位置）', command=biaoti, relief='groove').pack()
# button_long = Button(root, text="远距离", command=long, relief='groove').place(x=865, y=500)
# button_undo = Button(root, text='撤销', command=t.undo, relief='groove').place(x=865, y=570)
# button_clear = Button(root, text="清屏", command=t.clear, relief='groove').place(x=865, y=605)
# button_hide = Button(root, text='隐藏', command=t.hideturtle, relief='groove').place(x=865, y=640)
# button_show = Button(root, text='显示', command=t.showturtle, relief='groove').place(x=900, y=640)
# button_save = Button(root, text='保存', command=save, relief='groove').place(x=865, y=675)
# button_insert_image = Button(root, text="插图", command=insert_image, relief='groove').place(x=900, y=675)
"""元件符号区"""
frame_components = Frame(canva,borderwidth=1,bg='white',relief='groove')
frame_components.place(x=100, y=600)
# 起止符号
icon_shape_s = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_shape_s.jpg")))
button_shape_s = Button(frame_components, image=icon_shape_s, command=shape_s, relief='groove').grid(row=0,column=0, padx=3)
# 法兰
icon_falan = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_falan.jpg")))
button_falan = Button(frame_components, image=icon_falan, command=falan, relief='groove').grid(row=1,column=0, padx=3)
# 异径管
icon_btol = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_btol.jpg")))
button_btol = Button(frame_components, image=icon_btol, command=btol, relief='groove').grid(row=0,column=1, padx=3)
icon_ltob = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_ltob.jpg")))
button_ltob = Button(frame_components, image=icon_ltob, command=ltob, relief='groove').grid(row=1,column=1, padx=3)
# 测厚杠圈
icon_gang = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_gang.jpg")))
button_gang = Button(frame_components, image=icon_gang, command=gang, relief='groove').grid(row=0,column=2, padx=3)
icon_quan = ImageTk.PhotoImage(Image.open(get_resource_path(r"icons\icon_quan.jpg")))
button_quan = Button(frame_components, image=icon_quan, command=quan, relief='groove').grid(row=1,column=2, padx=3)
# 阀门
button_xiaofamen = Button(frame_components, text='小阀', command=xiaofamen, relief='groove',bg='white').grid(row=0,column=3, padx=3)
button_dafamen = Button(frame_components, text='大阀', command=dafamen, relief='groove',bg='white').grid(row=1,column=3, padx=3)
# 仪表
button_yibiao = Button(frame_components, text="仪表", command=yibiao, relief='groove',bg='white').grid(row=0,column=4, padx=3)
# 打断
button_daduan = Button(frame_components, text="打断", command=daduan, relief='groove',bg='white').grid(row=1,column=4, padx=3)
# 盖章
button_stamp = Button(frame_components, text="流向", command=t.stamp, relief='groove',bg='white').grid(row=0,column=5, padx=3,sticky='w')
# 手动施法
button_manual = Button(frame_components, text="手动施法", command=manual, relief='groove',bg='white').grid(row=1,column=5, padx=3)
"""逻辑结束"""
# ttk.Style().configure("TButton", width=2, relief="groove",background="white")
# button_test = ttk.Button(canva,text="上").place(x=500,y=500)
theScreen.mainloop()
root.mainloop()
