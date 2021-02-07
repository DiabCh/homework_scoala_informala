# 1


def sumof(*args):
    sumnum = 0
    for object in args:
        if type(object) is int:
            sumnum = sumnum + object
    return sumnum


print(sumof(1, 3, 5, 5, -5,  "g", [1, 2, "a"]))


# 2


def does_everything(number, sumof=0, even_sum=0, odd_sum=0):
    for dummy in range(number+1):
        sumof = dummy + sumof
# or alternatively just return sum(range(number+1)
    for dummy in range(number+1):
        if dummy % 2 == 0:
            even_sum = even_sum + dummy
    for dummy in range(number+1):
        if dummy % 2 != 0:
            odd_sum = odd_sum + dummy
    return sumof, even_sum, odd_sum


print(f"sum of number : {does_everything(5)[0]}")
print(f"sum of even numbers : {does_everything(5)[1]}")
print(f"sum of odd numbers : {does_everything(5)[2]}")

# 3


def int_checker(user_input):
    try:
        user_input = int(user_input)
        print(user_input, "this is a number")

    except:

        print(0, "this is a string")


int_checker(input("Enter an integer\n"))
