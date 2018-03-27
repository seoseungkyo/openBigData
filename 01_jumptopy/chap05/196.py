class FourCal:
    def setdsata(self,first,second):
        self.first=first
        self.second=second

    def sum(self):
        result=self.first+self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a=FourCal()
b=FourCal()
a.setdsata(4,2)
b.setdsata(3,7)
a.sum()
a.mul()
a.div()
b.sum()
b.mul()
b.sub()
b.div()
