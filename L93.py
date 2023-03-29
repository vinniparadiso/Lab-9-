#Vincenza Paradiso, Olivia Busk, and Rosemary Hoffman

def replace_substring(string, substring, replace):
    output= []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring :
            index += len(substring)
            output.append(replace)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))
replace_substring("Happy birthday to you, happy birthday to you", "birthday ", "life ")
