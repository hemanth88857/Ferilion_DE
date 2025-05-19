class ParentClass:
    parent_clas_var = "parent_clas_var"

    def __init__(self, parent_inst_var):
        self.parent_inst_var = parent_inst_var
        self._parent_prot_var = "_parent_prot_var"         #  Protect variable
        self.__parent_private_var = "__parent_private_var" #  private variable

    def parent_inst_meth(self):
         return f"from parent class {self.parent_inst_var}"


    def _parent_prot_meth(self):
        return 'from _parent_prot_meth'

    def __parent_private_meth(self):                        #Private method
        return "from __parent_private_meth"

    @classmethod
    def parent_class_method(cls):
        return "from parent_class_method"

    @staticmethod
    def parent_stat_meth():
        return "from parent_stat_meth"

    @property
    def parent_prop_meth(self):
        return "from parent_prop_meth"


class ChildClass(ParentClass):
    def __init__(self, child_cls_inst_var, for_parent_inst_var):
        # ParentClass.__init__(self, for_parent_inst_var)
        super().__init__(for_parent_inst_var)
        self.child_cls_inst_var = child_cls_inst_var
        self.for_parent_inst_var = for_parent_inst_var


    def child_inst_meth(self):
        return (f"{self.parent_inst_var} \n"
                f"{ParentClass.parent_clas_var}\n"
                f"{ParentClass.parent_class_method()}\n"
                f"{self.parent_inst_meth()} \n"
                f"{super().parent_inst_meth()} \n"
                f"{super()._parent_prot_meth()} \n"
                f"{super()._ParentClass__parent_private_meth()} \n"
                f"{super().parent_stat_meth()} \n"
                f"{self._parent_prot_var} \n"
                f"{self._ParentClass__parent_private_var} \n"
                f"{self.parent_prop_meth}")

    def parent_inst_meth(self):
        return "from child class"

ch_obj = ChildClass("child", "parent")
print(ch_obj.child_inst_meth())
print(ch_obj.parent_prop_meth)
print(ch_obj.parent_inst_var)
print(ch_obj._parent_prot_var)
print(ch_obj.parent_clas_var)
print(ch_obj.__parent_private_var)
print(ch_obj.parent_stat_meth())
print(ch_obj.parent_inst_meth())
print(ch_obj._parent_prot_meth())
print(ch_obj.parent_class_method())
print(ch_obj.__parent_private_meth())


# class Fun:
#     def __init__(self, fun_inst_var):
#         self.fun_inst_var = fun_inst_var
#
#     def parent_inst_meth(self):
#         return "from Fun Class"
#
#
# class ChildClass(ParentClass, Fun):
#
#     def __init__(self, ch_ins_var, pr_ins_var, fun_ins_var):
#         ParentClass.__init__(self, pr_ins_var)
#         Fun.__init__(self, fun_ins_var)
#         self.ch_ins_var = ch_ins_var
#         self.pr_ins_var = pr_ins_var
#         self.fun_ins_var = fun_ins_var
#
#
#     def ch_inst_meth(self):
#         return f"{super().parent_inst_meth()}"
#
#     def parent_inst_meth(self):
#         return "from Child Class"
#
#
# obj = ChildClass("child", "parent", "fun")
# print(obj.parent_inst_meth())
#
#

# class A:
#     def meth(self):
#         print("entering A")
#         super().meth()
#         print("exiting A")
#
# class B(A):
#     def meth(self):
#         print("entering B")
#         super().meth()
#         print("exiting B")
#
# obj = B()
# obj.meth()