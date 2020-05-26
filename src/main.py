##
# Main function of the Python program.
#
##

from src.mapa import mapa


def main():
    print("<h3>mapa</h3>")
    m = ['....',
         '.###',
         '.7#4',
         '###.',
         '#.#.',
         '.3#.']
    print("in:")
    print('\n'.join(m))
    print("out:")
    print(mapa(m))


if __name__ == '__main__':
    main()