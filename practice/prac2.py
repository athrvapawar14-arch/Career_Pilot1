class Bank_Account:
    def __init__(self, name, id, password, balance):
        self.name = name
        self.id = id
        self.__balance = balance
        self.__password = password

        print("The account was created successfully!!!")


    def show_balance(self):
        print(f"Your current balance is : {self.__balance}")

    def show_details(self):
        print("Your details are: ")
        print("Name : " + self.name)
        print("ID :" + self.id)




A = Bank_Account("Athrva", "AX101", "AT13", 1000 )


