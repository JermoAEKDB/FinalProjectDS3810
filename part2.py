userName = input("Hello! Welcome to my program! Please input your First Name:")
sameName = str("Jeremy")

if userName == sameName:
    print("Cool, that is my name too!")
    mileinput = float(input("How many miles away do you live, Jeremy?"))
    kilometeradjustment = mileinput * 1.609344
    print("That's approximately", round(kilometeradjustment,2), "kilometers away." )
else:
    mileinput = float(input("Nice to meet you," + userName + "\nHow many miles away do you live? : "))
    kilometeradjustment = mileinput * 1.609344
    print("That's approximately", round(kilometeradjustment, 2), "kilometers away.")