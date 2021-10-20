def str_to_int(input_string):

    output_int = 0
    
    if input_string[0] == '-':
        is_negative = True
        start_idx = 1
    else:
        is_negative = False
        start_idx = 0

    for i in range(start_idx, len(input_string)):
        place = 10 ** (len(input_string) - (i+1))
        digit = ord(input_string[i]) - ord('0')
        output_int += place * digit
    
    if is_negative:
        return -1 * output_int
    else:
        return output_int

s = '-1234'
print(str(str_to_int("2") *  str_to_int("3")))