"""
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""


class Cat:
    def weight(self):  # 与一般函数定义不同，类方法必须包含参数self,且为第一个参数
        print("The cat weighs 10kg !")

    def height(nothing):  # self不是python关键字，我们把它换成其他的也是可以正常运行的
        print("The cat is 1 meter tall !")


# cat = Cat()
# cat.weight()
# cat.height()


class People:
    # 定义基本属性
    name = ""
    age = 18
    weight = 0  # 定义私有属性，私有属性在类外部无法直接进行访问

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def speak(self):
        print("%s 说：我%d岁了！我%d斤！" % (self.name, self.age, self.__weight))


# people = People("yuanxianchao", 18, 80)
# People.name = 100
# people.speak()


class Student(People):
    grade = ""

    def __init__(self, name, age, weight, grade):
        super().__init__(name, age, weight)
        self.grade = grade

    def speak(self):
        print("%s 说：我%d岁了，我在读%d年纪" % (self.name, self.age, self.grade))


# s = Student("ken", 10, 60, 3)
# s.speak()


# 多重继承
class Speaker:
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print("我叫%s,我是一个演说家，我演讲的主题是%s" % (self.name, self.topic))


class Sample(Speaker, Student):
    a = ""

    def __init__(self, name, age, weight, grade, topic):
        Student.__init__(self, name, age, weight, grade, )
        Speaker.__init__(self, name, topic)


test = Sample("abc", 18, 100, 10, "Python")
test.speak()


# 方法重写
class Parent:
    def my_method(self):
        print("调用父类方法")


class Child(Parent):
    def my_method(self):
        print("调用子类方法")


child = Child()
child.my_method()

# 调用父类方法
super(Child, child).my_method()
