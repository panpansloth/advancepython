import abc


class Validated(abc.ABC):
    def __set_name__(self, owner, name):
        """
        __set_name__方法的作用是，当一个描述符被放置到一个类的属性中时，它会自动调用__set_name__方法。
        :param owner: 其中owner参数是托管类的引用
        :param name: name参数是属性的名称
        :return:
        """
        self.storage_name = name

    def __set__(self, instance, value):
        """
        :param instance: 托管实例的引用
        :param value: 要设定的值
        :return:
        """
        # __set__方法的第1行把职责委托给自身的validate方法。
        value = self.validate(instance, value)
        instance.__dict__[self.storage_name] = value

    @abc.abstractmethod
    def validate(self, instance, value):
        """
        abc.abstractmethod装饰器把validate方法标记为抽象方法。
        抽象方法只有声明，没有实现。
        :param instance:
        :param value:
        :return: return validated value or raise ValueError
        """


class Quantity(Validated):
    """a number greater than zero"""

    def validate(self, instance, value):
        # 实现抽象方法Validated.validate要求的模板方法
        if value <= 0:
            raise ValueError(f'{self.storage_name} must be > 0')
        return value


class NonBlank(Validated):
    """a string with at least one non-space character"""

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError(f'{self.storage_name} cannot be empty or blank')
        return value


class LineItem:
    # description = NonBlank()在LineItem类中被执行时,NonBlank实例的__set_name__方法会被自动调用。
    # 这个方法把描述符的storage_name属性设为'description'。
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        # 在LineItem实例的__init__方法中,描述符的__set__方法被调用,把值设定为托管实例的属性。
        self.description = description
        self.weight = weight
        self.price = price


    def subtotal(self):
        return self.weight * self.price


truffle = LineItem('White truffle', 1, 1)
print(truffle.__dict__)
