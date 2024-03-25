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
#-----------------------------------------------

# print('hello world')

def add_list(*nums):
    total = 0
    all_numbers = True

    if len(nums) == 0:
        return 0
    
    for num in nums:
        if isinstance(num, (float, int)):
            total += num
        else:
            print('NaN')
            all_numbers = False
    if all_numbers: 
        print(total)

add_list('st')
add_list(1, 2, 3.1)





# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------

def remove_ends(str):
    if len(str) < 3:
        return ''
    else:
        return str[1:-1]

print(remove_ends('abcde'))
print(remove_ends('ab'))

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
#-----------------------------------------------

def is_palindrome(str):
    # if len(str) is 0 or 1, return true
    if len(str) == 1 or len(str) == 0:
        return ('string length 0 or 1')
    else:
        if str[0] == str[-1]:
            return True
        else: 
            return False

print(is_palindrome('abcbcba'))



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
#-----------------------------------------------

def is_prime(num):
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
    return True
  
print(is_prime(4))
print(is_prime(29))
print(is_prime(200))


# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there is an 8.5% sales tax attached to each item. Then set up a conditional that adds a $10 Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15},
  {"item": "tower fan", "price": 35},
]


#-----------------------------------------------
# Solution Goes Here ->
#-----------------------------------------------

def total_checkout_cost(cart, state):
    # declare a total variable and initialize it to 0
    total = 0
    # declare a shipping_fee variable and initalize it to 0
    shipping_fee = 0
    # loop thru the list:
    for item in cart: 
        # go into each dictionary
        total += item['price'] + item['price'] * 0.085
    if state == 'HI' or 'AK' or 'TX' or 'FL':
    # next, check state - HI, AK, TX, or FL $10 shipping fee,
        shipping_fee = 10
        total += shipping_fee
    # - AL, MS, NV, or IL $5 shipping fee
    elif state == 'AL' or 'MS' or 'NV' or 'IL':
        shipping_fee = 5
        total += shipping_fee

    return total



print(total_checkout_cost(shopping_cart, 'CA'))


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
#-----------------------------------------------

def fizz_buzz(num):
    if isinstance(num, (float, int)) == False:
        print((f'{num}is not a number'))
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    print(num)


fizz_buzz(1)

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
#-----------------------------------------------


def chess_board(rows, columns):
    # Initialize the chessboard
    board = []

    # Generate each row
    for row in range(rows):
        # Initialize the current row
        current_row = []
        
        # Generate each column in the row
        for col in range(columns):
            # Determine the cell color based on the sum of row and column indexes
            if (row + col) % 2 == 0:
                current_row.append("O")  # White space
            else:
                current_row.append("X")  # Black space

        # Add the completed row to the chessboard
        board.append(current_row)

    return board

print(chess_board(2, 3))