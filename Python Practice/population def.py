def main():
    def describeTask():
        print('This program displays the population')
        print('The density of the last state to become')
        print('part of the United States.\n')

    describeTask()

    def calculateDensity(state, pop, landArea):
        density= pop/landArea
        print('The density of', state, 'is')
        print('{0:,2f} people per square mile.'.format(density))
    
    calculateDensity('Hawaii', 1375000, 6423)

main()
