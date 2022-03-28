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
    s = input("nhập vào câu của bạn : ")