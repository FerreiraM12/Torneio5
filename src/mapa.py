'''

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

'''


def mapa(m):
    return (0,0,False,0)