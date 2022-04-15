
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


nam=Tui("Kieu Nam","2000","BienHoa","Student")
nam.intro()
nam.live("337 phạm văn thuận, biên hoà, đồng nai")
nam.work("Can Tho University")
ha=Wife("Nguyen Thu Ha","2000","Bac Giang","Student")
ha.intro()
