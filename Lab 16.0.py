string1 = input("Enter a string consisting of A, T, C, and/or G")
string2 = input("Enter a string consisting of A, T, C, and/or G")

dict = {'A': 'Add an indel', 'D': 'Delete an indel.', 'S': 'Score', 'Q': 'Quit'}
print(dict)

def(dict):
    option = input("Choose a command")
    if option in dict:
