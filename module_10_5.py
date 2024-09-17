from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, encoding="utf-8") as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time_1 = datetime.now()

    for filename in filenames:
        read_info(filename)

    end_1 = datetime.now()
    print(f"Линейное выполнение заняло {end_1 - start_time_1} секунд")

    with multiprocessing.Pool(processes=8) as pool:
        start_time_2 = datetime.now()
        pool.map(read_info, filenames)
    end_2 = datetime.now()
    print(f"Многопроцессорное выполнение заняло {end_2 - start_time_2} секунд")
