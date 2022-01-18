class BankAccount(object):
    # __init__ is like a constructor
    # it is used to initialize the object that is created
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        print('in __init__')
        
    # all methods (with some exceptions) must have self as a first parameter...
    # ...even though you don't pass self when you call the method (Python does)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("can't deposit nonpositive amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("can't withdraw", amount, "or you would be overdrawn!")
        else:
            print("can't withdraw nonpositive amount!")

