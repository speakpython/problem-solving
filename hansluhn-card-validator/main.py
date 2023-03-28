#https://speakpython.codes/problem-solving/2023/03/27/hansluhn-card-validator.html#card-validation-in-python

def getDigit(number):
    if len(number) > 1:
        digitSum = 0
        for digit in number:
            digitSum += int(digit)
        return digitSum
    
    return int(number)

def sumOfDoubleEvenPlace(number):
    evenDigitSum = 0
    for i in range(1, len(number), 2):
        evenDigitSum += getDigit(str(int(number[i]) * 2))
        
    return evenDigitSum

def sumOfOddPlace(number):
    oddDigitSum = 0
    for i in range(0, len(number), 2):
        oddDigitSum += int(number[i])

    return oddDigitSum

#https://speakpython.codes/problem-solving/2023/03/27/hansluhn-card-validator.html#driver-code---isvalidnumber

def isValid(number):
    if 14 <= len(number) <= 16:
        number = number[::-1]
        if (sumOfOddPlace(number) + sumOfDoubleEvenPlace(number)) % 10 == 0:
            return True

    return False

#https://speakpython.codes/problem-solving/2023/03/27/hansluhn-card-validator.html#example-testing

number = '5105105105105100' #fictitious Mastercard Card Number
print(isValid(number))

#Output: True

number = '4556567890123456' #fictitious Visa Card Number
print(isValid(number))

#Output: True

number = '4559567990123456' #fictitious Visa Card Number
print(isValid(number))

#Output: False