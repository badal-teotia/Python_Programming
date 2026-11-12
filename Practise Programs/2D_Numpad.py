# Making a 2D num pad.

gh = ((1,2,3),
      (4,5,6),
      (7,8,9),
      ('*',0,'#'))

for l in gh:
    for i in l:
        print(i, end = ' ')
    print()
    