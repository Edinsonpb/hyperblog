from ctypes.wintypes import INT


def main():

    nit = str(input("Digite el nit sin digito de verificación "))
    nit = nit.strip()
#    nit = nit.isdigit()
    dudn = nit[-2:]
    udn = nit[-1:]
    print(dudn)
    print(udn)


if __name__ == '__main__':
    main()