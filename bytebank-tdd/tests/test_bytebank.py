import pytest
from codigo.bytebank import Funcionario
from pytest import mark

class TesteClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' #Given(contexto)
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        result = funcionario_teste.idade() #When(ação)

        assert result == esperado #then(desfecho)

    def test_quando_sobrenome_recebe_Eduardo_Geraldo_deve_retornar_Geraldo(self):
        entrada = ' Eduardo Geraldo ' # Given
        esperado = 'Geraldo'

        Geraldo = Funcionario(entrada, '11/11/2000', 1111)
        resultado = Geraldo.sobrenome() #When

        assert resultado == esperado

    #@mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_nome = 'Eduardo Geraldo'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # when
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2008', entrada)
        result = funcionario_teste.calcular_bonus()

        assert result == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_receb_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000

            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            result = funcionario_teste.calcular_bonus()

            assert result



