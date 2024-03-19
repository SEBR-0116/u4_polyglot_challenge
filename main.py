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

def add_list(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "NaN"
    return total
    
# print(add_list(1,2,3))




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

def remove_ends(s):
    if len(s)<3:
        return " "
    else:
        return s[1:-1]
    
# print(remove_ends("Today is Monday"))
# print(remove_ends("Hi"))
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
    

def is_palindrome(a):
        a = a.lower().replace("","")
        if len(a) <= 1:
            return True 
        return a == a[::-1]
    
# print(is_palindrome("radar"))
# print(is_palindrome("Hello"))
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

## 2 is the smallest prime number 
def is_prime(x):
    if x < 2:  
        return False
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: 
            return False
    
    return True 
# print(is_prime(2)) 
#-----------------------------------------------




# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there is an 8.5% sales tax attached to each item. Then set up a conditional that adds a $10 Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. All other states recieve free shipping. 

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

def calculate_total_cost(items_list, homestate):
    sales_tax_rate = 0.085  
    shipping_fee = 0
    
    for item in items_list:
        item_price = item['price']
        total_item_cost = item_price
        
        # Calculate sales tax for the item
        sales_tax = total_item_cost * sales_tax_rate
        
        # Add sales tax to the total cost
        total_item_cost += sales_tax
        
        # Add shipping fee based on homestate
        if homestate in ['HI', 'AK', 'TX', 'FL']:
            shipping_fee += 10
        elif homestate in ['AL', 'MS', 'NV', 'IL']:
            shipping_fee += 5
    
    # Add shipping fee to the total cost
    total_cost = sum(item['price'] for item in items_list) + shipping_fee
    
    return total_cost

# print( calculate_total_cost(shopping_cart,"AL"))
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
def fizzbuzz(num):
    if not isinstance(num, int):
        return "is not a number"
    
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
# fizzbuzz(50)
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
def create_chessboard(rows, columns):
    chessboard = []
    for row in range(rows):
        row_data = []
        for col in range(columns):
            if (row + col) % 2 == 0:
                row_data.append('O')  # White cell
            else:
                row_data.append('X')  # Black cell
        chessboard.append(row_data)
    return chessboard

# Test the function
rows = 6
columns = 4
chessboard = create_chessboard(rows, columns)

# Print the chessboard pattern
for row in chessboard:
    print(row)

#-----------------------------------------------
