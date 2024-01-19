#1.a
print("ex 1")
from functools import reduce

def este_palindrom(s):
    return s.lower() == s[::-1].lower()

def count_palindrom(underage, practic):
    try:
        with open(practic, 'r') as file:
            people = map(lambda line: line.strip().split(','), file)
            if underage:
                palindrom_underage = filter(lambda p: este_palindrom(p[0]) and int(p[1]) < 18, people)
                return reduce(lambda count, _: count + 1, palindrom_underage, 0)
            else:
                palindrom = filter(lambda p: este_palindrom(p[0]), people)
                return reduce(lambda count, _: count + 1, palindrom, 0)
    except FileNotFoundError:
        print(f" '{practic}' nu exista.")
    except Exception as e:
        print(f"Exista o gresala: {e}")

file_name = "people.txt"
print(f"Numarul de oameni sub 18 ani cu un nume palindorm din fisier: {count_palindrom(True, file_name)}")
print(f"Toate numele palindroame din fisier: {count_palindrom(False, file_name)}")

#1.b
def test_count_palindrom_underage_true():
    result = count_palindrom(True, 'test_people.txt')
    assert result == 6, f"Erwartet: 6, Erhalten: {result}"
    print("Testfall 'underage=True' bestanden.")

def test_count_palindrom_underage_false():
    result = count_palindrom(True, 'test_people.txt')
    assert result == 6, f"Erwartet: 6, Erhalten: {result}"
    print("Testfall 'underage=False' bestanden.")

#2
print("ex 2")
class BinaryNumber:
    def __init__(self, number_string: str):
        self.number_string = number_string
        self.numberList = [int(digit) for digit in self.number_string]

    def __str__(self):
        return f'BinaryNumber {self.number_string}'

    def sum(self, number, return_list: bool):
        number1 = list(reversed(self.numberList))
        number2 = list(reversed(number.numberList))
        if return_list:
            cf = 0
            new_number = []
            if len(number1) > len(number2):
                maxim = number1
            else:
                maxim = number2
            for index in range(len(maxim)):
                if index < min(len(number1), len(number2)):
                    digit_on_pos = number1[index] + number2[index] + cf
                else:
                    digit_on_pos = maxim[index] + cf

                if digit_on_pos > 1:
                    cf = 1
                    digit_on_pos = 0
                else:
                    cf = 0

                new_number.append(digit_on_pos)

            if cf == 1:
                new_number.append(1)

            return new_number[::-1]
        else:
            cf = 0
            new_number = []
            if len(number1) > len(number2):
                maxim = number1
            else:
                maxim = number2
            for index in range(len(maxim)):
                if index < min(len(number1), len(number2)):
                    digit_on_pos = number1[index] + number2[index] + cf
                else:
                    digit_on_pos = maxim[index] + cf

                if digit_on_pos > 1:
                    cf = 1
                    digit_on_pos = 0
                else:
                    cf = 0

                new_number.append(digit_on_pos)

            if cf == 1:
                new_number.append(1)

            numberString = ''.join(map(str, reversed(new_number)))
            return numberString


binary_number1 = BinaryNumber("101")
binary_number2 = BinaryNumber("1110")
binary_number3 = BinaryNumber('1001')
res_sum = binary_number1.sum(binary_number2, True)
res_sum2 = binary_number1.sum(binary_number2, False)
print('Suma in lista', res_sum)
print('Suma in string', res_sum2)
#b
class RepoBinaryNumber:
    def __init__(self):
        self.binarynumbers = []

    def sum_all(self):
        if len(self.binarynumbers) == 1:
            number1 = self.binarynumbers[0]
            return BinaryNumber.sum(BinaryNumber('0'), number1, False)
        elif len(self.binarynumbers) == 2:
            number1 = self.binarynumbers[0]
            number2 = self.binarynumbers[1]
            return BinaryNumber.sum(number1, number2, False)

    def add(self, number: BinaryNumber):
        if number.numberList[-1] == 1:
            self.binarynumbers.append(number)


repo_binary_number = RepoBinaryNumber()
repo_binary_number.add(binary_number1)
repo_binary_number.add(binary_number2)
repo_binary_number.add(binary_number3)
print('Suma numerelor impare: ', repo_binary_number.sum_all())

