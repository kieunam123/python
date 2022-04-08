import numpy as np
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

bt7()