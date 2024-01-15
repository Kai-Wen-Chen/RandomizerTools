import random

class CoinToss(object):
    def __init__(self) -> None:
        pass

    def toss(self, times : int) -> list:
        result = list()
        for i in range(times):
            result.append(random.randint(0,1))
        return result
    
    def begin(self) -> bool:
        time = input('How many coins (1 ~ 100, or 0 to quit) do you want to toss?: ')
        if not str.isdigit(time):
            print('Invalid input, please try again')
            return self.begin()
        
        time = int(time)
        if time == 0:
            print('quit')
            return False
        elif 1 <= time <= 100:
            print(self.toss(time))
            return True
        else:
            print('Invalid input, please try again')
            return self.begin()        


if __name__ == '__main__':
    coin_toss = CoinToss()
    while coin_toss.begin():
        pass
