def line (string1, string2):
    if type(string1) != str or type(string2) != str: 
        return 0
    if string1 == string2:
        return 1
    elif (string1 != string2):
        if (len(string1) > len(string2)):
            return 2
        if (string2 == 'learn'):
            return 3
        
    
print(line('1', '2'))
print(line('1', '1'))
print(line('123', '1'))
print(line('123', 'learn'))
