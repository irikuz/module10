from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self._enemies_left = 100

    def run(self):
        print(f'{self.name}, на нас напали!' + '\n')

        days = 0
        while self._enemies_left > 0:

            days += 1
            sleep(1)
            self._enemies_left -= self.power
            print(f"{self.name} сражается {days} дней , осталось {self._enemies_left} воинов.")
            if self._enemies_left <= 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
