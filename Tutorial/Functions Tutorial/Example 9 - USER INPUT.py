state= input('Enter a name for a city (e.g: Hawaii): ')
pop= int(input('Enter the population value of the city (e.g: 1375000): '))
landArea= int(input('Enter a value for the land area (e.g: 6423): '))

def main():
    describeTask()
    calculateDensity(state, pop, landArea)

def describeTask():
    print('This program displays the population')
    print('Density of the last state to become')
    print('part of the United States. \n')

def calculateDensity(state, pop, landArea):
    density= pop/landArea
    print('The density of', state, 'is')
    print("{0:,.2f} people per square mile.".format(density))

main()
