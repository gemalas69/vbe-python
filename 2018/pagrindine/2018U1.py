from math import floor

def main():
    with open('./2018/pagrindine/U1.txt', 'r') as f:
        duomenys = [line.strip() for line in f.readlines()]
        kruveliu_skaicius = int(duomenys[0])
        duomenys.pop(0)
    if kruveliu_skaicius < 1 or kruveliu_skaicius > 30:
        return
    juosteliu_duom = {}

    for line in duomenys:
        spalva, juosteliu_kiekis = line.split(' ')
        if spalva not in juosteliu_duom.keys():
            juosteliu_duom[spalva] = int(juosteliu_kiekis)
        else:
            juosteliu_duom[spalva] += int(juosteliu_kiekis)
    veliaveliu_skaicius = str(floor(min(juosteliu_duom.values()) / 2))

    with open('./2018/pagrindine/U1rez.txt', 'w') as f:
        maziausias_juost_sk = min(juosteliu_duom.values())
        f.write(f'{veliaveliu_skaicius}\n')
        for spalva in 'GZR':
            f.write(f'{spalva} {juosteliu_duom[spalva] - maziausias_juost_sk}\n')


main()