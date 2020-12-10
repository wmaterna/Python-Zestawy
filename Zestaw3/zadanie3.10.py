dictionary = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
def roman2int():
    x = input("Enter number in roman: ")
    result = 0
    if isItRoman(x) == False:
        return -1
    for i in range(len(x)):
        if dictionary[x[i]] > dictionary[x[i - 1]] and i > 0 :
            result = result + dictionary[x[i]] - 2 * dictionary[x[i - 1]]
        else:
            result = result + dictionary[x[i]]
    return result

def isItRoman(roman_number):
    for i in range(len(roman_number)):
        if roman_number[i] not in dictionary:
            print("Not roman number symbol")
            return False
    return True


if __name__ == '__main__':
    returnedValue = roman2int()
    if returnedValue == -1:
        print("Conversion failed")
    else:
        print("Convertet result: " + str(returnedValue))

""""
 inne przykładowe sposoby na stowrzenie słownika:
 dictionary = dict (
    I = 1,
    V = 5,
    X = 10,
    L = 50,
    C = 100,
    D = 500,
    M = 1000
)

listOfRomanNumbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
listOfArabicNumbers = [1, 5, 10, 50, 100, 500, 1000]

"""

