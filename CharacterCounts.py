import string

sentence = "His name was John, lived at 47 Main Street, and was only 23 years old."

isLower_int = 0
isUpper_int = 0
isNumeric_int = 0
isPunctiation_int = 0

for letter in sentence.strip():
    if letter.islower():
        isLower_int += 1
    if letter.isupper():
        isUpper_int += 1
    if letter.isnumeric():
        isNumeric_int += 1
    if letter in string.punctuation:
        isPunctiation_int += 1

isUpper_str = str(isUpper_int).rjust(5)
isLower_str = str(isLower_int).rjust(5)
isNumeric_str = str(isNumeric_int).rjust(5)
isPunctiation_str = str(isPunctiation_int).rjust(5)

print(str("Upper case").rjust(15),isUpper_str)
print(str("Lower").rjust(15),isLower_str)
print(str("Digits").rjust(15),isNumeric_str)
print(str("Punctuation").rjust(15),isPunctiation_str)