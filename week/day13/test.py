for x in range(1, 10):
    for y in range(1, 10):
        z = x * y
        if x >= y:
            print('{y} * {x} = {z}'.format(x=x, y=y, z=z),end='  ')
        else:
            print('\n')
            break