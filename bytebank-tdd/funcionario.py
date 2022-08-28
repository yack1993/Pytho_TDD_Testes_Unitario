from bytebank import Funcionario

funcionario = Funcionario('Eduardo Fulileco', '10/12/1990', 1000)

#print(funcionario)
#print("Sua idade é: ",funcionario.idade())


#teste automatizado
def teste_idade():
    func_teste = Funcionario('Eduardo Fulileco', '10/12/1990', 1000)
    print(func_teste.idade())

teste_idade()