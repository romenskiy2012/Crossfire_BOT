from time import strftime, localtime, sleep #Для (Time)
print("Модуль tic подключлн")


def test(Date, Time):
    F = []
    F2 = []
    F.extend(Date)
    print(F)
    A = ""
    for Flist in F:
        if Flist == ":":
            F2.append(A)
            A = ""
        else:
             A = f"{A}{Flist}"
    F2.append(A)
    G1 = F2[0]
    G2 = F2[1]
    G3 = F2[2]
    print(f'{int(G1)} - {int(strftime("%Y"))}') # Год
    print(f'{int(G2)} - {int(strftime("%m"))}') # Месяц
    print(f'{int(G3)} - {int(strftime("%d"))}') # День

    if (int(G1) <= int(strftime("%Y"))):
        if ((int(G2) == int(strftime("%m"))) and (int(G3) < int(strftime("%d"))) or (int(G2) < int(strftime("%m")))):
            print("Просрочено")
            return (True)
        if ((int(G2) == int(strftime("%m"))) and (int(G3) == int(strftime("%d")))):


            F = []
            F.extend(Time)
            F2 = []
            A = ""
            for Flist in F:
                if Flist == ":":
                    F2.append(A)
                    A = ""
                else:
                    A = f"{A}{Flist}"
            F2.append(A)
            G1 = F2[0]
            G2 = F2[1]
            print(f'{int(G1)} - {int(strftime("%H"))}')
            print(f'{int(G2)} - {int(strftime("%M"))}')
            if (((int(G1) == int(strftime("%H"))) and (int(G2) <= int(strftime("%M")))) or (int(G1) < int(strftime("%H")))):
                print("Просрочено")
                return (True)
            else:
                print("Ешё годен2")
                return (False)
        else:
            print("Ешё годен1")
            return (False)
