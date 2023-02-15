def count(year):
    yearsNums = []
    for i in year:
        yearsNums.append(int(i))
    for i in yearsNums:
        if yearsNums.count(i) > 1:
            return False
    return True


year = input()
year = int(year) + 1
year = str(year)
while count(year) != True:
    year = int(year) + 1
    year = str(year)
print(year)
# 1000 => 1001 => 1002 => 1012 => 1022 => 1023 1
# 1111
# 1001
# 1231
# 1110
# 1234
# 1987 => 2013   11
# 2013 => 2014 5
# 2000 => 2
#
#
#
#
#
