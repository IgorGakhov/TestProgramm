def gcd(num1, num2):
    if num1 == 0:                                #1
        return num2
    elif num2 == 0:                              #1
        return num1
    elif num1 == num2:                           #1
        return num1
    elif num1 == 1:                              #2
        return 1
    elif num2 == 1:                              #2
        return 1
    elif num1 % 2 == 0 and num2 % 2 == 0:        #3
        return 2 * gcd(num1 // 2, num2 // 2)
    elif num1 % 2 == 0 and num2 % 2 != 0:        #4
        return gcd(num1 // 2, num2)
    elif num1 % 2 != 0 and num2 % 2 == 0:        #5
        return gcd(num1, num2 // 2)
    elif num1 % 2 != 0 and num2 % 2 != 0:
        if num2 > num1:
            return gcd((num2 - num1) // 2, num1) #6
        elif num2 < num1:
            return gcd((num1 - num2) // 2, num2) #7