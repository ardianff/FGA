class A : 
    def a(self) :
        return 'a'
class B : 
    def __str__(self) :
        return 'b'
class C(B) : 
    pass
o = C()
print(o)