def is_valid_walk(walk):
    coord_x = 0
    coord_y = 0

    time = 0
    directions = ['n', 's', 'e', 'w']
    for char in walk:
        if char in directions:
            time += 1
            if char == 'n':
                coord_y += 1
            elif char == 's':
                coord_y -= 1
            elif char == 'e':
                coord_x += 1
            else:
                coord_x -= 1
    if time == 10 and coord_x == 0 and coord_y == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))
