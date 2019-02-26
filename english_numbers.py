# Yash Mistri
# Translates a number to the English phrase

# keywords used to create the number phrase
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = [' ', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousands = [' ', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion']


def print_eng_num(n):
    if n == 0:
        return 'zero'
    result = ''
    placeCounter = 1

    while n > 0:
        #converts the 2 places left of the comma to english
        if (placeCounter - 1) % 3 == 0:
            #01 to 09
            if n % 100 <= 9 and n % 100 >= 1:
                result = ' '.join([ones[n % 100], thousands[(placeCounter - 1) // 3], result])

            #10 to 19
            elif n % 100 >= 10 and n % 100 <= 19:
                result = ' '.join([teens[n % 100 - 10], thousands[(placeCounter - 1) // 3], result])

            #20 to 99
            elif n % 100 >= 20:
                result = ' '.join([tens[n % 100 // 10 - 1], \
                            (ones[n % 10] if n%10 > 0 else ''), \
                            thousands[(placeCounter - 1) // 3], \
                            result])

            elif n % 1000 > 0 and placeCounter>3:
                
                result = ' '.join([thousands[(placeCounter - 1) // 3], result])

            placeCounter += 2
            n = n//100
            continue


        #converts the place to the right of the comma to english
        elif placeCounter % 3 == 0 and n % 10 != 0:
            result = ' '.join([ones[n % 10], 'hundred', result])
            placeCounter += 1
            n = n//10
        else:
            placeCounter += 1
            n = n//10
    return result
