class NameOfClass():
    class_attribute = 'some_value'

    # constructor
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg1 = arg1

    def method(self):
        # CODE HERE
        return("message from method")

    def method2(self, arg1):
        # CODE HERE
        return(f"message from method2 with paramether is {arg1}")

    @classmethod
    def cls_method(cls, arg1, arg2):
        # CODE HERE
        return("message from cls_method and your parameter is {} and {}".format(arg1, arg2))

    @staticmethod
    def stc_method(arg1, arg2):
        # CODE HERE
        pass

# Create class object
class_object1 = NameOfClass('param1', 'param2')

# Call method (call to line9)
print(class_object1.method())
print(class_object1.method2('hello'))

# Call class method (line 14) @classmethod not require instance
print(NameOfClass.cls_method('param1', 'param2'))