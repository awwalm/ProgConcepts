def circleArea(r):
    area= 3.14 * r * r
    print('the area of a circle of radius ', r, ' is ', area, 'centimetres squared ', sep=' ')

def mainArea():
    circleArea(14)
    circleArea(13)
    radius=int(input('Enter the number for the radius of a circle: '))
    circleArea(radius)

mainArea()
