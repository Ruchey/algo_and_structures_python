"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HEX:
    def ltn(self, l):
        "letter to number"
        if l.isalpha():
            l.upper()
            letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
            return letters[l]
        return int(l)

    def ntl(self, n):
        "Convert a number to a letter"
        if n < 10:
            return n
        if n > 15:
            return 0
        nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        return nums[n]

    def dec_to_hex(self, n):
        nums = []
        while n > 15:
            nums.append(n % 16)
            n = int(n / 16)
        nums.append(n)
        nums.reverse()
        to_hex = []
        for i in nums:
            to_hex.append(str(self.ntl(i)))
        return "".join(to_hex)

    def __init__(self, h):
        nums = list(h)
        deg = len(nums) - 1
        # 19F = 1*16^2 + 9*16^1 + F*16^0
        dec = 0
        for i in nums:
            dec += self.ltn(i)*16**deg
            deg -= 1
        self.num = dec

    def __add__(self, obj):
        self.summ = self.num + obj.num
        return self.dec_to_hex(self.summ)

    def __mul__(self, obj):
        self.mult = self.num * obj.num
        return self.dec_to_hex(self.mult)


a = HEX('A2')
b = HEX('C4F')
c = a + b
d = a * b

print(c)
print(d)
