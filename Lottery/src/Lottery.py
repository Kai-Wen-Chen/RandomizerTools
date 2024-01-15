import random

class Lottery(object):
    def __init__(self) -> None:
        self._minValue = 1
        self._maxValue = 100
    
    def pick(self, time: int) -> list():
        pool = [x for x in range(self._minValue, self._maxValue + 1)]
        result = random.sample(pool, k=time)

        return result
    
    def setLotteryRange(self, minValue: int, maxValue: int) -> None:
        self._minValue = minValue
        self._maxValue = maxValue

    def begin(self) -> bool:
        print(f'Current lottery range: {self._minValue} ~ {self._maxValue}')
        option = input('Input \"p\" to pick lottery, \"s\" to set the lottery range, or \"q\" to quit: ')
        if option == 'p' or option == 'P':
            time = input(f'How many numbers (1 ~ {self._maxValue - self._minValue + 1}, or 0 to quit) do you want to pick?: ')
            if not str.isdigit(time):
                print('Invalid input, please try again')
                return self.begin()
        
            time = int(time)
            if time == 0:
                print('quit')
                return False
            elif 1 <= time <= self._maxValue - self._minValue + 1:
                print(self.pick(time))
                return True
            else:
                print('Invalid input, please try again')
                return self.begin()
            
        elif option == 's' or option == 'S':
            minValue = input('Input the min value of lottery (1 ~ 10000): ')
            if not str.isdigit(minValue) or not (1 <= int(minValue) <= 10000):
                print('Invalid input, please try again')
                return self.begin()
            
            maxValue = input('Input the max value of lottery (1 ~ 10000): ')
            if not str.isdigit(maxValue) or not (1 <= int(maxValue) <= 10000) or minValue > maxValue:
                print('Invalid input, please try again')
                return self.begin()
            
            self.setLotteryRange(int(minValue), int(maxValue))
            return self.begin()
        
        elif option == 'q' or option == 'Q':
            print('quit')
            return False
        
        else:
            print('Invalid option, please try again')
            return self.begin()



if __name__ == '__main__':
    lottery = Lottery()
    while lottery.begin():
        pass
