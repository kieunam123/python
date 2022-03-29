# Kieu Vu Hoai Nam
# B1807650
# Cau 1
def cau1():
    num = ""
    char = ""
    s = input("nhập vào câu của bạn : ")
    for i in s:
        if i.isdigit(): 
            num+=i
        else: char+=i
    print("số lượng chữ số trong câu : ", len(num))
    print("số lượng chữ cái trong câu : ", len(char))
            
# Kieu Vu Hoai Nam
# B1807650
# Cau 2
def cau2():
    upper = ""
    lower = ""
    s = input("nhập vào câu của bạn : ")
    for i in s:
        if i.isupper():
            upper+=i
        else : lower+=i
    print("số chữ hoa là : ", len(upper))
    print("số chữ thường là : ", len(lower))

# Kieu Vu Hoai Nam
# B1807650
# Cau 3
def cau3():
    char = ""
    s = input("nhập vào câu của bạn : ")
    for i in s:
        if i.isupper():
            char+=i
        else: char+=i.upper()
    print("các chữ cái đã được in hoa : ",char)

# Kieu Vu Hoai Nam
# B1807650
# Cau 4
def cau4():
    values = []
    for i in range(100, 301):
        s = str(i)
        if (int(s[0])%2!=0) and (int(s[1])%2!=0) and (int(s[2])%2!=0):
            values.append(s)
    print (",".join(values))

# Kieu Vu Hoai Nam
# B1807650
# Cau 5
def cau5():
    