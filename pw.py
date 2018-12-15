tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    maxAll = []
    max = 0
    for r in range(len(table)):
        for c in range(len(table[0])):
            if len(table[r][c]) > max:
                max = len(table[r][c])
        maxAll.append(max)
        max = 0

        for row in

print(tableData)

str1 = 'test\ntest\ntest\ntest '
str2 = 'test\ntest\ntest\ntest '

print(str1, end=' ')
print(str2.rjust(80), end=' ')