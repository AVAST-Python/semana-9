def estas_tocando_el_banjo_1(name):
    if name[0] == 'r' or name[0] == 'R':
        return name + ' toca el banjo'
    else:
        return name + ' no toca el banjo'



def estas_tocando_el_banjo_2(name):
    if name[0].upper() == 'R':
        return name + ' toca el banjo'
    else:
        return name + ' no toca el banjo'



def estas_tocando_el_banjo(name):
    if name[0].upper() == 'R': return name + ' toca el banjo'

    return name + ' no toca el banjo'



def estas_tocando_el_banjo(name):
    if name[0].upper() == 'R': return f'{name} toca el banjo'

    return f"{name} no toca el banjo"




print(estas_tocando_el_banjo('martin'))
print(estas_tocando_el_banjo('Raul'))
