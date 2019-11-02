def TopTenSquare():

    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1

values = TopTenSquare()

for i in values:
    print(i)
