from math import log

first_num = int(input())
second_num = int(input())

if second_num <= 0 or second_num == 1:
    log_value = log(first_num)
else:
    log_value = log(first_num, second_num)

print(round(log_value, 2))