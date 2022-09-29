from TarefaTabela2.Tabela import Tabela


from Tabela import Tabela

'''
AUTORES:
Carlos Eduardo de Andrade Pereira - 168321
Luiz Otávio de Oliveira Silva - 240519
Pedro Augusto Canuto de Oliveira - 186691
'''

# A tarefa desta semana é uma continuação da implementação da tabela.
# Primeiramente deve existir um construtor da classe Tabela com
# zero ou um argumentos. Se for executado
teste = Tabela()
# deve ser criada uma tabela vazia.
# por outro lado, se for passado no construtor o nome de um arquivo,
# a tabela deve ser carregada deste arquivo.
# Veja o exemplo:
teste = Tabela("carros.txt")
print(teste)
# O arquivo carros.txt que possui a tabela vai ser dado para você.
# Veja abaixo o formato do arquivo.
# ['placa','ano','marca','modelo']
# ['PAF1A79',2020,'volkswagem','gol']
# ['OWH2Z46',2017,'volkswagem','polo']
# ['IRD3T61',2016,'volkswagem','gol']
# ['XTP8W51',2020,'chevrolet','onix']
# . . ..
#
# A primeira linha possui o cabeçalho da tabela, e as próximas linhas
# contêm os registros da tabela. O seu construtor deve funcionar nestes dois
# casos.
#
#
# Agora você deve criar um método em Tabela que salva a tabela em um arquivo.
teste.writeFile("saida.txt")

# Este método cria um arquivo contendo os dados da tabela. Ele deve funcionar de maneira
# a que os dados escritos no arquivo possam novamente subir para uma tabela, conforme
# mostrado abaixo:

teste = Tabela("saida.txt")
print(teste)