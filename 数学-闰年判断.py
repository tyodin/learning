for year in range (1000,2050):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print (year)