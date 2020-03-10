def biggest_guy(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print(num1)
        else:
            print(num3)
    elif num2 > num3:
        print(num2)
    else:
        print(num3)
biggest_guy(10, 3, 2) 
