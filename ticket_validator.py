def validate_ticket(code):
    numbersOfCode = code[3:8]
    num = int(numbersOfCode)
    return (len(code) == 8) and code[0:2] == 'TX'
def get_ticket_tier(code):
    if code[2] == '0' or code[2] == '1' or code[2] == '2' or code[2] == '3' and validate_ticket(code) is True:
        return 'General'
    elif code[2] == '4' or code[2] == '5' or code[2] == '6' and validate_ticket(code) is True:
        return 'VIP'
    elif code[2] == '7' or code[2] == '8' or code[2] == '9' and validate_ticket(code) is True: 
        return 'Platinum'
    else: 
        raise ValueError 
def calculate_total(prices, discount=0):
    if (not isinstance(prices, list)):
        raise TypeError
    elif (discount > 1 or discount < 0):
        raise ValueError
    else:
        total = 0 
        for(i in prices):
            total += i 
        return total
