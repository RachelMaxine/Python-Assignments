'''Assignment 1

This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.

This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1.
    Factorial. 1 point.

    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.

    Parameters
    ----------
    x: int
        the integer whose factorial to return

    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line
def factorial(n):

	return 1 if (n==1 or n==0) else n * factorial(n - 1);

num = 4;
print("Factorial of",num,"is",
factorial(num))


    '''Item 2.
    Classify Grade. 2 points.

    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9

    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.

    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line
marks = float(input("Input Grade"))

if marks >= 92:
    print("Grade: A+")
elif marks >= 86 and marks < 91.9:
    print("Grade: A")
elif marks >= 80 and marks < 85.9:
    print("Grade: A")
elif marks >= 74 and marks < 79.9:
    print("Grade: B+")
elif marks >= 67 and marks < 73.9:
    print("Grade: B")
elif marks >= 60 and marks < 66.9:
    print("Grade: C")
else:
    print("Grade: F")


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.

    You have purchased two bags of items.
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.

    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.

    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line

item_quantity_1 = float(input('Quantity of Items in Bag 1'))
item_quantity_2= float(input('Quantity of Items in Bag 2'))
item_weight_1 = float(input('Weight of Each Item in Bag 1'))
item_weight_2 = float(input('Weight of Each Item in Bag 2'))

avg = (item_quantity_1*item_weight_1 + item_quantity_2*item_quantity_2) / (item_quantity_1+item_quantity_2)

print('The weighted average weight of one item = %avg)

def string_sum(string):
    '''Item 4.
    String Sum. 3 points.

    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.

    Parameters
    ----------
    string: str
        a string that can contain any character.

    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line
def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit

print(sum_digits_string("Rachel12122000"))

def distance(x_1, y_1, x_2, y_2):

    '''Item 5.
    Distance. 3 points.

    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum

    You may want to import the `math` library for this number.

    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate

    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line
x_1 = float(input('Enter x1: '))
y_1 = float(input('Enter y1: '))
x_2 = float(input('Enter x2: '))
y_2 = float(input('Enter y2: '))

d = ( (x_2-x_1)**2 + (y_2-y_1)**2 ) ** 0.5

print('Distance = %f' %(d))

def make_change(amount):
    '''Item 6.
    Make Change. 5 points.

    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.

    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.

    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line
    diffChange =amount
    countPeso =0
    count25 =0
    count10 =0
    count05 =0
    count01 =0
    if amount ==0:
        return 0
    while diffChange >= 1 :
        countPeso += 1
        diffChange -=1

    while diffChange >= .25:
        countPeso +=1
        diffChange -=.25

    while diffChange >= .10:
        countPeso +=1
        diffChange -=.10

    while diffChange >= .05:
        countPeso +=1
        diffChange -=.05

    while diffChange >= .01:
        countPeso +=1
        diffChange -=.01

    print(f"1P:{countPeso}/25C:{count25}/10C:{count10}/5C:{count05}/1C:{count01}")
make_change(27.78)
