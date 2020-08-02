"""

************
*          *
*          *
*          *
************

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a length 1.');
    if (width < 2) or (height < 2):
        raise Exception('"Width" or "Height" must be greater than 2.');
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('O', 15, 5)
