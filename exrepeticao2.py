#solicitar um nome de usuário e uma senha, e a senha não pode ser igual ao nome do usuário
nome = str(input('Digite o nome do usuário: '))
senha = str(input('Digite uma senha: '))
while senha == nome:
    senha = str(input('A senha digitada é igual o nome do usuário, digite uma senha diferente: '))
print = input('seu nome de usuário será {} e sua senha será {}'.format(nome, senha))
