dinheiro = float(input('O seu produto terá um desconto na compraa efetuada: '))
desconto = (dinheiro*0.05)
total = (dinheiro - desconto)

print('Com o desconto de 5% aplicado ao produto o valor caiu para {:.2f}'.format(total))