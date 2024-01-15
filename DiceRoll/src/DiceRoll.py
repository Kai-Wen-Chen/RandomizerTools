import random

class DiceRoll(object):
    def __init__(self) -> None:
        self._minValue = 1
        self._maxValue = 6
        pass

    def roll(self, time: int) -> list():
        result = list()
        for i in range(time):
            result.append(random.randint(self._minValue, self._maxValue))
        return result
    
    def setDiceValue(self, minValue: int, maxValue: int) -> None:
        self._minValue = minValue
        self._maxValue = maxValue

    def begin(self) -> bool:
        print(f'Current dice value: {self._minValue} ~ {self._maxValue}')
        option = input('Input \"r\" to roll dice, \"s\" to set the dice value, or \"q\" to quit: ')
        if option == 'r' or option == 'R':
            time = input('How many dices (1 ~ 100, or 0 to quit) do you want to roll?: ')
            if not str.isdigit(time):
                print('Invalid input, please try again')
                return self.begin()
        
            time = int(time)
            if time == 0:
                print('quit')
                return False
            elif 1 <= time <= 100:
                print(self.roll(time))
                return True
            else:
                print('Invalid input, please try again')
                return self.begin()
            
        elif option == 's' or option == 'S':
            minValue = input('Input the min value of dice (0 ~ 10000): ')
            if not str.isdigit(minValue) or not (0 <= int(minValue) <= 10000):
                print('Invalid input, please try again')
                return self.begin()
            
            maxValue = input('Input the max value of dice (0 ~ 10000): ')
            if not str.isdigit(maxValue) or not (0 <= int(maxValue) <= 10000) or minValue > maxValue:
                print('Invalid input, please try again')
                return self.begin()
            
            self.setDiceValue(int(minValue), int(maxValue))
            return self.begin()
        
        elif option == 'q' or option == 'Q':
            print('quit')
            return False
        
        else:
            print('Invalid option, please try again')
            return self.begin()


if __name__ == '__main__':
    dice_roll = DiceRoll()
    while dice_roll.begin():
        pass
