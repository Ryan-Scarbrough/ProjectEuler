retarded = {
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
}

sum0 = 0
for i in range(1, 10):
    sum0 += len(retarded[i])
sum0 = sum0*190 #################

sum1 = 0
for i in range(10, 20):
    sum1 += len(retarded[i])
sum1 = sum1*10 #################

sum2 = 0
for i in range(20, 100, 10):
    sum2 += len(retarded[i])
sum2 = sum2*100 #################

three_digits = len("hundred")*900 #################

nd = len("and")*891 #################
thousand = len("onethousand")

print(sum([sum0, sum1, sum2, three_digits, nd, thousand]))
