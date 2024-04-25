def find_highest_number(num1, num2, num3):
    return max(num1, num2, num3) #change max to min to find smallest number

num1 = input("Type in your first number: ")
num2 = input("Type in your second number: ")
num3 = input("Type in your third number: ")
highest_number = find_highest_number(num1, num2, num3)
print("The highest number between {}, {}, and {} is: {}".format(num1, num2, num3, highest_number))
