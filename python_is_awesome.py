print("how are you")

name = "Gin"
age = 50

print("I am "+name + " and my age is " + str(age))


def fun(a):
    print(a+100)
    return "hallo"

my_return_value = fun(5)
print("my_return_value is "+str(my_return_value))


class Name:
    def classfunction(self):
        print("hey I'm inside the class")

n = Name()
n.classfunction()
