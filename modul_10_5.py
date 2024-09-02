import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf8') as fyle_my:
        while True:
            con_text = fyle_my.readline()
            if not con_text:
                break
            all_data.append(con_text)

files = ["file 1.txt","file 2.txt","file 3.txt","file 4.txt"]


if __name__ == '__main__':
    start = datetime.now()
    for file in files:
        read_info(file)
    print(f"Время линейного метода {datetime.now() - start}")

    start = datetime.now()
    with multiprocessing.Pool(processes=4) as poo:
        poo.map(read_info,files)

    print(f"Время мультипроцессорного метода {datetime.now() - start}")