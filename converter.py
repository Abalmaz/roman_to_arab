# define two tuples with a list of Roman and Arabic numbers,
# where the indices of equal values coincide
roman = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I', '(', ')')
arab = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

def convert(n):
    if n in roman:
        return arab[roman.index(n)]
    elif n in arab:
        return roman[arab.index(n)]
    else:
        return "Sorry, you entered not roman or arabic number"

def roman_to_arab(num):
    result, i = 0, 0
    while i < len(num):
        curr_val = 0
        if i < len(num)-1 and convert(num[i]) < convert(num[i+1]):
            curr_val = num[i] + num[i+1]
            i += 2
        else:
            curr_val = num[i]
            i += 1

        if curr_val in roman:
            result += convert(curr_val)
        else:
            return "Incorrect roman numeral"
    return result

def arab_to_roman(num):
    result = ''
    for i in range(len(arab)):
        while (num%arab[i] < num):
            result += roman[i]
            num -= arab[i]
    return result

def big_arab_to_roman(num):
    thousands = num//1000
    remainder = num%1000
    thousands_to_roman = "({})".format(arab_to_roman(thousands))
    remainder_to_roman = arab_to_roman(remainder)
    return thousands_to_roman + remainder_to_roman


def main():
    number = input("Enter roman or arab numeral: ")
    lenght = len(number)
    n = 0

    # check entered number, if all symbol is roman
    for i in range(lenght):
        if number[i] in roman:
            n += 1
    if n == lenght:
        if '(' in number and ')' in number:
            parts = number[1:].split(')')
            thousands = roman_to_arab(parts[0])*1000
            remainder = roman_to_arab(parts[1])
            print (thousands+remainder)
        else:
            print (roman_to_arab(number))

    # if entered number not Roman, try convert to decimal
    else:
        try:
            num = int(number)
            if num < 4000:
                print (arab_to_roman(num))
            else:
                print (big_arab_to_roman(num))

        except ValueError:
            print("Oops, some thing wrong, your enter not roman or arabic number")



if __name__ == "__main__":
    main()