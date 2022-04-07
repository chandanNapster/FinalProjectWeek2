

class name:

    def __init__(self):
        self.__name = ""

    def display(self):
        self.__name += " contributor"
        return self.__name

    def setName(self, name):
        self.__name = name


if __name__ == "__main__":
    n = name()
    n.setName("Ron")
    print(n.display())
