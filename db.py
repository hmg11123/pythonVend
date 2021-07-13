# 자판기
class Vend :
    type = ""
    name = ""
    value = 0
    sell= 0
    remnant= 0

    def data_setter(self, v1, v2, v3, v4, v5) :
        self.type = v1
        self.name = v2
        self.value = v3
        self.sell = v4
        self.remnant = v5

    def __str__(self):
        return f"{self.type}자판기 | {self.name} | {self.value}  | {self.sell} | {self.remnant}"
    
