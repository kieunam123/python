from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Kieu Vu Hoai Nam
# B1807650
def bt1():
    arr = np.array([1,3,5,7,9])
    print(arr)

# Kieu Vu Hoai Nam
# B1807650
def bt2():
    arr=np.array([(1,3,5,7,9), 
                  (2,4,6,8,10)])
    print(arr)

# Kieu Vu Hoai Nam
# B1807650
def bt3():
    arr=np.zeros((10))
    arr[6]=13
    print(arr)

# Kieu Vu Hoai Nam
# B1807650
def bt4():
    b=np.ones((5,5))
    b[1,1]=0;b[1,2]=0;b[1,3]=0
    b[2,1]=0;b[2,2]=0;b[2,3]=0
    b[3,1]=0;b[3,2]=0;b[3,3]=0
    print(b)

# Kieu Vu Hoai Nam
# B1807650
def bt5():
    c=np.ones((3,3))
    c1=np.pad(c,pad_width=1)
    print(c1)

# Kieu Vu Hoai Nam
# B1807650
def bt6():
    list1=np.array([10,20,40,60,70])
    list2=np.array([10,30,50,60])
    eq=np.intersect1d(list1,list2)	
    print(eq)


# Kieu Vu Hoai Nam
# B1807650
def bt7():
    d=np.linspace(1,100,num=100)
    chan=np.where(d%2==0)
    print(chan)

# Kieu Vu Hoai Nam
# B1807650
def bt8():
    x=np.arange(-10.0,10.0,0.01)
    # x=np.linspace(-10,10,num=20,dtype=int)
    y=np.sin(x)
    plt.scatter(x,y)
    plt.show()

# Kieu Vu Hoai Nam
# B1807650
def bt9():
    x=np.linspace(-5,5,num=20,dtype=int)
    y=x**3-2*x**2+x+5
    plt.scatter(x,y)
    plt.show()

# Kieu Vu Hoai Nam
# B1807650
def bt10():
    x=np.arange(-10.0,10.0,0.01)
    y=np.sin(x)
    z=np.cos(x)
    plt.plot(x,y,x,z)
    plt.title("Do thi hinh sin va cos")
    plt.legend()
    plt.show()

# Kieu Vu Hoai Nam
# B1807650
def bt11(): 
    x=np.arange(-10.0,10.0,0.01)
    figsize = (7, 7)
    cols=3
    rows=1
    y1=np.sin(x)
    y2=np.cos(x)
    y3=np.tan(x)
    plt.figure(figsize=figsize, constrained_layout=True).subplots(cols,rows)
    # sin
    ax1 = plt.subplot(221)
    plt.plot(x,y1,'o', ls='-', ms=4,markevery=None, color='green')
    plt.title("Sin")
    # cos
    ax2 = plt.subplot(222)
    plt.plot(x,y2,'o', ls='-', ms=4,markevery=None, color='red')
    plt.title("Cos")
    # tan
    ax3 = plt.subplot(223)
    plt.plot(x,y3,'o',ms=5,ls='-',markevery=3, color = 'blue')
    plt.title("Tan")
    # draw
    ax1.set(xlim=(-10.0,10.0),ylim=(-2.0,2.0), autoscale_on=False)
    ax2.set(xlim=(-10.0,10.0),ylim=(-2.0,2.0), autoscale_on=False)
    ax3.set(xlim=(-1.5,1.5),ylim=(-2.0,2.0), autoscale_on=False)
    plt.show()

# Kieu Vu Hoai Nam
# B1807650
def bt12(): 
    image = Image.open('hinh.jpeg') 
    image.show()

# Kieu Vu Hoai Nam
# B1807650
def bt13(): 
    image = Image.open('hinh.jpeg')
    box = (100, 100,200,200)
    new_image = image.crop(box)
    new_image.show()

# Kieu Vu Hoai Nam
# B1807650
def bt14(): 
    image = Image.open('hinh.jpeg')
    image_180 = image.rotate(180)
    image_180.save('anhchinhsua.jpg')
    image_180.show()

# Kieu Vu Hoai Nam
# B1807650
def bt15(): 
    image = Image.open('hinh.jpeg')
    xamden_image = image.convert('L')
    image_180 = xamden_image.rotate(180)
    image_180.save('anhtrangden.jpg')
    image_180.show()

