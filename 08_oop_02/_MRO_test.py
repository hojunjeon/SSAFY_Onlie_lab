class A :
    def __ini__(self) :
        print("A")
class B :
    def __ini__(self) :
        print("B")        

class C(A) :
    def __ini__(self) :
        super().__init__()
        print("C")
class D(B) :
    def __ini__(self) :
        super().__init__()
        print("D")

class E(C,D) :
    def __ini__(self) :
        super().__init__()
        print("E")                

print(E.__mro__)