import csv

arquivo = open('ocorrencia.csv', 'r')

# converte o arquivo aberto em csv. ´´E preciso passar o delimitador, pois o arquivo csv usa como padrão a vírgula, porém o delimitador do arquivo csv é o ;
leitor_csv = csv.reader(arquivo, delimiter=';')

# Cria um arquivo para escrever os casos de Joinville
casosJoinville = open('casosJoinville.txt', 'w')

# é preciso deixar como comentário para não fazer o cursor ir para o final do arquivo, e assim o proximo for não vai achar o conteúdo do arquivo csv, pois o cursor já estará no final do arquivo
# vizualizando o conteúdo do arquivo csv
#  for linha in leitor_csv:
#      print(linha)

for linha in leitor_csv:
    if linha[8] == 'JOINVILLE':
        codigo_ocorrencia = linha[0]
        ocorrencia_classificacao = linha[5]
        ocorrencia_dia = linha[12]
        investigacao_status = linha[15]

        print(linha)

        casosJoinville.write(
            f'{codigo_ocorrencia}|{ocorrencia_classificacao}|{ocorrencia_dia}|{investigacao_status}\n')


casosJoinville.close()
arquivo.close()
