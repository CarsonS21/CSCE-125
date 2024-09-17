# hw4Task2
#Carson Sessoms
#sessomsc@usca.edu
#Homework 4
#this program takes the sum of 2 numbers or double the sum if they are the same
#last changed 2/21/2023
def mysum(x,y):
    """takes two numbers and returns their sum """
    total = x + y
    print(total)
def sum_double(x,y):
    if x == y:
        total = (x + y) * 2
        print(int(total))
    else:
        total = x + y
        print(int(total))
def test():
    """ function for testing """
    test1 = sum_double(1, 2)
    print('first test returns', test1)
    test2 = sum_double(2, 2)
    
