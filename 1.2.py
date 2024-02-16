cost = int(input('Введите общую стоимость: '))
if cost >= 4608:
    totalcst = (cost-(96*48))/(96/16)
    print(int(totalcst), '- стоимость золотых часов')
else:
    print('wrong cost')

