pop= 300000
print('{0:10}{1}'.format('year', 'population'))
for year in range(2014, 2019):
    print('{,<10d}{,d}'/format(year, round(pop)))
    pop+= 0.03 * pop
