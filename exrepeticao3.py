#nome, idade, salário, sexo e estado civil
nome = str(input('Digite o seu nome: '))
while len(nome) <= 3:
    nome = str(input('Digite um nome com mais de 3 caracteres: '))
idade = int(input('Digite a sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Digite uma idade válida: '))
salario = float(input('Digite o seu salário: R$ '))
while salario <= 0:
    salario = float(input('Digite um salário maior do que R$ 0 '))
sexo = str(input('Digite seu sexo (f)-feminino ou (m)-masculino: '))
while sexo != 'f' and sexo != 'm':
    sexo = str(input('Digite um sexo válido f ou m: '))
es = str(input('Digite seu estado civil onde, (s)-solteira, (c)-casada, (v)-viuva, (d)-divorciada: '))
while es != 's' and es != 'c' and es != 'v' and es != 'd':
    es = str(input('Digite um estado civil válido (s, c, v, d): '))
print('O nome digitado foi {}, a idade foi {} anos, o salário ganho foi R${}, seu sexo é {} e seu estado civil {}'.format(nome, idade, salario, sexo, es))
