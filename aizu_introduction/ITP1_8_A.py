# fAIR, LATER, OCCASIONALLY CLOUDY.

# Fair, later, occasionally cloudy.

s = input()

new_string = ""
for i in s:
    if i.isupper():
        new_string += i.lower()
    elif i.islower():
        new_string += i.upper()
    else:
        new_string += i
print(new_string)