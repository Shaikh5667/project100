
class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceInquiry(self):
        print("Your balance is 500")

    def cashWidthDrawal(self , amount):
        new_amount = 100
        print("You have withDrawed: " + str(amount) + "Your remaining balance is:" + str(new_amount))

def main():
    name = input("Hi whats your name =")
    print("Hi,"+ name)
    cardnumber = input("Insert your card number:")
    pin = input("Enter your pin: ")
    new_user = Atm(cardnumber,pin)

    print("Select your method")
    print("1. Balance Inquiry")
    print("2. Cash withDrawal")
    method = int(input("Select method option: "))

    if (activity == 1):
        new_user.balanceInquiry()
    elif (activity == 2):
            amount = int(input("Select the amount: "))
            new_user.cashWidthDrawal(amount)
    else:
            print("Select a valid number")

if __name__ == "__main__":
    main()
            