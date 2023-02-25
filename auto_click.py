from pymouse import PyMouse #调用Pymouse模块
from PIL import Image
from PIL import ImageChops
import time #调用时间模块（考略到网站点击延时）

def click_func():
    print("Start program")
    n = 1000
    t = 1
    for i in range(n): #循环n次
        m = PyMouse()
        a = m.position()#获取当前坐标的位置
        print(i)
        print(a) #显示位置
        time.sleep(t)   #延时t秒
        print("grapping screen")
        grap_screen()
        print("grapping screen done")
        if compare_images() == "success":
            m.move(100, 100) #鼠标移动至坐标（x,y）
            a = m.position()
            print(a)
            m.click(888, 524)   #鼠标点击坐标（x,y）
        else:
            print("error")
        time.sleep(t) 


def grap_screen():
    area = (0, 0, 300, 300)
    im2 = ImageGrab.grab(area)
    im2.save("screenshot.png")
    return im2

def compare_images():
    """
    比较图片
    :param path_one: 第一张图片的路径
    :param path_two: 指定屏幕位置
    :return: 相同返回 success
    """
    image_one = Image.open("screenshot.png")
    image_two = Image.open("STANDER.jpg")
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            return "success"
        else:
            return "ERROR: 匹配失败！"

    except ValueError as e:
        return "{0}\n{1}".format(e, "图片大小和box对应的宽度不一致!")


if __name__ == '__main__':
    click_func()

