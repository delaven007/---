#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/19 10:33
@File    : peppapig.py
@Author  : frank.chang@shoufuyou.com

https://docs.python.org/zh-cn/3/library/turtle.html
https://docs.python.org/zh-cn/3/library/turtle.html#turtle.color
https://docs.python.org/zh-cn/3/library/turtle.html#turtle.write
https://docs.python.org/zh-cn/3/library/turtle.html#turtle.pencolor
https://mp.weixin.qq.com/s/bdTK4HrAw5sNgIfAzP-F8g
"""

import turtle


def nose(x, y):  # 鼻子
    turtle.penup()  # 提起笔
    turtle.goto(x, y)  # 定位
    turtle.pendown()  # 落笔，开始画

    # 将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    turtle.setheading(-30)
    turtle.begin_fill()  # 准备开始填充图形
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.left(3)  # 向左转3度
            turtle.forward(a)  # 向前走a的步长
        else:
            a = a - 0.08
            turtle.left(3)
            turtle.forward(a)
    turtle.end_fill()  # 填充完成

    turtle.penup()
    turtle.setheading(90)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(10)
    turtle.pendown()
    turtle.pencolor(255, 155, 192)  # 画笔颜色
    turtle.setheading(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)  # 返回或设置pencolor和fillcolor
    turtle.end_fill()

    turtle.penup()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.pendown()
    turtle.pencolor(255, 155, 192)
    turtle.setheading(10)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.color(160, 82, 45)
    turtle.end_fill()


def head(x, y):  # 头
    turtle.color((255, 155, 192), "pink")
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(180)
    turtle.circle(300, -30)
    turtle.circle(100, -60)

    turtle.circle(80, -100)
    turtle.circle(150, -20)
    turtle.circle(60, -95)
    turtle.setheading(161)
    turtle.circle(-300, 15)
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    turtle.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            turtle.lt(3)  # 向左转3度
            turtle.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            turtle.lt(3)
            turtle.fd(a)
    turtle.end_fill()


def cheek(x, y):  # 腮

    # 深红色
    turtle.color((255, 155, 192))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()


def mouth(x, y):  # 嘴
    # 保存画笔的属性
    pen = turtle.pen()

    turtle.color(239, 69, 19)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-80)
    turtle.circle(30, 40)
    turtle.circle(40, 80)

    # 还原画笔属性
    turtle.pen(pen)


def setting():  # 参数设置
    turtle.pensize(5)
    turtle.showturtle()  # 使乌龟无形（隐藏）
    turtle.colormode(255)  # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    turtle.color((255, 155, 192), "pink")
    # turtle.setup(840, 1200)
    # 设置屏幕大小,或者比例
    turtle.setup(width=0.35, height=1.0)
    turtle.speed("normal")


def init_pen():
    turtle.pensize(5)
    turtle.showturtle()
    # 画笔主题色
    # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    turtle.colormode(255)
    turtle.color((255, 155, 192), "pink")


def show_coordinate(length: int = 1000):
    """
    显示 坐标系

    length * length 坐标系  30 * 30
    :return:
    """
    turtle.penup()
    turtle.home()

    half = length // 2

    # 设置 朝向东
    turtle.setheading(0)

    turtle.pensize(1)
    turtle.color('black')

    # 拿起笔开始画x 轴
    turtle.penup()
    turtle.backward(half)
    # 放下笔
    turtle.down()

    # x 轴
    # turtle.forward(length)
    print_dot(length)

    # 开始画y轴
    turtle.penup()
    turtle.home()
    turtle.goto(0, -half)

    # 设置 朝向
    turtle.setheading(90)
    # 放下笔
    turtle.down()

    print_dot(length)
    # turtle.forward(length)


def print_dot(length):
    """

    :param length:int 长度
    :return:
    """
    i = 0
    # 标尺的 单位, 10 个像素打一个点
    step = 10
    turtle.color('black')
    while i <= length:
        turtle.forward(step)
        turtle.dot(3, "blue")
        i = i + step


def words(x=0, y=0):
    """
    打印我是 佩奇
    :param x:
    :param y:
    :return:
    """
    turtle.penup()
    turtle.goto(x, y)
    print(f"turtle.position():{turtle.position()}")
    turtle.down()

    turtle.color("violet")
    turtle.write("小猪佩奇,我就是佩奇呢", font=('Arial', 40, 'normal'), align="center")

    print('write down ..')


def ear(x=0, y=0):
    # 拿笔 走到 x,y 点上
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()

    # east
    turtle.setheading(0)
    turtle.left(70)

    turtle.color((255, 155, 192), "pink")

    turtle.begin_fill()  # 准备开始填充图形

    turtle.forward(40)

    # 画个半圆
    turtle.circle(15, extent=180)
    # 转回来走直接
    turtle.forward(44)

    pensize = turtle.pen().get('pensize')

    turtle.pensize(1)

    turtle.setposition(x, y)
    turtle.end_fill()

    # 恢复画笔的大小
    turtle.pensize(pensize)


def right_ear(x=0, y=0):
    """
    右边的耳朵

    大概 位置  (80,130)
    :return:
    """
    # 拿笔 走到 x,y 点上
    turtle.penup()
    turtle.goto(x, y)

    turtle.down()

    turtle.setheading(0)
    turtle.left(60)

    turtle.color((255, 155, 192), "pink")

    turtle.begin_fill()  # 准备开始填充图形

    turtle.forward(40)

    # 画个半圆
    turtle.circle(15, extent=180)
    # 转回来走直接
    turtle.forward(44)

    pensize = turtle.pen().get('pensize')

    turtle.pensize(1)

    turtle.setposition(x, y)
    turtle.end_fill()

    # 恢复画笔的大小
    turtle.pensize(pensize)


def two_ears():
    """
    两个可爱的耳朵
    :return:
    """
    # 左边的耳朵
    ear(x=25, y=153)
    right_ear(x=80, y=130)


def eye(x=0, y=0):
    turtle.penup()
    turtle.goto(x, y)

    print(f"postion:{turtle.position()}")

    turtle.down()
    # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0..cmode范围内
    turtle.colormode(255)
    turtle.color((255, 155, 192), "pink")

    # 开始画圆
    print(f"before position:{turtle.position()}")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.color("white")
    turtle.end_fill()

    print(f"after position:{turtle.position()}")

    # 调整 里面圆的位置,画圆
    turtle.begin_fill()
    x, y = turtle.position()
    x, y = x + 8, y - 1

    # 画眼珠
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()
    print(f"turle_position:{turtle.position()}")
    turtle.color("black")
    turtle.circle(2)
    turtle.end_fill()


def two_eyes():
    """
    画两个眼睛
    :return:
    """
    init_pen()
    eye(x=0, y=130)
    x, y = turtle.position()
    # right eye
    eye(x=x + 45, y=y - 20)


def two_hands():
    """
    two hands

    # left hand  (-25,-35)

    right hand (112,-30)

    :return:
    """
    turtle.penup()
    turtle.goto((-27 + 2, -35))
    turtle.down()

    # south
    turtle.setheading(270)
    turtle.right(60)

    # left hand
    turtle.forward(45)
    turtle.backward(17)

    # 画第二个 手指
    turtle.right(45)
    turtle.forward(13)
    turtle.backward(13)

    # 画第三个手指
    turtle.setheading(270)
    turtle.right(15)
    turtle.forward(10)

    # right hand (112,-30)
    turtle.penup()
    turtle.goto((112, -30))
    turtle.down()
    # direction south
    turtle.setheading(270)

    turtle.left(60)
    turtle.forward(45)
    turtle.backward(17)

    #  # 画第二个 手指
    turtle.left(45)
    turtle.forward(13)
    turtle.backward(13)

    # 画第三个手指
    turtle.setheading(270)
    turtle.left(15)
    turtle.forward(10)

    print('two hands finished.')
    #
    # turtle.penup()
    # turtle.home()
    # turtle.hideturtle()
    pass


def leg(x=0, y=0):
    """
    腿和 脚 一起画吧
    :param x:
    :param y:
    :return:
    """
    # 保存画笔
    pen = turtle.pen()

    # 把比调整到x,y 点上.
    turtle.penup()
    turtle.goto(x, y)
    turtle.down()

    # turtle.hideturtle()
    # south
    turtle.setheading(270)
    turtle.pensize(10)
    turtle.forward(43)

    # one foot
    turtle.color("black")
    turtle.pensize(1)

    # 开始画鞋子
    # west
    turtle.setheading(180)

    # 准备填充
    turtle.begin_fill()

    turtle.right(5)
    turtle.forward(30)
    turtle.circle(6, extent=188)
    turtle.forward(30)
    turtle.circle(4, extent=190)
    # 填充完成
    turtle.end_fill()

    # 还原画笔
    turtle.pen(pen)


def two_legs():
    """
    两只腿
    :return:
    """
    leg(x=10, y=-137)

    leg(x=80, y=-137)


def skirt(x=0, y=0):
    """
    裙子 小猪佩奇的 裙子
    (-20,-18)

    left --leftmiddle----leftmiddle_second---- middle ---
    --- right_middle_second ---right_middle  --  right

    画笔颜色 要深红色 , 粗细 就是主题色 就可以了.
    :param left: (x,y)  元祖, 一个点的x,y 坐标
    :return:
    """
    # 保存画笔的属性
    pen = turtle.pen()

    # 设置颜色
    turtle.color("#CD0000")

    turtle.pensize(5)
    turtle.showturtle()

    turtle.penup()
    turtle.goto(x, y)
    print(f"postion:{turtle.position()}")
    turtle.down()

    turtle.setheading(0)
    turtle.left(-100)

    # 开始填充 裙子的颜色
    turtle.begin_fill()

    # 左边斜线1
    turtle.forward(120)
    turtle.setheading(0)

    # 下面直线2
    turtle.forward(170)

    turtle.left(100)
    # 第三条线3
    turtle.forward(115 + 2 + 2)

    # 上面一条线4
    turtle.setheading(180)

    begin = (x, y)

    # 脸颊 的相对中间点
    middle = (50, -41)
    # 最后一条线.. 第四条线,要找到对应的弧度, 还是有一定的难度
    turtle.pensize(1)
    # turtle.color("black")
    # 用粉色 可以 盖住  多边形的缺陷
    turtle.color((255, 155, 192), "pink")

    left_middle = (12, -32)
    left_middle_second = (18 + 5, -32 - 2 - 2)

    right_middle = (80, -34)
    right_middle_second = (67, -39)

    turtle.goto(*right_middle)
    turtle.goto(*right_middle_second)
    turtle.goto(*middle)
    turtle.goto(*left_middle_second)
    turtle.goto(*left_middle)

    turtle.goto(*begin)

    turtle.setheading(180)

    # 裙子的颜色,设置画笔的颜色
    turtle.color("#CD5C5C")

    # 填充裙子完成
    turtle.end_fill()

    # 恢复画笔
    turtle.pen(pen)


def tail(x=0, y=0):
    """
    tail  尾巴  (120,110)
    :return:
    """
    turtle.penup()

    turtle.goto(x, y)
    turtle.down()

    # east
    turtle.setheading(0)

    turtle.forward(10)

    turtle.circle(10, extent=145)
    turtle.setheading(225)
    turtle.circle(12, 195)


def main():
    setting()  # 画布、画笔设置

    nose(-100, 100)  # 鼻子
    head(-69, 167)  # 头

    # 耳朵
    two_ears()

    # 眼睛
    two_eyes()
    cheek(85, 10)  # 腮
    mouth(-20, 30)  # 嘴

    skirt(x=-20, y=-18)

    # 两只小手
    two_hands()

    # 尾巴
    tail(x=120 + 3, y=-110)

    # 腿和脚
    two_legs()

    words(0, -300)  # 文字

    # show_coordinate(600)
    turtle.hideturtle()
    turtle.done()


def test_one():
    turtle.home()
    print(f"position:{turtle.position()}")

    turtle.circle(50)

    print(f"position:{turtle.position()}")

    turtle.goto(100, 100)
    print(f"position:{turtle.position()}")
    turtle.circle(40)
    print(f"position:{turtle.position()}")
    turtle.done()


if __name__ == '__main__':
    main()
