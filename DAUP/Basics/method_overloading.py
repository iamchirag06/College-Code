class Number:
    def __init__(self, value):
        self.value = value

    # +
    def __add__(self, other):
        return self.value + other.value

    # -
    def __sub__(self, other):
        return self.value - other.value

    # *
    def __mul__(self, other):
        return self.value * other.value

    # /
    def __truediv__(self, other):
        return self.value / other.value

    # ==
    def __eq__(self, other):
        return self.value == other.value

    # >
    def __gt__(self, other):
        return self.value > other.value

    # <
    def __lt__(self, other):
        return self.value < other.value


n1 = Number(20)
n2 = Number(10)

print("Addition =", n1 + n2)
print("Subtraction =", n1 - n2)
print("Multiplication =", n1 * n2)
print("Division =", n1 / n2)
print("Equal =", n1 == n2)
print("Greater Than =", n1 > n2)
print("Less Than =", n1 < n2)