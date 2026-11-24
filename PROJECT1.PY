# Rent Calculator

rent= int(input("Enter your flat/room rent= "))
food= int(input("Enter the amount of food ordered= "))
electricity_spend =int(input("Enter the total electricity spend=  "))

charge_per_unit = int(input("Enter the Charge per unit=  "))
persons = int(input("Enter the number of persons living in rooom/flat= "))

total_bill = electricity_spend * charge_per_unit
output =(food + rent + total_bill) // persons

print("Each person have to pay = ",output)