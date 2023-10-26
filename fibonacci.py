lenght = 10

fibo = [0, 1]

for i in range(2, lenght):
  number1 = fibo[i - 2]
  number2 = fibo[i - 1]
  nextNumber = number1 + number2

  fibo.append(nextNumber)
  
print(fibo)