from urllib.request     import Request, urlopen # Biblioteca usada para realizar requests
from bs4                import BeautifulSoup # Biblioteca usada para executar o scrapping da página
from nltk.tokenize      import word_tokenize, sent_tokenize # Biblioteca utilizada para dividir o texto em palavras e sentenças
from nltk.corpus        import stopwords # Biblioteca utilizada para definir as stopwords
from string             import punctuation # Biblioteca utilizada para identificar pontuação
from nltk.probability   import FreqDist # Biblioteca utilizada para criar a distribuição de frequência
from collections        import defaultdict # Biblioteca utilizada para manuzear um dicionário de palavras
from heapq              import nlargest # Biblioteca utilizada para ordenar as sentenças 

# Declara a URL que será visitada com o request especificado
link = Request('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html', headers={'User-Agent': 'Mozilla/5.0'})

# O retorno do request é armazenado em 'pagina'
pagina = urlopen(link).read().decode('utf-8', 'ignore')

# Dentro da página retornada, busca a div com id 'noticia', que é onde o texto está
soup = BeautifulSoup(pagina, "lxml")
texto = soup.find(id="noticia").text

# Divide o texto em sentenças
sentencas = sent_tokenize(texto)
# Divide o texto em palavras
palavras = word_tokenize(texto.lower())

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

# Seleciona as n (nesse caso, as 4) sentenças mais importantes para o resumo
idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

# Imprime o resumo
for i in sorted(idx_sentencas_importantes):
    print(sentencas[i])