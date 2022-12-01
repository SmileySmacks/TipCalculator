def calculation():
    tip_percent = tip / 100
    tip_amount = bill * tip_percent
    meal_and_tip = tip_amount + bill
    total_to_return = meal_and_tip / to_split
    return total_to_return

def user_input(prompt, datatype):
    value = input(prompt)
    try:
        input_to_return = datatype(value)
        return input_to_return
    except ValueError:
        print("Input failed, please use {:s}".format(str(datatype)))
        return user_input(prompt, datatype)


print("\nWelcome to the \"Bill Tip Calculator\"!")
print("\nAll you need to do is:\n1.) Enter your bill\n2.) Enter the amount of people (if bill is being split)\n3.) Enter the amount you would like to tip.")
print("\n\n1.) What was the total for the bill?")
bill = user_input("Total Bill: ", float)
print("\nAwesome, the total for your meal was " + "$" + str(bill) + ".")
print("\n\n2.) How many people are splitting the bill?")
to_split = user_input("Number of People: ", int)
print("\nSo the bill is divided", str(to_split), "way(s).")
print("\n\n3.) What percent of the bill would you like to leave as a tip? (Enter a numeral value only. No special characters.)")
tip = user_input("Tip: ", int)
print("\nYou would like to tip", str(tip) + "%! Nice!")
total = calculation()
print("\n\n\n\nYour total is " + "$" + str(total), "each! Thank you for using the \"Bill Tip Calculator\"!")
