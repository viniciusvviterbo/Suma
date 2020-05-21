import argparse # Biblioteca utilizada para gerenciar os argumentos do terminal
import os # Biblioteca utilizada para gerenciar os arquivos do sistema operacional
from nltk.tokenize import word_tokenize # Biblioteca utilizada para dividir o texto em palavras
from nltk.tokenize import sent_tokenize # Biblioteca utilizada para dividir o texto em sentenças
from nltk.corpus import stopwords # Biblioteca utilizada para definir as stopwords
from string import punctuation # Biblioteca utilizada para identificar pontuação
from nltk.probability import FreqDist # Biblioteca utilizada para criar a distribuição de frequência
from collections import defaultdict # Biblioteca utilizada para manuzear um dicionário de palavras
from heapq import nlargest # Biblioteca utilizada para ordenar as sentenças 

# Configuracao dos argumentos
parser = argparse.ArgumentParser(description = 'Software sumarizar textos.')
parser.add_argument('-f', action = 'store', dest = 'caminho_arquivo', default = '', required = True, help = 'Arquivo com o texto a ser sumarizado.')
parser.add_argument('-n', action = 'store', dest = 'n_frases', default = 5, required = True, help = 'Número de frases que irão compor o resumo gerado.')

# Recebe os argumentos. Se a variável nao for passada, retorna -h
arguments = parser.parse_args()
# Lê o conteúdo do texto
with open(arguments.caminho_arquivo, 'r') as file:
    texto_original = file.read().replace('\n', '')

try:
    # Define o nome base do arquivos a ser criado
    nome_arquivo = os.path.splitext(os.path.basename(arguments.caminho_arquivo))[0]
        
    # Divide o texto em sentenças
    sentencas = sent_tokenize(texto_original)
    # Divide o texto em palavras
    palavras = word_tokenize(texto_original.lower())

    # Separa as palavras que possuem significado unicamente sintático das que também possuem significado contextual
    stopwords = set(stopwords.words('portuguese') + list(punctuation))
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

    # Define a distribuição de frequência em que palavras aparecem para descobrir sua importância
    frequencia = FreqDist(palavras_sem_stopwords)

    # Define uma pontuação para ordenar a importância das sentenças no texto
    sentencas_importantes = defaultdict(int)

    # Percorre todas as sentenças do texto e coletar dados oriundos delas
    for i, sentenca in enumerate(sentencas):
        for palavra in word_tokenize(sentenca.lower()):
            if palavra in frequencia:
                sentencas_importantes[i] += frequencia[palavra]

    # Seleciona as n sentenças mais importantes para o resumo. Esse número é informado pelo usuário
    idx_sentencas_importantes = nlargest(int(arguments.n_frases), sentencas_importantes, sentencas_importantes.get)

    # Cria o arquivo de resumo
    arquivo_resumo = open(nome_arquivo + '_resumo.txt','w')
    # Declara o texto a ser escrito no resumo
    resumo_conteudo = ''
    # Adiciona as sentenças mais importantes
    for i in sorted(idx_sentencas_importantes):
        resumo_conteudo += (sentencas[i] + '\n')
    # Escreve o conteúdo ao arquivo
    a = arquivo_resumo.write(resumo_conteudo)
    # Fecha o arquivo
    arquivo_resumo.close()

except():
    print('Algum erro ocorreu.')