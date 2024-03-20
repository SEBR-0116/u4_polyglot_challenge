# Challenge 1:  add_List

# Prompt:
# - Write a function called add_list that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - If called with no arguments, return 0 (zero).
# - If any non-number arguments are in the argument, return "NaN"


# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5
# add("peanut_butter", "marshmellow_fluff") //=> NaN

#-----------------------------------------------
# Solution Goes Here - >
def add_list(list):
    if len(list) == 0:
        return 0
    else:
        for x in list:
            if isinstance(x,(int,float)):
                return sum(list)
            else:
                return 'NaN'

print(add_list([]))
print(add_list([7,50,1.23]))
print(add_list([7,50,-1.23]))
print(add_list(['a','b','c']))
    
    
#-----------------------------------------------




# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
# Solution Goes Here - >
def remove_ends(str1):
    if len(str1) < 3:
            return ''
    else:
        return str1[1:len(str1)-1]

print(remove_ends("Led Zeppelin Rules"))        
    
#-----------------------------------------------



# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
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
def is_palindrome(word):
    list_no_spaces =''
    if len(word) < 2:
        return True
    else:
        for x in word:
            if x != ' ':
                list_no_spaces += x.lower()
        
        y = 0 
        z = len(list_no_spaces) -1
        
        while y < z:
            if list_no_spaces[y] != list_no_spaces[z]:
                return False
            y += 1
            z -= 1
        return True
        
    # print(list_no_spaces)
print(is_palindrome('app l pp a'))
print(is_palindrome('SEI Rocks'))
print(is_palindrome('rotor'))
print(is_palindrome('A nut for a jar of tuna'))
print(is_palindrome(''))
#-----------------------------------------------



# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true 
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

#-----------------------------------------------
# Solution goes here ->

def isPrime(input_num):
    x = 1
    if input_num <= 1:
        return False
        
    for x in range(2,input_num -1):
        if input_num % x == 0:
            print(f"test  {input_num%x}")
            return False
    print(f"test  {input_num%x}")
    return True
            
print(f"29 is prime : {isPrime(29)}")
print(f"42 is prime : {isPrime(42)}")
print(f"141 is prime : {isPrime(141)}")
print(f"2 is prime : {isPrime(2)}")
print(f"3 is prime : {isPrime(3)}")
print(f"4 is prime : {isPrime(4)}")
print(f"200 is prime : {isPrime(200)}")

#-----------------------------------------------




# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there is an 8.5% sales tax attached to each item.
# Then set up a conditional that adds a $10 Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. 
# All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]


#-----------------------------------------------
# Solution Goes Here ->
def total_cost(card, location):
    result = 0     
    loc_list_10 = ["HI", "AK", "TX", "FL"]
    loc_list_5 = ["AL", "MS", "NV", "IL"]
    # print(card[0].get('price'))
    total_no_tax = 0
    for key in range(len(card)):
        total_no_tax += card[key].get('price')
    
    print(total_no_tax)
    includes_tax = total_no_tax * 0.085 + total_no_tax
    shippint_cost = 0 
    for x in loc_list_10:
        if x == location:
            shippint_cost =  10
    for y in loc_list_5:
        if y == location:
            shippint_cost = 5
    result = includes_tax + shippint_cost
    return result

print(f"Total cost for HI shipping : {total_cost(shopping_cart,'HI')}")
#-----------------------------------------------


# Challenge 6: fizz_buzz

# Prompt -> Write a program that prints the numbers from 1 to 50. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
# If your argument is not a number, return "is not a number"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"

#-----------------------------------------------
# Solution Goes Here ->

def fizz_buzz(number):
    if not isinstance(number, (int)):
        return f"{number} is not a Number"
    if number > 0 and  number < 51:
        if number%3 == 0 and number%5 == 0:
            return "FizzBuzz"
        elif number%3 == 0:
            return "Fizz"
        elif number%5 == 0:
            return "Buzz"
        else:
            return " "
        
print(fizz_buzz(10))
print(fizz_buzz(30))
print(fizz_buzz(18))
print(fizz_buzz(22))
print(fizz_buzz("ham_sandwich"))
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
print("=================================")
def chessboard_creator(row,column):
    
    white_space = "O"
    black_space = "X"
    cell_list = []
   
    
    # Row print
    for r in range(row):
        row_pattern = []
        for c in range(column):
            # row_pattern.append(c)
            # print(row_pattern)
            if c + r % 2 == 0:
                row_pattern.append(white_space)
            elif c + r % 2 != 0:
                row_pattern.append(black_space)
            print(row_pattern)
        cell_list.append(row_pattern)
    return cell_list    
print(chessboard_creator(3,7))
#-----------------------------------------------
