"""

Neste torneio pretende-se que implemente uma função para validar o mapa
de um arquipélago.

O mapa (rectangular e quadriculado) é constituído por um conjunto de ilhas
e por mar, sendo representado por uma lista de strings onde o caracter '.'
representa uma quadrícula de terra (parte de uma ilha) e o caracter '#'
uma quadrícula de mar. Uma ilha é um conjunto de quadrículas de terra
acessíveis entre si. É possível aceder de uma quadrícula a outra se forem
vizinhas na horizontal ou na vertical. As ilhas podem também ter quadrículas
com um digito, digito esse que representa uma quadrícula de terra mas também a
dimensão da ilha (em quadrículas).

Uma ilha está bem representada no mapa se contem exactamente um digito com a
sua dimensão correcta. Um mapa está correcto se todas as ilhas estão bem
representadas e se apenas existe um mar (todas as quadrículas de mar são
acessíveis entre si).

A função deve devolver um tuplo com a seguinte informação (por esta ordem):
- Número de ilhas bem representadas
- Número de ilhas mal representadas
- Um booleano que indica se existe apenas um mar.
- O número mínimo de caracteres que seria preciso alterar para que o mapa
  estivesse correcto.

Note que se não existirem ilhas mal representadas e existir apenas um mar este
último número deverá ser 0. Nos testes a realizar este número, quando não 0,
será tipicamente bastante pequeno.

"""


def mapa(m):
    global leny
    global lenx
    leny = len(m)
    lenx = len(m[0])
    lm = percorreMapa(m)  # (mar, listaIlhas)
    listaIlhas = lm[1]
    qMar = lm[0]
    marUnico = initPercorreMar(m, qMar)
    bemRep = 0
    malRep = 0
    for ilha in listaIlhas:
        if len(ilha.digits) == 1 and ilha.digits[0][0] == len(ilha.pontos):
            bemRep += 1
        else:
            malRep += 1
    if malRep > 0:
        alterar = 1
    else:
        alterar = 0

    return (bemRep,malRep,marUnico,alterar)


class ilha:
    def __init__(self, pontos, digits, visitados):
        self.pontos = pontos
        self.digits = digits
        self.visitados = visitados


#  Percorre o mapa, sempre que encontra uma QIlha usa a função initcontaQilha para
#  criar um objeto ilha e colocar na lista de ilhas. Esta função também devolve quantos QMar existem
def percorreMapa(m):
    listaDeIlhas = []
    visitados = []
    qMar = 0
    for y in range(leny):
        for x in range(lenx):
            if not ((y, x) in visitados) and m[y][x] != '#':
                umaIlha = initcontaQIlha(m, y, x)
                visitados.extend(umaIlha.visitados)
                listaDeIlhas.append(umaIlha)
            if m[y][x] == '#':
                qMar += 1
    return qMar, listaDeIlhas


def initcontaQIlha(m, y, x):
    visitados = [(y, x)]
    qIlha = [(y, x)]
    digit = []
    if m[y][x].isdigit():
        digit.append((int(m[y][x]), (y, x)))

    def contaQIlha(m, y, x):

        if 1 <= y <= leny and 0 <= x <= lenx - 1:  # y-1, x
            if m[y - 1][x] != '#' and not ((y - 1, x) in visitados):
                visitados.append((y - 1, x))
                qIlha.append((y - 1, x))
                if m[y - 1][x].isdigit():
                    digit.append((int(m[y - 1][x]), (y - 1, x)))
                contaQIlha(m, y - 1, x)
            elif m[y - 1][x] == '#' and not ((y - 1, x) in visitados):
                visitados.append((y - 1, x))

        if - 1 <= y <= leny - 2 and 0 <= x <= lenx - 1:  # y+1, x
            if m[y + 1][x] != '#' and not ((y + 1, x) in visitados):
                visitados.append((y + 1, x))
                qIlha.append((y + 1, x))
                if m[y + 1][x].isdigit():
                    digit.append((int(m[y + 1][x]), (y + 1, x)))
                contaQIlha(m, y + 1, x)
            elif m[y + 1][x] == '#' and not ((y + 1, x) in visitados):
                visitados.append((y + 1, x))

        if 0 <= y <= leny - 1 and 1 <= x <= lenx:  # y, x-1
            if m[y][x - 1] != '#' and not ((y, x - 1) in visitados):
                visitados.append((y, x - 1))
                qIlha.append((y, x - 1))
                if m[y][x - 1].isdigit():
                    digit.append((int(m[y][x - 1]), (y, x - 1)))
                contaQIlha(m, y, x - 1)
            elif m[y][x - 1] == '#' and not ((y, x - 1) in visitados):
                visitados.append((y, x - 1))

        if 0 <= y <= leny - 1 and -1 <= x <= lenx - 2:  # y, x+1
            if m[y][x + 1] != '#' and not ((y, x + 1) in visitados):
                visitados.append((y, x + 1))
                qIlha.append((y, x + 1))
                if m[y][x + 1].isdigit():
                    digit.append((int(m[y][x + 1]), (y, x + 1)))
                contaQIlha(m, y, x + 1)
            elif m[y][x + 1] == '#' and not ((y, x + 1) in visitados):
                visitados.append((y, x + 1))

    contaQIlha(m, y, x)
    return ilha(qIlha, digit, visitados)


def initPercorreMar(m, mar):
    x = 0
    y = 0
    visitados = []
    for y in range(leny):
        for x in range(lenx):
            if m[y][x] == '#':
                mar -= 1
                visitados.append((y, x))
                break
            visitados.append((y, x))
        else:
            continue
        break

    def percorreMar(m, y, x):
        nonlocal mar
        if 1 <= y <= leny and 0 <= x <= lenx - 1:
            if m[y - 1][x] == '#' and not ((y - 1, x) in visitados):
                mar -= 1
                visitados.append((y - 1, x))
                percorreMar(m, y - 1, x)
            elif not ((y - 1, x) in visitados):
                visitados.append((y - 1, x))

        if - 1 <= y <= leny - 2 and 0 <= x <= lenx - 1:
            if m[y + 1][x] == '#' and not ((y + 1, x) in visitados):
                mar -= 1
                visitados.append((y + 1, x))
                percorreMar(m, y + 1, x)
            elif not ((y + 1, x) in visitados):
                visitados.append((y + 1, x))

        if 0 <= y <= leny - 1 and 1 <= x <= lenx:
            if m[y][x - 1] == '#' and not ((y, x - 1) in visitados):
                mar -= 1
                visitados.append((y, x - 1))
                percorreMar(m, y, x - 1)
            elif not ((y, x - 1) in visitados):
                visitados.append((y, x - 1))

        if 0 <= y <= leny - 1 and -1 <= x <= lenx - 2:
            if m[y][x + 1] == '#' and not ((y, x + 1) in visitados):
                mar -= 1
                visitados.append((y, x + 1))
                percorreMar(m, y, x + 1)
            elif not ((y, x + 1) in visitados):
                visitados.append((y, x + 1))

    percorreMar(m, y, x)
    if mar > 0:
        return False
    return True
