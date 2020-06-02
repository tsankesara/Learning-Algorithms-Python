# Iterative Solution
input_str = "HeyThere"
def str_len_itr(input_str):
    count = 0
    for i in range(len(input_str)):
      if input_str[i] != None:
         count = count + 1
    return count
print(str_len_itr(input_str))
# Recursive Solution
def rec_str_len(input_str):
    if input_str == "":
        return 0
    return 1 + rec_str_len(input_str[1:])

print(rec_str_len(input_str))