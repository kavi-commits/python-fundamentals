# day 15 week 4

#class and objects

#class is the blueprint drawing of a motor
#object is one motor built from it
#attributes are what that motor holds: its serial number, its RPM.
#methods are what that motor can do: start(), stop().


class Motor:
    def __init__(self, serial, rpm): # the assembly line step that fills in the starting values
        self.serial = serial
        self.rpm = rpm

    def spin(self):
        print(f"Motor {self.serial} spinning at {self.rpm} RPM")

m1 = Motor("A-001", 1500)
m2 = Motor("A-002", 3000)
m1.spin() # Motor A-001 spinning at 1500 RPM
m2.spin() # Motor A-002 spinning at 3000 RPM

# What actually happens when you write Motor("A-001", 1500)
# 1. Python builds a blank, empty motor in memory
# 2. it automatically calls __init__ on the blank motor, handling it "A-001" and 1500.
# 3. inside __init__, self.serial = serial means "stamp this serial onto this motor"
# 4. the finished motor is stored in m1.

# self = "this one"
# when you call m1.spin() , python secretly rewrites it as Motor.spin(m1). so self is just m1 inside the method.
# self.rpm inside spin() reads m1's RPM
# call m2.spin() and the same code now reads m2's RPM

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"The current balance is {self.balance}.")

acc1 = BankAccount("John", 500)
acc2 = BankAccount("Mary", 800)

acc1.deposit(300)
acc2.deposit(400)
acc1.show_balance()
acc2.show_balance()
acc1.withdraw(200)
acc2.withdraw(300)
acc1.show_balance()
acc2.show_balance()
