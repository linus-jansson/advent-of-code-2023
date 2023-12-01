
inp = ""

f = open("input.txt", "r")
inp = f.readlines()
f.close()

digit_list = []

for line in inp:
    digit_string = ""
    for char in line:
        # If char is a digit 
        if char.isdigit():
            # If length of tmp is longer or equal than 2,
            # We replace the last digit with the current digit
            if len(digit_string) >= 2:
                digit_string = digit_string[:-1]
                digit_string += char
            else: 
                digit_string += char
    # If the line only contains one digit we add the same again
    if len(digit_string) == 1:
        digit_string = digit_string*2

    digit_string = int(digit_string)
    digit_list.append(digit_string)
        
print(digit_list)
print(sum(digit_list))