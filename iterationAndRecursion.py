def factorial_recursive(num):
    if num == 0 or num ==1:
        return 1 
    else: 
        return num * factorial_recursive(num-1)

def factorial_iterative(num): 
    fact = 1 
    for number in range (2, num=1):
        fact = number * fact
    return fact

def main ():
    numlist = [0, 5, 10, 25, 100]







if __name__"__main__":
