

"Single Inheritance"
# class A:
#     def meth_a(self):
#
#         return f"print A"
#
# class B(A) :
#     def meth_b (self):
#         return f"print B"
#
#
# obj1 = B()
#
# print(obj1.meth_a())
# print(obj1.meth_b())



"Multiple Inheritance"


class A :
    def meth_a(self):
        return "From A"

class B:
    def meth_b(self):
        return "From B"

    def meth_a(self):
        return "from A<B"

class C(B,A):
    def meth_c(self):
        return "From C"


obj1 = C()

print(obj1.meth_c())
print(obj1.meth_b())
print(obj1.meth_a())

"mutlilevel Inheritance"

"Multiple Inheritance"


# class A :
#     def meth_a(self):
#         return "From A"
#
# class B(A):
#     def meth_b(self):
#         return "From B"
#
#     # def meth_a(self):
#     #     return "From A,B"
#
# class C(B):
#     def meth_c(self):
#         return "From C"
#
#
# obj1 = C()
#
# print(obj1.meth_c())
# print(obj1.meth_b())
# print(obj1.meth_a())

"herical"

# class A :
#     def meth_a(self):
#         return "From A"
#
# class B(A):
#     def meth_b(self):
#         return "From B"
#
#     # def meth_a(self):
#     #     return "From A,B"
#
# class C(A):
#     def meth_c(self):
#         return "From C"
#
#
# obj1 = C()
# obj2 = B()
#
# print(obj1.meth_c())
# print(obj1.meth_a())
#
# print(obj2.meth_b())
# print(obj2.meth_a())



"Hybrid Inheritance"

# class A :
#     def meth_a(self):
#         return "From A"
#
# class B(A):
#     def meth_b(self):
#         return "From B"
#
#     # def meth_a(self):
#     #     return "From A,B"
#
# class C(A):
#     def meth_c(self):
#         return "From C"
#
# class D(B,C):
#     def math_d(self):
#         return "Form D"

# obj1 = C()
# obj2 = B()
#
# print(obj1.meth_c())
# print(obj1.meth_a())
#
# print(obj2.meth_b())
# print(obj2.meth_a())


class A:
    def meth(self):
        return "From A"
    # pass

class B(A):
    # def meth(self):
    #     return "From B"
    pass
    # def meth_a(self):
    #     return "From A,B"


class C(A):
    def meth(self):
        return "From C"
    # pass

class D(B, C):
    # def math(self):
    #     return "Form D"
    pass

# print(D.mro())

ob1 = D()
print(ob1.meth())


class A:
    # def meth(self):
    #     return "From A"
    pass

class B(A):
    # def meth(self):
    #     return "From B"
    pass
    # def meth_a(self):
    #     return "From A,B"


class C(B):
    # def meth(self):
    #     return "From C"
    pass

class D(C,A):
    # def math(self):
    #     return "Form D"
    pass

print(D.mro())