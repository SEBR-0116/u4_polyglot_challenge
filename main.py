# Challenge 1:  add_List

# Prompt:
# - Write a function called add_list that accepts any quantity of numbers as arguments, 
# adds them together and returns the resulting sum.
# - If called with no arguments, return 0 (zero).
# - If any non-number arguments are in the argument, return "NaN"

# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5
# add("peanut_butter", "marshmellow_fluff") //=> NaN

#-----------------------------------------------
# Solution Goes Here - >

def add_list(*args):
    try:
        return sum(args)
    except TypeError:
        return "NaN"

result = add_list(5, 6, 7, 8, 9)
print("Sum:", result)

result = add_list(10, 20, 30)
print("Sum:", result)

result = add_list('a', 'b')
print("Sum:", result)
#-----------------------------------------------




# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, 
# then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
# Solution Goes Here - >

def remove_ends(string):
    if len(string) < 3:
        return " "
    else: 
        return string[1: -1]
    
input_string = "Mia"
print(remove_ends(input_string))

input_string = "Boom"
print(remove_ends(input_string))

input_string = "Vanderpump Rules"
print(remove_ends(input_string))
#-----------------------------------------------



# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, 
# then returns true or false depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that is the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.

# Examples:
# is_palindrome('SEI Rocks'); //=> false
# is_palindrome('rotor'); //=> true
# is_palindrome('A nut for a jar of tuna'); //=> true
# is_palindrome(''); //=> true

#-----------------------------------------------
# Solution Goes Here - >

def is_paliondrom(string):
    cleaned_string = ''.join(char for char in string if char.isalnum())

    start = 0
    end = len(cleaned_string) -1

    while start < end:
        if cleaned_string[start] != cleaned_string[end]:
            return False
        start += 1
        end -= 1
    return True

print(is_paliondrom("radar"))
print(is_paliondrom("race car"))
print(is_paliondrom("yellow"))
print(is_paliondrom("madam"))
print(is_paliondrom("theatre"))
#-----------------------------------------------



# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime 
# number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.

# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true 
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

#-----------------------------------------------
# Solution goes here ->

def is_prime(n):
    if n <= 1:
        return False
    
    for x in range(2, int(n** 0.5) + 1):
            if n % x == 0:
                return False
            
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(18))
print(is_prime(0))
#-----------------------------------------------




# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost 
# if there is an 8.5% sales tax attached to each item. Then set up a conditional that adds a $10 
# Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. 
# All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

#-----------------------------------------------
# Solution Goes Here ->

def total_cost(shopping_cart, homestate):
    sales_tax = 8.5 /100
    additional_fee_states = ['HI', 'FL', 'TX', 'AK'] 
    total_price = sum(item['price']for item in shopping_cart)

    if homestate in additional_fee_states:
        total_price += 10
    elif not homestate in additional_fee_states:
        return "Free Shipping!"

    total_price_with_tax = total_price * (1 + sales_tax)
    return total_price_with_tax    

shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]

homestate = 'TX'
print("Total cost with tax and additional fee:", total_cost(shopping_cart, homestate))
#-----------------------------------------------


# Challenge 6: fizz_buzz

# Prompt -> Write a program that prints the numbers from 1 to 50. 
# But for multiples of three print “Fizz” instead of the number and 
# for the multiples of five print “Buzz”. For numbers which are 
# multiples of both three and five print “FizzBuzz”
# If your argument is not a number, return "is not a number"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"

#-----------------------------------------------
# Solution Goes Here ->

def fizzbuzz(n):
    if not isinstance(n, int) and not isinstance(n, float):
        return "is not a number"
    
    result = []
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

print(fizzbuzz(50))
print(fizzbuzz(3))
print(fizzbuzz(35))
print(fizzbuzz("Howdy"))
#-----------------------------------------------




# Challenge 7 - Chessboard Creator

# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

# Making a digital chessboard is an interesting way of visualising how loops can work together.

# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

# So chess_board(6,4) should return an array like this:



[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]
# And chess_board(3,7) should return this:


[
    ["O","X","O","X","O","X","O"],
    ["X","O","X","O","X","O","X"],
    ["O","X","O","X","O","X","O"]
]

#The white spaces should be represented by an: 'O' and the black an: 'X'

# The first row should always start with a white space 'O'

#-----------------------------------------------
# Solution Goes Here - >

def chess_board(rows, colomns):
#---- Create empty list called board ------##
    board = []
#---- Nest loop to generate row of chessboard -----##
    #-- Row index is 'r' ----#
    for r in range(rows):
        row = []
    #-- Colomn index is 'c' ----#
        for c in range(colomns):
#---- Condition to determine place x or o ---------##
            if (r + c) % 2 == 0:
                if r == 0 and c == 0:
                    row.append('o')
                else:
                    row.append('x')
            else:
                row.append('o')
        board.append(row)
    return board

rows = 4
colomns = 6
chessboard = chess_board(rows, colomns)
for row in chessboard:
    print(row)
#-----------------------------------------------
