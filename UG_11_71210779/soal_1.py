def add(inputan1, inputan2):
    return inputan1 + inputan2
 
def subtract(inputan1, inputan2):
    return inputan1 - inputan2
 
def multiply(inputan1, inputan2):
    return inputan1 * inputan2
 
def divide(inputan1, inputan2):
    return inputan1 / inputan2
 
while True:
    print('\nSelect operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Close')
    operasi = int(input('Enter choice(1/2/3/4/5): '))
    if operasi == 1:
        inputan1 = float(input('Enter first number: '))
        inputan2 = float(input('Enter second number: '))
        print("{}".format(add(inputan1, inputan2)))
    elif operasi == 2:
        inputan1 = float(input('Enter first number: '))
        inputan2 = float(input('Enter second number: '))
        print("{}".format(subtract(inputan1, inputan2)))
    elif operasi == 3:
        inputan1 = float(input('Enter first number: '))
        inputan2 = float(input('Enter second number: '))
        print("{}".format(multiply(inputan1, inputan2)))
    elif operasi == 4:
        inputan1 = float(input('Enter first number: '))
        inputan2 = float(input('Enter second number: '))
        print("{}".format(divide(inputan1, inputan2)))
    elif operasi == 5:
        break
    else:
        print('Enter choice 1 until 5')
