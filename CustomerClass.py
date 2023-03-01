class Customer:

    def __init__(self, name, addr, phone):
        self.__name = name
        self.__address = addr
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, addr):
        self.__address = addr

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
