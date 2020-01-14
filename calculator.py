import pdb


class Calculator:
    m_sing = True
    def convert(self, number):
        aNumber = []
        reverse_number = number[::-1]
        if number[0] == '-':
            reverse_number = number[:-2:-1]
            self.m_sing = not self.m_sing
        else:
            reverse_number = number[::-1]

        for char in reverse_number:
            aNumber.append(char)

        return list(map(int, aNumber))

    def decode(self, number):
        sign = 1
        if number[-1] ==  '*':
            number.pop(len(number) - 1)
            sign = -1

        decoded_number = ""
        reverse_number = number[::-1]
        for number in reverse_number:
            decoded_number += str(number)

        decoded_number = int(decoded_number)

        decoded_number = decoded_number * sign
        if not self.m_sing:
            decoded_number *= -1
        return decoded_number

    def is_greater(self, A, B, base=10):

        decimal_sum_A = 0
        decimal_sum_B = 0

        for i in range(len(A)):
            decimal_sum_A += A[i]*pow(base, i)

        for i in range(len(B)):
            decimal_sum_B += B[i]*pow(base, i)


        if decimal_sum_A >= decimal_sum_B:
            return True

        return False

    def add(self, A, B, base=10):
        tmp = len(A)

        if len(A) != len(B):
            tmp = max(len(A), len(B))
        for i in range(len(A), tmp + 1, 1):
            A.append(0)
        for i in range(len(B), tmp + 1, 1):
            B.append(0)
        result = []

        for i in range(tmp + 1):
            result.append(0)

        for i in range(tmp):
            sum = result[i] + A[i] + B[i]
            result[i] = sum % base
            if sum >= base:
                result[i + 1] = sum - (sum - 1)

        j = len(result) - 1
        while (result[j] == 0):
            result.pop(j)
            j -= 1
        return result

    def substract(self, A, B, base=10):
        tmp = len(A)
        minus = False

        if not self.is_greater(A, B, base=base):
            A_temp = B.copy()
            B_temp = A.copy()
            minus = True


        if len(A_temp) != len(B_temp):
            tmp = max(len(A_temp), len(B_temp))
        for i in range(len(A_temp), tmp + 1, 1):
            A_temp.append(0)
        for i in range(len(B_temp), tmp + 1, 1):
            B_temp.append(0)
        result = []

        for i in range(tmp + 1):
            result.append(0)

        for i in range(tmp):
            sum = A_temp[i] - B_temp[i]
            if sum < 0:
                A_temp[i + 1] -= 1
                sum = base + A_temp[i] - B_temp[i]
            result[i] = sum


        if base != 2:
            j = len(result) - 1
            while (result[j] == 0):
                result.pop(j)
                j -= 1
        if minus:
            result.append('*')
        return result

    def multiply(self, A, B):
        dlA = len(A)
        dlB = len(B)
        result = []

        for i in range(dlA + dlB):
            result.append(0)

        for i in range(dlA):
            for j in range(dlB):
                sum = result[i+j] + A[i]*B[j]
                result[i+j] = int(sum%10)
                result[i+j+1] = int(result[i+j+1] +sum/10)

        k = len(result) - 1
        while (result[k] == 0):
            result.pop(k)
            j -= 1



        return result

    def divide(self, A, B):
        pass


if __name__ == '__main__':
    number1 = "2"
    number2 = "10"
    binary_1 = "01"
    binary_2 = "11"
    number3 = "-5"
    number4 = "7"

    calc = Calculator()

    num1 = calc.convert(number1)
    num2 = calc.convert(number2)
    res1 = calc.add(num1, num2)

    b_num1 = calc.convert(binary_1)
    b_num2 = calc.convert(binary_2)
    res1_bin = calc.add(b_num1, b_num2, base=2)  # Change system

    num3 = calc.convert(number3)
    num4 = calc.convert(number4)


    res2 = calc.substract(num1, num2)  # Return negative number
    res3 = calc.multiply(num3, num4)  # Multiply


    print(f"Wynik dodawania: {calc.decode(res1)}")
    print(f"Wynik dodawania binarnego: {calc.decode(res1_bin)}")
    print(f"Wynik odejmowania: {calc.decode(res2)}")
    print(f"Wynik mnożenia: {calc.decode(res3)}")

    calc.m_sing = True
