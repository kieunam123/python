class human:
    def __init__(self,hoten,namsinh,quequan,nghenghiep):
        self.hoten = hoten
        self.namsinh = namsinh
        self.quequan = quequan
        self.nghenghiep = nghenghiep

class Tui(human):
    def __init__(self, hoten, namsinh, quequan, nghenghiep):
        super().__init__(hoten, namsinh, quequan, nghenghiep)
    def intro(self):
        print("tui tên là : {}".format(self.hoten))
    def live(self,noicutru):
        print("{} đang sống ở {}".format(self.hoten,noicutru))
    def work(self,diachicoquan):
        print("{} đang làm {} tại {}".format(self.hoten,self.nghenghiep,diachicoquan))


class Wife(human):
    def __init__(self, hoten, namsinh, quequan, nghenghiep):
        super().__init__(hoten, namsinh, quequan, nghenghiep)
        self._husband = "Kieu Nam"

    def intro(self):
        print("{} là vợ của {}".format(self.hoten,self._husband))

class nguoi(human):
    def __init__(self, hoten, namsinh, quequan, nghenghiep):
        super().__init__(hoten, namsinh, quequan, nghenghiep)
    def intro(self,diachicoquan):
        print("họ tên : {}".format(self.hoten))
        print("năm sinh : {}".format(self.namsinh))
        print("quê quán : {}".format(self.quequan))
        print("nghề nghiệp : {}".format(self.nghenghiep))
        print("địa chỉ cơ quan : {}".format(diachicoquan))

class Student()

nam=Tui("Kieu Nam","2000","BienHoa","Student")
nam.intro()
nam.live("337 phạm văn thuận, biên hoà, đồng nai")
nam.work("Can Tho University")
ha=Wife("Nguyen Thu Ha","2000","Bac Giang","Student")
ha.intro()

def bt2():
    name={};year={};place={};job={};company={}
    n=int(input("nhập số lượng người muốn nhập vào hệ thống : "))
    for i in range(1,n+1):
        name[i]=input("nhập họ tên người thứ %d : "%i)
        year[i]=int(input("nhập năm sinh người thứ %d : "%i))
        place[i]=input("nhập quê quán người thứ %d : "%i)
        job[i]=input("nhập nghề nghiệp người thứ %d : "%i)
        company[i]=input("nhập địa chỉ cơ quan người thứ %d : "%i)
        print("--------")
    for i in range(1,n+1):
        print("--------\nthông tin người thứ %d : "%i)
        connguoi=nguoi(name[i],year[i],place[i],job[i])
        connguoi.intro(company[i])
bt2()
