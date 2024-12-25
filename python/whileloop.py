# password = input("enter your password :")
# while password != "Balaji@2124":
#     print("wrong password enter again!")
#     password = input("try again :")
# print("welcome balaji")


# num = int(input("enter a num between o and end :"))
# total = 0
# while num != 0:
#     total = total +num
#     num = int(input("enter another number :"))
# print("total count =",total)
# total = total * 0.8
# print("total discount :",total)


# num = int(input("enter a number between 1 to 10"))
# tries = 0
# while num != 2:
#     if num <= 0:
#         tries +=1
#         print("number must be greater than 0")
#         num = int(input("enter a number greater than 0 :"))
#     elif num >=11:
#         tries +=1
#         print("number must be less than 10")
#         num = int(input("enter a number less than 10 :"))
#     else:
#         tries +=1
#         print("guess again")
#         num = int(input("enter new number :"))
# print("you guessed correct number in ",tries,"attempts")

"""Write a Python program that prints the multiplication table for a number that the user inputs. The table should display the products from 1 to 10.
For example, if the user inputs 7, the output should be:
7 x 1 = 7
:
:
7 x 10 = 70
Requirements:
Use a loop to generate the table.
Prompt the user for the number, then print the multiplication results."""

# number = int(input("enter a number to get it table"))
# a = 1
# while a < 11 :
#     print(number,"x",a,"=",(number * a))
#     a+=1
# if number == 1:
#     print("this is your",number,"st table ")
# elif number ==2:
#     print("this is your",number,"nd table ")
# elif number == 3:
#     print("this is your",number,"rd table ")
# else:
#     print("this is your",number,"th table ")

"""Challenge: Count Down Timer
Write a Python program that takes a number as input and counts down from that number to 0, printing each number along with a message.
For example, if the user inputs 5, the output should look like:
5... Get ready!
4... Get ready!
3... Get ready!
2... Get ready!
1... Get ready!
0... Time's up!
Requirements:
Use a loop to count down from the number to 0.
Print a message along with each number.
At the end, print <Time's up!>"""

# number = int(input("enetr a number to start countdown"))
# while number != 0:
#     if number >0:
#         print(number,"... Get ready!")
#         number -=1
#     else:
#         number = int(input("number must be psitive : "))
# print("0 ...Time's up!")

"""Challenge: Even and Odd Counter
Write a Python program that:
Takes a list of numbers from the user (you can hardcode a sample list if you prefer).
Counts how many of the numbers are even and how many are odd.
Prints the count of even and odd numbers.
For example, for the list [1, 2, 3, 4, 5, 6], the output should be:
Even numbers: 3
Odd numbers: 3
Requirements:
Use a loop to iterate over the list.
Use modulo operation (%) to check if a number is even or odd."""

# even = 0
# odd = 0
# while True:
#     a = int(input("enter a number,0 to stop"))
#     if a == 0:
#         break
#     if a % 2 == 0:
#         even += 1
#     if a % 2 != 0:
#         odd += 1
#     if a < 0 :
#         pass
# print("even numbers count =",even)
# print("odd numbers count =",odd)

