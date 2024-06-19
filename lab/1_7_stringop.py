# Write a menu-driven program that performs the following operations on
# strings
#     Check if the String is a Substring of Another String
#     Count Occurrences of Character
#     Replace a substring with another substring
#     Convert to Capital Letters

def substring(str,n):
    if n in str:
        return True
def occurences(str,char):
    return str.count(char)
def replace_string(str,char1,char2):
    return str.replace(char1,char2)
def uupper(str):
    return str.upper()

while True:
    print("\nString Operations Menu:")
    print("1. Check Substring")
    print("2. Count Character Occurrences")
    print("3. Replace Substring")
    print("4. Convert to Uppercase")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        str = input("Enter the main string: ")
        n = input("Enter the substring to check: ")
        if substring(str,n):
            print("substring present")
    elif choice == 2:
        str = input("Enter the main string: ")
        n = input("Enter the character: ")
        o=occurences(str,n)
        print("occurence of {n} is {o}")
    elif choice == 3:
        str = input("Enter the main string: ")
        n = input("Enter the word to be replaced : ")
        m = input("Enter the word to be replaced with: ")
        r=replace_string(str,n,m)
        print("new string : {r}")
    elif choice == 4:
        str = input("Enter the main string in lower case: ")
        u = uupper(str)
        print(u)
        break 