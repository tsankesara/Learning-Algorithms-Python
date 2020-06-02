
input_str_1 = "HelloLLLs"
def find_uppercase_iterative(input_str, rangestr):
    for i in range(rangestr):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found"

def find_uppercase_rec(input_str, Index=0):
    if input_str[Index].isupper():
        return input_str[Index]
    if Index == len(input_str) - 1:
        return "No uppercase found"
    return find_uppercase_rec(input_str, Index+1)

print(find_uppercase_rec(input_str_1))