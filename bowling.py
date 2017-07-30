# Returns the score of a bowling game
def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i].upper() == 'X':
                result += get_value(game[i+1])
                in_first_half = False
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not in_first_half:
            frame += 1
            in_first_half = True
        else:
            in_first_half = False
    return result


# Returns the value in number of a character.
def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char.upper() == 'X':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
