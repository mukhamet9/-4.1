from fake_math import fake_divide1 as fd1
from fake_math import fake_divide2 as fd2
from true_math import true_divide1 as td1
from true_math import true_divide2 as td2

result_1 = fd1(69, 3)
result_2 = fd2(3, 0)
result_3 = td1(49, 7)
result_4 = td2(15, 0)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
